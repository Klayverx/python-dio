class Calculadora:
    #vai ser executado sempre que for instanciado
    def __init__(self, num1, num2):
        #"vazio", não faz nada
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.divisao(10, 5))
print(calculadora.multiplicacao(100, 2))