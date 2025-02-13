import requests
import pytest 

URL='https://api.pokemonbattle.ru/v2'
TOKEN='463b8ea525ceaeaa954abf41070ac782'
HEADER={'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
trainer_id='19511'
def test_status_code():
    response=requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response.status_code==200
def test_id_trainer():
    response_id_trainer=requests.get(url=f'{URL}/trainers', headers=HEADER,params={'trainer_id':trainer_id})
    assert response_id_trainer.json()['data'][0]['id']==trainer_id