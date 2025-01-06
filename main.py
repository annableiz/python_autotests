import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '256fd63f176c6a7d136fab1d5db3ab4e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

pokemon_id = ''

body_pokemon_create = {
    "name": "Petya",
    "photo_id": -1
}



response1 = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_pokemon_create)

pokemon_id = response1.json()['id']

print(" ")
print("1 запрос --> создание покемона")
print(response1.text)

body_pokemon_change = {
    "name": "Kolya",
    "photo_id": 2,
    'pokemon_id': pokemon_id
}

response2 = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_pokemon_change)

print(" ")
print("------------------------------")
print("2 запрос --> смена имени")
print(response2.text)


body_pokemon_pockeball = {
    'pokemon_id': pokemon_id
}


response3 = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokemon_pockeball)

print(" ")
print("------------------------------")
print("3 запрос --> добавление в покеболл")
print(response3.text)
print(" ")