usuario = input("Informe o nome de usuário: ")
senha = input("Informe a senha do usuário: ")
while senha == usuario:
    print("Senha não pode ser igual ao usuário!!!")
    usuario = input("Informe o nome de usuário novamente: ")
    senha = input("Informe a senha do usuário: ")

    if senha != usuario:
        print("USUÁRIO LOGADO COM SUCESSO!!!!")
