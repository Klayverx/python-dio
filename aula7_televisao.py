class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        #se estiver ligada
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

# print(__name__)
# Só executa se quando quem tiver chamando for o mesmo arquivo
# Quando executamos o próprio arquivo, o "__name__" é "__main__"
if __name__ == "__main__":
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))