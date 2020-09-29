resultado = 0
for x in range (1, 10):
    if x < 9:
        resultado += 1
print(resultado)

# a = int(input('Entre com a primera nota: '))
# while a > 10:
#     a = int(input('Você digitou errado. Digite novamente a nota: '))
# b = int(input('Entre com a segunda nota: '))
# while b > 10:
#     b = int(input('Você digitou errado. Digite novamente a nota: '))
# c = int(input('Entre com a terceira nota: '))
# while c > 10:
#     c = int(input('Você digitou errado. Digite novamente a nota: '))
# d = int(input('Entre com a quarta nota: '))
# while d > 10:
#     d = int(input('Você digitou errado. Digite novamente a nota: '))
#
# media = (a+b+c+d) / 4
#
# print('Média: {}'.format(media))


# nota = int(input('Entre com a nota: '))
#
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota: '))
# print(nota)


# a = 0
# while a <= 10:
#     print(a)
#     a += 1


# a = int(input('entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)


# a = int(input('Entre com um número: '))
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo!'.format(a))