import token

import requests
import json

"""
This Test Case is responsible for negative scenarios of acceptance testing for Get a category by ID
"""


#  Testing if ID accept any string value as the category ID.
def test_parent_categories_id_error():
    request = _get_category_request('/abc')
    status = request.status_code
    assert status == 404


#   Testing if ID of child accept any string value as the category ID
def test_first_child_categories_id_error():
    request = _get_category_request('?parent.id=eyJzY29wZSI6WyJhbGxlZ3JvOmFwaTpvcmRlcnM6cmVhZCIsImFsbGVncm86YXBpOnByb')
    status = request.status_code
    assert status == 404


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

