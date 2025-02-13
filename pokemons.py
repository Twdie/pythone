import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '463b8ea525ceaeaa954abf41070ac782'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
BODY_CREATE_POKEMON={
    "name": "generate",
    "photo_id": -1
}
body_change_name_pokemon={
    "pokemon_id": "233409",
    "name": "generate",
    "photo_id": -1
}
body_add_pokeboll={
    "pokemon_id": "233409"
}
body_battle={
    "attacking_pokemon": "9",
    "defending_pokemon": "30"
}
response_create=requests.post(url=f'{URL}/pokemons',headers=HEADER,json=BODY_CREATE_POKEMON)
print(response_create.text)
body_change_name_pokemon['pokemon_id']=response_create.json()['id']
response_change_name_pokemon=requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_change_name_pokemon)
print(response_change_name_pokemon.text)
body_add_pokeboll['pokemon_id']=response_create.json()['id']
response_add_pokeboll=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER,json=body_add_pokeboll)
print(response_add_pokeboll.text)

'''Дальше я немного упоролся и воссоздал весь путь по проведению битвы в один клик'''
response_get_list_pokemons=requests.get(url=f'{URL}/pokemons',params={'in_pokeball':1,'status':1})
body_battle['defending_pokemon']=response_get_list_pokemons.json()['data'][3]['id']
body_battle['attacking_pokemon']=response_create.json()['id']
response_battle=requests.post(url=f'{URL}/battle',headers=HEADER,json=body_battle)
print(response_battle.text)