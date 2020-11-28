class Error(Exception):
    pass

# Classe personalizada para tratamento de erro
class InputError(Error):
    # Personalizando a mensagem do erro
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            # raise força uma exceção
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido, digite apenas números')
    # ex é o ero encontrado no bloco try
    except InputError as ex:
        print(ex)