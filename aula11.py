# Tratamento de erros

lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print("Fechando o arquivo")
    arquivo.close()

# Encadeamento de except
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero")
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por 0!")
except ArithmeticError:
    print("Houve um erro ao executar uma operação eritmética")
except IndexError:
    print("Erro ao acessar um índice inválido da lista")
except Exception as ex:
    print("Erro desconhecido. Erro: {}" .format(ex))
else:
    print("Executa quando não ocorre exceção")

# Sempre executa, independente dos erros
finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()
