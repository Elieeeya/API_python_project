from conftest import *
from requests.auth import HTTPBasicAuth


# JIRA: тестируем статус код после создания комментария

url = 'https://testbase.atlassian.net/rest/api/3/issue/TEST-18485/comment'

user = '*****'
password = '*****'

body = {
    "body":
        {
            "version":1,
            "type":"doc",
            "content":
                [
                    {"type":"paragraph",
                     "content":
                         [
                             {"type":"text",
                              "text":"Тест комент"
                              }
                         ]
                     }
                ]
        },
    "visibility":None
}


def test_add_comment_jira():
    response = requests.post(url, auth=HTTPBasicAuth(user, password), json=body)

    assert response.status_code == 201


