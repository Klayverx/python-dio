conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

# inverso da intersecção
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
# sub-conjunto
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))

# super-conjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'gato', 'cachorro', 'gato', 'elefante']
print('Lista: {}'.format(lista))
# convertendo a lista para conjunto já que não possui duplicidade
conjunto_animais = set(lista)
print('Conjunto: {}'.format(conjunto_animais))
# convertendo de volta o conjunto para lista
lista_animais = list(conjunto_animais)
print('Lista depois da conversão: {}'.format(lista_animais))


# conjunto = {1, 2, 3, 4, 3, 4}
#
# # adicionando um elemento
# conjunto.add(6)
# # removendo um elemento pela posição
# conjunto.discard(2)
#
# print(conjunto)