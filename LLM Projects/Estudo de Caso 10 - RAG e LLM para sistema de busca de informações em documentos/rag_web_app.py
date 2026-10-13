# Módulo da Interface Web e Consulta à API

import os
import json
import urllib.parse
import re
import streamlit as st
import requests
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="RAG Project", page_icon=":100:", layout="centered")

st.title('_:green[Assistente IA]_')
st.title('_:blue[Busca com IA Generativa e RAG]_')

question = st.text_input("Digite Uma Pergunta Para a IA Executar Consulta nos Documentos:", "")

if st.button("Enviar"):
    st.write("A pergunta foi: \"", question+"\"")
    
    url = "http://127.0.0.1:9000/rag_api"
    payload = json.dumps({"query": question})
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        st.error(f"Erro na API ({response.status_code}): {response.text}")
        st.stop()

    answer = response.json().get("answer", "")
    documents = response.json().get("context", [])

    if not answer:
        st.warning("A API respondeu, mas sem conteúdo.")
        st.stop()
    
    answer_exibicao = answer
    
    # 1. Cria um dicionário mapeando cada "doc_id" retornado pela API para o seu Link formatado em Markdown
    doc_map = {}
    for doc in documents:
        doc_id = doc.get('doc_id')
        path = doc.get('path')
        if doc_id and path:
            url_path = urllib.parse.quote(path)
            link = f"http://127.0.0.1:9000/arquivos/{url_path}"
            # O texto em markdown vira: [ID123](http://127.0.0.1:9000/arquivos/...)
            doc_map[doc_id] = f"[{doc_id}]({link})"
            
    if doc_map:
        # 2. Ordenamos os IDs pelo tamanho (do maior pro menor). 
        # Isso evita que um ID curto tipo "ID12" substitua a metade de um ID longo tipo "ID12345".
        sorted_ids = sorted(doc_map.keys(), key=len, reverse=True)
        escaped_ids = [re.escape(did) for did in sorted_ids]
        
        # 3. Cria uma regra Regex que localiza QUALQUER UM dos IDs no texto da resposta
        pattern = re.compile("|".join(escaped_ids))
        
        # 4. Substitui todos os IDs encontrados pelos seus respectivos hiperlinks em UMA ÚNICA PASSAGEM
        answer_exibicao = pattern.sub(lambda match: doc_map[match.group(0)], answer_exibicao)

    # Exibe a resposta final com todos os links embutidos
    st.markdown(answer_exibicao)