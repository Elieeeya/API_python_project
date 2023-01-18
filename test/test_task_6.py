from conftest import *


url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/fio'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 793d2830a6360a1569c8e7b9dd1afeb2f57ffa77',
    'Cookie': '__ddg1_=tsiWpEpXN9YCR5LYMZxu'
}

body = [
    {'query': '"Андрей Мал'}
]


# Найдите в ответах фамилию "Малахов" (именно фамилию).
def test_find_user():
    response = requests.post(url, json=body[0], headers=headers)
    assert response.status_code == 200
    assert response.json()['suggestions'][5]['data']['surname'] == 'Малахов'
