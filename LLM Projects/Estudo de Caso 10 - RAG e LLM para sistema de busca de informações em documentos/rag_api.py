import os
import re
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Jinja2 para templates de prompt
from jinja2 import Environment, FileSystemLoader, select_autoescape

# LangChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient

# Env vars
try:
    import rag_env_var
except ImportError:
    rag_env_var = None

import warnings
warnings.filterwarnings('ignore')


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("rag_api")

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)


# ============================================================
# CONFIGURAÇÕES
# ============================================================

# Modelos
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "openai/gpt-oss-20b"

# Qdrant
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "ragVectorDB"

# RAG
K_RESULTADOS = 8

# LLM
LLM_TEMPERATURE = 0.2
LLM_MAX_TOKENS = 4096

# NVIDIA
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"

# Jinja2
PROMPTS_DIR = Path(__file__).parent / "prompts"

# Variáveis passadas pro template
PROMPT_VARIAVEIS = {
    "competencia": None,                  # ex.: "direito_publico" (deixe None se genérico)
    "incluir_valores_monetarios": True,
}


# ============================================================
# JINJA2 SETUP
# ============================================================

logger.info(f"Configurando Jinja2. Diretório de prompts: {PROMPTS_DIR}")

# Cria a pasta caso não exista durante o carregamento inicial (para evitar erros se recém-clonado)
PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

jinja_env = Environment(
    loader=FileSystemLoader(str(PROMPTS_DIR)),
    autoescape=select_autoescape(disabled_extensions=("j2",), default=False),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=False,
)

def renderizar_prompt(template_nome: str, variaveis: dict) -> str:
    """Carrega e renderiza um template Jinja2."""
    template = jinja_env.get_template(template_nome)
    return template.render(**variaveis)


# ============================================================
# INICIALIZAÇÃO
# ============================================================

logger.info(f"Carregando modelo de embedding: {EMBEDDING_MODEL}")
hf = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

logger.info(f"Conectando ao Qdrant em {QDRANT_URL}")
qdrant_client = QdrantClient(QDRANT_URL)
qdrant = Qdrant(qdrant_client, COLLECTION_NAME, hf)
retriever = qdrant.as_retriever(search_kwargs={"k": K_RESULTADOS})

# NVIDIA LLM
nvidia_key = getattr(rag_env_var, "nvidia_key", None) if rag_env_var else os.getenv("NVIDIA_API_KEY")

if nvidia_key:
    logger.info(f"LLM configurado: {LLM_MODEL}")
    llm = ChatOpenAI(
        model=LLM_MODEL,
        base_url=NVIDIA_BASE_URL,
        api_key=nvidia_key,
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS,
    )
else:
    logger.warning("⚠️  NVIDIA_API_KEY não encontrada!")
    llm = None


# ============================================================
# HELPERS
# ============================================================

def extrair_id_documento(path: str) -> str:
    """
    Extrai o ID numérico do nome do arquivo.
    Ex: 'Documentos/72495028 - Outros Anexos.pdf' → 'ID72495028'
    """
    nome = os.path.basename(path)
    match = re.match(r"(\d+)", nome)
    if match:
        return f"ID{match.group(1)}"
    return f"ID_{os.path.splitext(nome)[0].replace(' ', '_')}"


def formatar_documentos(docs) -> str:
    """Formata os documentos recuperados usando IDs."""
    partes = []
    for doc in docs:
        path = doc.metadata.get("path", "desconhecido")
        doc_id = extrair_id_documento(path)
        partes.append(f"[{doc_id}]\n{doc.page_content}")
    return "\n\n---\n\n".join(partes)


def montar_list_res(docs) -> list:
    """Monta a lista de metadados pra retornar ao frontend."""
    return [
        {
            "id": i + 1,
            "doc_id": extrair_id_documento(doc.metadata.get("path", "")),
            "path": doc.metadata.get("path", "desconhecido"),
            "content": doc.page_content # Permite mostrar o conteúdo extraído no Frontend
        }
        for i, doc in enumerate(docs)
    ]


