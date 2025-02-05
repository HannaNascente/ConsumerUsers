# Define a URL base da API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define a URL do endpoint para recuperar todos os usuários
USERS_ENDPOINT = f"{BASE_URL}/users"

# Define a URL do endpoint para recuperar um usuário pelo seu ID
# O {} será substituído pelo ID do usuário ao fazer a requisição
USER_BY_ID_ENDPOINT = f"{BASE_URL}/users/{{}}"

# Define a URL do endpoint para recuperar as postagens feitas por um usuário
# O primeiro {} será substituído pelo ID do usuário ao fazer a requisição
USER_POSTS_ENDPOINT = f"{BASE_URL}/users/{{}}/posts"