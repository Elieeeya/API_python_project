from conftest import *


url = 'https://reqres.in/api/users'


params = [
    {'page': 1}
]


# Найдите количество пользователей (переменная total) и имя «Charles»
def test_find_user():
    response = requests.get(url, params=params[0])
    assert response.status_code == 200
    total = response.json()['total']
    assert total == 12
    Charles = response.json()['data'][4]['first_name']
    assert response.json()['data'][4]['first_name'] == 'Charles'
    print(total)
    print(Charles)