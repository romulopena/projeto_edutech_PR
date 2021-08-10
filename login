nome = input('Digite o seu nome: ')
senha = input('Digite sua senha: ')

while senha == nome:
    print('Sua senha deve ser diferente do seu nome!')
    nome = input('Digite o seu nome: ')
    senha = input('digite sua senha: ')


else:
    print('Sua conta foi criada com sucesso')
