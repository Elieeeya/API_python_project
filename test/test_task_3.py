from conftest import *
from requests.auth import HTTPBasicAuth

url = 'http://users.bugred.ru/tasks/rest/'

headers = {
    'Content-Type': 'application/json, application/xml, form-data',
    'Accept': 'application/json'
}

params = [
    {'query': 'Лунатиков'}  # params[0]
]


# MagicSearch: проверяем наличие генерального в базе
def test_user_verification():
    response = requests.get(url + 'magicsearch', params=params[0])
    assert response.status_code == 230 or 232 or 235
    print(response.status_code)
