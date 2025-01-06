import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = '256fd63f176c6a7d136fab1d5db3ab4e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '16462'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', headers = HEADER, params = {'trainer_id': TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] == 'Соколенок228'

