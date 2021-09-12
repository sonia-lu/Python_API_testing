import requests
import json
import jsonpath

"""
This Test Case is responsible for positive scenarios of acceptance testing for Get parameters supported by a category
"""


# Testing if first child of a parent has leaf=False; name!=null; parent!=None
def test_required_parameter():
    # Assert if ID exists
    request = _get_category_request('/315261/parameters')
    status = request.status_code
    assert status == 200
    # print(request.content)

    # Assert parameters required, requiredForProduct, type has default type of data
    json_request = json.loads(request.text)
    parameters = jsonpath.jsonpath(json_request, f'parameters')[0]

    for parameter in parameters:
        assert parameter['required'] is False or True
        assert parameter['requiredForProduct'] is False or True
        assert parameter['type'] is 'integer' or 'float' or 'string' or 'dictionary'


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

