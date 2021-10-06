distancia = float(input('informe a distância:'))
velocidade_media = float(input('informe a velocidade média durante o trajeto:'))
tempo = round(distancia / velocidade_media, 2)

print(f'o tempo estimado de viagem é de {tempo}')
