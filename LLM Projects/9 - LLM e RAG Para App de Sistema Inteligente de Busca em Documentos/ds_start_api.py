# Projeto 10 - IA Generativa e RAG Para App de Sistema Inteligente de Busca em Documentos - Frontend
# Módulo de Inicialização da API

# Import
import uvicorn

# Inicializa a API
if __name__=="__main__":
    uvicorn.run("dsa_api:app", host = '0.0.0.0', port = 8000, reload = False,  workers = 3)