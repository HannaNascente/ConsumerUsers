# Este módulo contém funções para interagir com a API de usuários.

import requests
# Importa a biblioteca requests para fazer requisições HTTP.

from .endpoints import USER_POSTS_ENDPOINT, USERS_ENDPOINT, USER_BY_ID_ENDPOINT
# Importa os endpoints da API do módulo endpoints. 
# USER_POSTS_ENDPOINT: Endpoint para obter os posts de um usuário específico.
# USERS_ENDPOINT: Endpoint para obter todos os usuários.
# USER_BY_ID_ENDPOINT: Endpoint para obter um usuário específico pelo ID.

def fetch_users():
    # Busca todos os usuários da API e imprime seus IDs e nomes.
    try:
        # Faz uma requisição GET para o endpoint de usuários
        response = requests.get(USERS_ENDPOINT)
        
        # Verifica se houve algum erro na requisição (status code 4xx/5xx) e levanta uma exceção haja erro.
        response.raise_for_status() 
        
        # Converte a resposta JSON em um objeto Python (lista de usuários)
        users = response.json()
        
        # Itera sobre a lista de usuários
        for user in users:
            # Imprime o id e o nome de cada usuário
            print(f"ID: {user['id']}, Name: {user['name']}")
        
    # Captura e trata erros HTTP
    except requests.exceptions.HTTPError as http_err: 
        print(f"\nOcorreu um erro HTTP: {http_err}")
        
    # Captura e trata erros de conexão
    except requests.exceptions.ConnectionError as conn_err: 
        print(f"\nOcorreu um de conexão: {conn_err}")
        
    # Captura e trata erros de timeout
    except requests.exceptions.Timeout as timeout_err: 
        print(f"\nOcorreu um erro de Timeout: {timeout_err}")
    
    # Captura e trata outros erros relacionados à requisição
    except requests.exceptions.RequestException as req_err: 
        print(f"\nOcorreu um erro: {req_err}")
    
    
def fetch_user_by_id(user_id):
    # Busca um usuário pelo ID e imprime seu nome e email.
    try:
        # Formata a URL do endpoint com o ID do usuário
        url = USER_BY_ID_ENDPOINT.format(user_id)
        
        # Faz uma requisição GET para o endpoint do usuário específico
        response = requests.get(url)
        
        # Verifica se houve algum erro na requisição (status code 4xx/5xx) e levanta uma exceção haja erro.
        response.raise_for_status() 
        
        # Converte a resposta JSON em um objeto Python (dicionário do usuário)
        user = response.json()
        
        # Imprime o nome e o email do usuário
        print(f"\nNome: {user['name']}, Email: {user['email']}")
         
    # Captura e trata erros HTTP   
    except requests.exceptions.HTTPError as http_err: 
        if response.status_code == 404:
            # Caso o status code seja 404, informa que o ID do usuário é inválido
            print(f"\nID de usuário inválido: {user_id}")
        else:
            # Para outros erros HTTP, imprime a mensagem de erro
            print(f"\nOcorreu um erro HTTP: {http_err}")
        
    # Captura e trata erros de conexão
    except requests.exceptions.ConnectionError as conn_err: 
        print(f"\nOcorreu um de conexão: {conn_err}")
        
    # Captura e trata erros de timeout
    except requests.exceptions.Timeout as timeout_err: 
        print(f"\nOcorreu um erro de Timeout: {timeout_err}")
    
    # Captura e trata outros erros relacionados à requisição
    except requests.exceptions.RequestException as req_err: 
        print(f"\nOcorreu um erro: {req_err}")

def fetch_user_posts(user_id):
    # Busca os posts de um usuário pelo ID e imprime os títulos dos posts.
    try:
        # Formata a URL do endpoint com o ID do usuário
        url = USER_POSTS_ENDPOINT.format(user_id)
    
        # Faz uma requisição GET para o endpoint dos posts do usuário específico
        response = requests.get(url)
        
        # Verifica se houve algum erro na requisição (status code 4xx/5xx) e levanta uma exceção haja erro.
        response.raise_for_status()
        
        # Converte a resposta JSON em um objeto Python (lista de posts)
        posts = response.json()
        
        # Itera sobre a lista de posts
        for post in posts:
            # Imprime o título de cada post
            print(f"Title: {post['title']}")
            
    # Captura e trata erros HTTP   
    except requests.exceptions.HTTPError as http_err: 
        if response.status_code == 404:
            # Caso o status code seja 404, informa que o ID do usuário é inválido
            print(f"\nID de usuário inválido: {user_id}")
        else:
            # Para outros erros HTTP, imprime a mensagem de erro
            print(f"\nOcorreu um erro HTTP: {http_err}")
        
    # Captura e trata erros de conexão
    except requests.exceptions.ConnectionError as conn_err: 
        print(f"\nOcorreu um de conexão: {conn_err}")
        
    # Captura e trata erros de timeout
    except requests.exceptions.Timeout as timeout_err: 
        print(f"\nOcorreu um erro de Timeout: {timeout_err}")
    
    # Captura e trata outros erros relacionados à requisição
    except requests.exceptions.RequestException as req_err: 
        print(f"\nOcorreu um erro: {req_err}")