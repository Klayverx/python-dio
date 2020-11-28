import requests

def retorna_dados_cep(cep):
    # API para consulta de CEPs
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())

    dados_cep = response.json()

    print(dados_cep['localidade'])
    print(dados_cep['uf'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemons = response.json()
    print(dados_pokemons['sprites']['front_shiny'])

def retorna_response(url):
    response = requests.get(url)
    print(response.text)

if __name__ == '__main__':
    retorna_response('https://web.digitalinnovation.one/home')
    # retorna_dados_cep(62160000)
    # retorna_dados_pokemon('pikachu')
