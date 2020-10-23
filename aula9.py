# w => Gera arquivo || sobrescreve
# a => Gera arquivo || acrescenta
# r => Leitura do arquivo

# módulo para manipulação de arquivos
import shutil

def escrever_arquivo(texto):
    diretorio = 'K:/Codes/PythonProjects/DIO-python'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)

    # separando os alunos pela quera de linha
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)

    lista_media = []

    for x in aluno_nota:
        # Separando os nomes das notas
        lista_notas = x.split(',')
        # Nome dos alunos nas primeiras posições
        aluno = lista_notas[0]
        # Removendo o nome dos alunos
        lista_notas.pop(0)
        # retorna a média dos valores que foram convertidos de str para int
        media = lambda notas: sum([int(i) for i in notas]) / 4

        # print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})

    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'K:/Codes/PythonProjects/DIO-python/testes_arquivos/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'K:/Codes/PythonProjects/DIO-python/testes_arquivos/notas_alunos.txt')

if __name__ == "__main__":
    # copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)

    # atualizar_arquivo('notas.txt', lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = '\nGustavo 7, 8, 0, 6\n'
    # ler_arquivo('teste.txt')