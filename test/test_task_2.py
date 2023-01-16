from conftest import *
from requests.auth import HTTPBasicAuth

url = 'https://testbase.atlassian.net/rest/api/3/issue/TEST-18485/comment'

user = 'mail.for.testbase@gmail.com'
password = 'AUaP65O4PnLFjoKqslJkCF9B'

body = {
    "body":
        {
            "version": 1,
            "type": "doc",
            "content":
                [
                    {"type": "paragraph",
                     "content":
                         [
                             {"type": "text",
                              "text": "Тест комент121"
                              }
                         ]
                     }
                ]
        },
    "visibility": None
}


def test_add_comment_jira():
    response = requests.post(url, auth=HTTPBasicAuth(user, password), json=body)
    # JIRA: тестируем статус код после создания комментария
    assert response.status_code == 201
    #  JIRA: проверим заголовок Content-Type
    assert response.headers == {'Content-Type': 'application/json;charset=UTF-8'}
