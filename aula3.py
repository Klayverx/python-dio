a = int(input('Entre com a primera nota: '))
if a > 10:
    a = int(input('Você digitou errado. Digite novamente a nota: '))
b = int(input('Entre com a segunda nota: '))
if b > 10:
    b = int(input('Você digitou errado. Digite novamente a nota: '))
c = int(input('Entre com a terceira nota: '))
if c > 10:
    c = int(input('Você digitou errado. Digite novamente a nota: '))
d = int(input('Entre com a quarta nota: '))
if d > 10:
    d = int(input('Você digitou errado. Digite novamente a nota: '))

media = (a+b+c+d) / 4

print('Média: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('foi informado alguma nota errada!')


# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')

# resto = a % 2
#
# if resto == 0:
#     print('número é par')
# else:
#     print('número é ímpar')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))
#
# print('final do programa')