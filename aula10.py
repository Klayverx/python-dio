# Datas em ython

from datetime import date, time, datetime, timedelta

# .strftime transforma os dados em string de acordo com as diretivas da biblioteca
# .strptime transforma de string para o tipo datetime


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    data_atual_str = data_atual.strftime('%A/%B/%Y')

    print(data_atual_str)
    print(type(data_atual_str))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H : %M : %S')
    print(horario_str)
    print(type(horario_str))


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())

    # Solução para converter para português
    tupla = ('Segunda', 'Terça', 'Quarta',
             'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    # Criando uma data
    data_criada = datetime(2020, 5, 27, 12, 15, 12)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2020 20:34:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(data_convertida.weekday())

    # Operações com datas
    nova_data = data_convertida - timedelta(days=365, hours=12, minutes=30)
    print(nova_data)


def questoes():
    data_viagem = datetime.now() - timedelta(days=1)
    print(datetime.now().weekday())  # retornou 0
    print(data_viagem)

    data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora = time(hour=13, minute=14, second=00)
    print('{} às {}'.format(data, hora))

    # hour = timedelta(hours=15)
    # soma = hour + 1
    # print(soma)

    data_atual = datetime.now()
    resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(resultado)


if __name__ == "__main__":
    # trabalhando_com_date()
    # trabalhando_com_time()
    # trabalhando_com_datetime()
    questoes()
