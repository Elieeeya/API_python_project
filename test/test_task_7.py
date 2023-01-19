from conftest import *

url = 'http://users.bugred.ru/tasks/rest/'

params = [
    {'company_name': 'Алкоголики и тунеядцы, тунеядцы и алкоголики'},
    {'company_type': 'ООО'},
    {'company_users': ['test_anna@gmail.com', 'mrak20@list.ru']},
    {'email_owner': 'aa2320991@mail.com'}
]



def test_create_company():
    response = requests.get(url + 'createcompany', params=params[0])
    assert response.status_code == 200
    print(response.text)


params_user = [
    {'email': 'test_cu_612121@mail.com'},
    {'name': 'Алкоголик'},
    {'tasks': [9]},
    {'companies': [18]}
]


def test_create_user():
    response = requests.get(url + 'createuser', params=params_user[0])
    assert response.status_code == 200
    print(response.text)


