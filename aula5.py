lista = [1, 10, 5, 7]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# imutável
tupla = (1, 10, 12, 14)
print(tupla)

# tupla[0] = 12

print(len(tupla))

# conversão de lista para tupla
tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)

# conversão de tupla para lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

lista_numerica[1] = 100
print(lista_numerica)



# ordem crescente
# lista.sort()
# ordem alfabética
# lista_animais.sort()
# print(lista)
# print(lista_animais)
#
# # contrário do sort
# lista.reverse()
# lista_animais.reverse()
# print(lista)
# print(lista_animais)


# nova_lista = lista_animais * 3

# print(nova_lista)
# print (lista_animais[1])

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#
# # soma de uma lista
# print(sum(lista))
#
# # maior valor de uma lista de números
# print(max(lista))



# if 'lobo' in lista_animais:
#     print("Existe um lobo na lista")
# else:
#     print("Não existe um lobo na lista")
#     # adicionando um elemento na lista
#     lista_animais.append('lobo')

# print(lista_animais)
#
# lista_animais.pop()
#
# print(lista_animais)
#
# lista_animais.pop(0)
#
# print(lista_animais)
#
# lista_animais.remove('elefante')
#
# print(lista_animais)

