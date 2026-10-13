# Módulo de Inicialização da API

# Import
import uvicorn

# Inicializa a API
if __name__=="__main__":
    uvicorn.run("rag_api:app", host = '0.0.0.0', port = 9000, reload = False,  workers = 4)