def extrair_texto_resposta(ai_message) -> str:
    """Extrai texto da AIMessage, com fallback pro reasoning do gpt-oss."""
    content = getattr(ai_message, "content", None)
    if content and str(content).strip():
        return content

    extras = getattr(ai_message, "additional_kwargs", {}) or {}
    reasoning = extras.get("reasoning")
    if reasoning and str(reasoning).strip():
        logger.info("Resposta obtida via additional_kwargs.reasoning")
        return reasoning

    metadata = getattr(ai_message, "response_metadata", {}) or {}
    if "reasoning" in metadata and metadata["reasoning"]:
        logger.info("Resposta obtida via response_metadata.reasoning")
        return metadata["reasoning"]

    logger.warning(
        f"AIMessage sem texto útil. "
        f"content={content!r} | additional_kwargs={extras} | metadata={metadata}"
    )
    return (
        "⚠️ O modelo não retornou uma resposta. "
        "Tente reformular a pergunta ou aumentar LLM_MAX_TOKENS."
    )


def limpar_markdown(texto: str) -> str:
    """Remove marcações Markdown, cumprindo o requisito de texto simples."""
    if not isinstance(texto, str):
        return texto
    texto = re.sub(r"^#{1,6}\s+", "", texto, flags=re.MULTILINE)
    texto = re.sub(r"\*\*([^*]+)\*\*", r"\1", texto)
    texto = re.sub(r"\*([^*]+)\*", r"\1", texto)
    texto = re.sub(r"__([^_]+)__", r"\1", texto)
    texto = re.sub(r"_([^_]+)_", r"\1", texto)
    texto = re.sub(r"`([^`]+)`", r"\1", texto)
    texto = re.sub(r"```[\s\S]*?```", "", texto)
    texto = re.sub(r"^[\-\*\+]\s+", "", texto, flags=re.MULTILINE)
    return texto.strip()


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="rag RAG API - Magistrado (Jinja2)",
    description="RAG jurídico com LangChain + Qdrant + NVIDIA NIM + Jinja2",
    version="6.0.0"
)

# Adicionado endpoint estático para acessar os arquivos pdf a partir da web
app.mount("/arquivos", StaticFiles(directory="."), name="arquivos")

class QueryRequest(BaseModel):
    query: str
    template: str = "prompt_contexto.j2"


class QueryResponse(BaseModel):
    context: list
    answer: str


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "rag RAG API - Magistrado",
        "embedding_model": EMBEDDING_MODEL,
        "llm_model": LLM_MODEL,
        "nvidia_configured": llm is not None,
        "framework": "LangChain LCEL + Jinja2 + FastAPI StaticFiles",
        "max_tokens": LLM_MAX_TOKENS,
        "k_resultados": K_RESULTADOS
    }


@app.get("/prompts")
def listar_prompts():
    """Lista os templates de prompt disponíveis."""
    templates = sorted([f.name for f in PROMPTS_DIR.glob("*.j2")])
    return {
        "disponiveis": templates,
        "diretorio": str(PROMPTS_DIR)
    }


@app.post("/rag_api", response_model=QueryResponse)
def rag_api(request: QueryRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")

    logger.info(f"Pergunta recebida: {query[:100]}")
    
    try:
        jinja_template = jinja_env.get_template(request.template)
        system_prompt = jinja_template.render(**PROMPT_VARIAVEIS)
    except Exception as e:
        logger.exception(f"Erro ao carregar o template {request.template}")
        raise HTTPException(status_code=400, detail=f"Erro de template: {e}")

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "DOCUMENTOS DOS AUTOS:\n\n{context}\n\nSOLICITAÇÃO:\n{question}")
    ])

    try:
        docs = retriever.invoke(query)
    except Exception as e:
        logger.exception("Erro na busca vetorial")
        raise HTTPException(status_code=500, detail=f"Erro na busca vetorial: {e}")

    list_res = montar_list_res(docs)

    if llm is None:
        return {
            "context": list_res,
            "answer": "⚠️ Chave da API NVIDIA não configurada."
        }

    rag_chain = (
        {
            "context": retriever | formatar_documentos,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | extrair_texto_resposta
        | limpar_markdown
    )

    try:
        response = rag_chain.invoke(query)
    except Exception as e:
        logger.exception("Erro na chain do LangChain")
        raise HTTPException(status_code=502, detail=f"Erro ao gerar resposta: {e}")

    logger.info(f"Resposta gerada ({len(response)} chars)")
    return {"context": list_res, "answer": response}
