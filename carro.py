class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def Cambio(self):
        print('automatico')
    
    def Combustivel(self):
        print('Gasolina')
        
    def Volante(self):
        print('eletrico')
    
carro1 = Carro('GM', 'Spin','2016')
print (carro1)
carro1.Cambio()
carro1.Combustivel()
carro1.Volante()