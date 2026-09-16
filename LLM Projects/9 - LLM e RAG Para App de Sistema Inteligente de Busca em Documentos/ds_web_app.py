# Projeto 10 - IA Generativa e RAG Para App de Sistema Inteligente de Busca em Documentos - Frontend
# Módulo da Interface Web e Consulta à API

# Importa o módulo re de expressão regular
import re

# Importa o módulo streamlit com o alias st
import streamlit as st

# Importa o módulo requests
import requests

# Importa o módulo json
import json

# Filtra warnings
import warnings
warnings.filterwarnings('ignore')

# Configurando o título da página e outras configurações (favicon)
st.set_page_config(page_title="DSA Projeto 10", page_icon=":100:", layout="centered")

# Define o título do aplicativo Streamlit
st.title('_:green[DSA - Projeto 10]_')
st.title('_:blue[Busca com IA Generativa e RAG]_')

# Cria uma caixa de texto para entrada de perguntas
question = st.text_input("Digite Uma Pergunta Para a IA Executar Consulta nos Documentos:", "")

# Verifica se o botão "Perguntar" foi clicado
if st.button("Enviar"):
    
    # Exibe a pergunta feita
    st.write("A pergunta foi: \"", question+"\"")
    
    # Define a URL da API
    url = "http://127.0.0.1:8000/dsa_api"

    # Cria o payload da requisição em formato JSON
    payload = json.dumps({"query": question})
    
    # Define os cabeçalhos da requisição
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    # Faz a requisição POST à API
    response = requests.request("POST", url, headers=headers, data=payload)

    # Obtém a resposta da API e extrai o texto da resposta à pergunta
    answer = json.loads(response.text)["answer"]
    
    # Compila uma expressão regular para encontrar referências a documentos
    rege = re.compile("\[Document\ [0-9]+\]|\[[0-9]+\]")
    
    # Encontra todas as referências a documentos na resposta
    m = rege.findall(answer)
    
    # Inicializa uma lista para armazenar os números dos documentos
    num = []
    
    # Extrai os números dos documentos das referências encontradas
    for n in m:
        num = num + [int(s) for s in re.findall(r'\b\d+\b', n)]

    # Exibe a resposta da pergunta usando markdown
    st.markdown(answer)
    
    # Obtém os documentos do contexto da resposta
    documents = json.loads(response.text)['context']
    
    # Inicializa uma lista para armazenar os documentos que serão exibidos
    show_docs = []
    
    # Adiciona os documentos correspondentes aos números extraídos à lista show_docs
    for n in num:
        for doc in documents:
            if int(doc['id']) == n:
                show_docs.append(doc)
                
    # Inicializa uma variável para o identificador dos botões de download
    dsa_id = 12688126414389178
    
    # Exibe os documentos expandidos com botões de download
    for doc in show_docs:
        
        # Cria um expansor para cada documento
        with st.expander(str(doc['id'])+" - "+doc['path']):
            
            # Exibe o conteúdo do documento
            st.write(doc['content'])
            
            # Abre o arquivo do documento e cria um botão de download
            with open(doc['path'], 'rb') as f:
                
                st.download_button("Download do Arquivo", f, file_name = doc['path'].split('/')[-1], key = dsa_id)
                
                # Incrementa o identificador do botão para download
                dsa_id = dsa_id + 1
