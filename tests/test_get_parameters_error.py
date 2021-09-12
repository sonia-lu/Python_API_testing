import requests
import json
import jsonpath
"""
This Test Case is responsible for negative scenarios of acceptance testing for Get parameters supported by a category
"""


# Testing if first child of a parent has leaf=False; name!=null; parent!=None
def test_required_parameter():
    # Assert if ID exists
    request = _get_category_request('/abc/parameters')
    status = request.status_code
    assert status == 404
    print(request.content)


def _get_category_request(test):
    token = __get_token()
    api_url = 'https://api.allegro.pl/sale/categories' + test
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.allegro.public.v1+json"}
    ch = requests.get(api_url, data='', headers=headers)
    return ch


def __get_token():
    with open('config.json', 'r') as j:
        json_data = json.load(j)
        token = json_data['access_token']
        return token


