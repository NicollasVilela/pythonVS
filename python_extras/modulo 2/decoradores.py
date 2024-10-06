'''from typing import Any


def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func() 
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")
    
minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
        
    def __call__(self) -> Any:
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")
        
@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")
    
segunda_funcao()'''


# DECORADORES COMUNS ====================================

# @classmethod
# @Staticmethod

class MinhaClasse:
    valor = 10 #atributo da classe
    def __init__(self, nome) -> None:
        self.nome = nome #atributo da instancia
        
    #requer uma instancia pra se chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
 
    @classmethod
    def metodo_classe(cls):
        return f"Método da classe chamado para valor = {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"
        
        
         
obj = MinhaClasse(nome = "Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla, 2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a = 10, b = 15))    