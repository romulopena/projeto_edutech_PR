#IMC PESO IDEAL
print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxxx     I M C   xxxxxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxxxx")

#entrada
nome = input("Olá! Bem vindo!!! me diga seu nome: ")
altura = float(input("{0} , qual a sua altura?: ".format(nome)))
peso = float(input("{0} , diga-me também o seu peso: ".format(nome)))
#processamento
imc = (peso / (altura * altura))
#saida
print("{0}, Seu IMC é: {1:.2f} !!!".format(nome, imc))
