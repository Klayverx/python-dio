a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma}'
      '\nSubtração: {sub}'
      '\nMultiplicação: {mult}'
      '\nDivisão: {div}'
      '\nResto: {rest}' .format(soma=soma,
                                sub=subtracao,
                                mult=multiplicacao,
                                div=divisao,
                                rest=resto))

print(resultado)

# x = '2'
# print(int(x))