# Projeto de Interação com API de Usuários

Este projeto é uma aplicação Python que interage com uma API de usuários. Ele permite buscar todos os usuários, buscar um usuário específico pelo ID e listar os títulos dos posts de um usuário específico.

## Estrutura do Projeto

- `src/api/endpoints.py`: Define os endpoints da API.
- `src/api/client.py`: Contém funções para interagir com a API de usuários.
- `src/main.py`: Contém a função principal que exibe o menu de opções para o usuário e executa as ações correspondentes.
- `src/requirements.txt`: Lista as dependências do projeto.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```sh
pip install -r src/requirements.txt

## Como Executar

cd src
python main.py

## Funcionalidades
* Buscar todos os usuários: A aplicação lista todos os usuários ao iniciar.
* Buscar usuário por ID: O usuário pode buscar um usuário específico pelo ID.
* Listar títulos dos posts por ID do usuário: O usuário pode listar os títulos dos posts de um usuário específico pelo ID.

## Exemplo de Uso
Ao iniciar a aplicação, a lista de usuários será exibida.
O menu de opções será exibido:
Menu:
1. Buscar usuário por ID
2. Listar títulos dos posts por ID do usuário
3. Sair

Escolha uma opção digitando o número correspondente e siga as instruções.

## Autor
Este projeto foi desenvolvido por [Seu Nome].