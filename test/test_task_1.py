#1. MagicSearch: проверяем статус коды

from conftest import *

url = 'http://users.bugred.ru/tasks/rest/'

headers = {
    'Content-Type': 'application/json, application/xml, form-data',
    'Accept': 'application/json'
}


params = [
    {'query': 'lolosha'},  # params[0]
    {'query': 'Красавчик', 'partyType': 'USER'},  # params[1]
    {'query': 'Ivan', 'partyType': 'USER'},  # params[2]
    {'query': 'ОАО Петушки', 'partyType': 'COMPANY'},  # params[3]
    {'query': 'Ромашк', 'partyType': 'COMPANY'},  # params[4]
    {'query': 'Алкоголики и тунеядцы'},  # params[5]
    {},  # params[6]
    {'query': ''},  # params[7]
    {'query': 'ОАО Петушки', 'partyType': 'COMP'},  # params[8]
    {'query': 'ОАО Петушки', 'taskStatus': 'NOACTUAL'},  # params[9]
    {'query': 'ОАО Петушки', 'include': 'NOACTUAL'}  # params[10]

]


def test_MagicSearch_status_230():
    response = requests.get(url + 'magicsearch', params=params[0])
    assert response.status_code == 230


def test_MagicSearch_status_231():
    response = requests.get(url + 'magicsearch', params=params[1])
    assert response.status_code == 231


def test_MagicSearch_status_232():
    response = requests.get(url + 'magicsearch', params=params[2])
    assert response.status_code == 232


def test_MagicSearch_status_233():
    response = requests.get(url + 'magicsearch', params=params[3])
    assert response.status_code == 233


def test_MagicSearch_status_234():
    response = requests.get(url + 'magicsearch', params=params[4])
    assert response.status_code == 234


def test_MagicSearch_status_235():
    response = requests.get(url + 'magicsearch', params=params[5])
    assert response.status_code == 235


def test_MagicSearch_status_455():
    response = requests.get(url + 'magicsearch', params=params[6])
    assert response.status_code == 455


def test_MagicSearch_status_456():
    response = requests.get(url + 'magicsearch', params=params[7])
    assert response.status_code == 456


def test_MagicSearch_status_457():
    response = requests.get(url + 'magicsearch', params=params[8])
    assert response.status_code == 457


def test_MagicSearch_status_458():
    response = requests.get(url + 'magicsearch', params=params[9])
    assert response.status_code == 458

def test_MagicSearch_status_459():
    response = requests.get(url + 'magicsearch', params=params[10])
    assert response.status_code == 459

