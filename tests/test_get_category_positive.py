import requests
import json
import jsonpath


"""
This Test Case is responsible for positive scenarios of acceptance testing for Get IDs of Allegro categories
"""


# Testing parent ID (int) if has leaf=False; name!=null; parent=None
def test_parent_categories_id_int():
    # Assert request is returned
    request = _get_category_request('')
    json_request = json.loads(request.text)
    categories = jsonpath.jsonpath(json_request, f'categories')[0]
    print(categories)
    status = request.status_code
    assert status == 200

    # Assert if ID is omitted, the list of main Allegro categories will be returned.
    for category in categories:
       assert category['parent'] is None
       assert category['leaf'] is False
       assert category['name'] is not 'null'


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

