from api.client import fetch_users, fetch_user_by_id, fetch_user_posts
# Importa as funções fetch_users, fetch_user_by_id e fetch_user_posts do módulo api.client

def menu():
    # Define a função menu que exibe o menu de opções para o usuário e executa a ação correspondente baseada na escolha do usuário.
    while True:
        # Inicia um loop infinito para exibir o menu repetidamente até que o usuário escolha sair.
        
        print("\nMenu:")
        # Exibe o título do menu.
        
        print("1. Buscar usuário por ID")
        # Exibe a opção 1 do menu: Buscar usuário por ID.
        
        print("2. Listar títulos dos posts por ID do usuário")
        # Exibe a opção 2 do menu: Listar títulos dos posts por ID do usuário.
        
        print("3. Sair")
        # Exibe a opção 3 do menu: Sair.
 
        choice = input("\nEscolha uma opção: ")
        # Solicita ao usuário que escolha uma opção do menu e armazena a escolha na variável choice.
        
        if choice == '1':
            # Verifica se a escolha do usuário é '1'.
            user_id = input("\nDigite o ID do usuário: ")
            # Solicita ao usuário que digite o ID do usuário e armazena o ID na variável user_id.
            
            fetch_user_by_id(user_id)
            # Chama a função fetch_user_by_id passando o ID do usuário como argumento.
        elif choice == '2':
            # Verifica se a escolha do usuário é '2'.
            user_id = input("\nDigite o ID do usuário: ")
            # Solicita ao usuário que digite o ID do usuário e armazena o ID na variável user_id.
            
            fetch_user_posts(user_id)
            # Chama a função fetch_user_posts passando o ID do usuário como argumento.
        elif choice == '3':
            # Verifica se a escolha do usuário é '3'.
            print("\nSaindo...")
            break
        # Sai do loop e termina o programa.
        else:
            # Informa ao usuário que a opção é inválida
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente (não importado como módulo).
    
    print("\nLista dos usuários:\n")
    # Exibe uma mensagem indicando que a lista de usuários será exibida.
    
    fetch_users()
    # Chama a função fetch_users para listar todos os usuários.
    
    menu()
    # Chama a função menu para exibir o menu de opções para o usuário.