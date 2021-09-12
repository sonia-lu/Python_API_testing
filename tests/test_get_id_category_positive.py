import requests
import json
import jsonpath


"""
This Test Case is responsible for positive scenarios of acceptance testing for Get a category by ID
"""


# Testing parent ID (int) if has leaf=False; name!=null; parent=None
def test_parent_categories_id_int_positive():
    _assert_parent_ID('/11763')


# Testing parent ID (UUID) if has leaf=False; name!=null; parent=None
def test_parent_categories_id_UUID_positive():
    _assert_parent_ID('/42540aec-367a-4e5e-b411-17c09b08e41f')


# Testing if first child of a parent has leaf=False; name!=null; parent!=None
def test_first_child_categories_id_positive():
    # Assert if ID exists
    request = _get_category_request('?parent.id=5')
    status = request.status_code
    assert status == 200

    # Assert if user can create offer on higher level category.
    json_request = json.loads(request.text)
    leaf = jsonpath.jsonpath(json_request, f'categories[0].leaf')
    assert leaf[0] is False

    # Assert if name is not null.
    name = jsonpath.jsonpath(json_request, f'categories[0].name')
    assert name[0] is not None or name != ''

    # Assert if parent category does not has parent ID.
    parent = jsonpath.jsonpath(json_request, f'categories[0].parent')
    assert parent[0] is not None


# Testing if lowest child of a parent has leaf=True; name!=null; parent!=None
def test_lowest_child_categories_id_positive():
    # Assert if ID exists
    request = _get_category_request('/315261')
    status = request.status_code
    assert status == 200

    # Assert if user can create offer on lower level category.
    json_request = json.loads(request.text)
    leaf = jsonpath.jsonpath(json_request, f'leaf')
    assert leaf[0] is True

    # Assert if name is not null.
    name = jsonpath.jsonpath(json_request, f'name')
    assert name[0] is not None or name != ''

    # Assert if parent category does not has parent ID.
    parent = jsonpath.jsonpath(json_request, f'parent')
    assert parent[0] is not None


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


def _assert_parent_ID(parent_id):
    request = _get_category_request(parent_id)
    status = request.status_code
    assert status == 200

    # Assert if user can create offer on parent category.
    json_request = json.loads(request.text)
    leaf = jsonpath.jsonpath(json_request, f'leaf')
    assert leaf[0] is False

    # Assert if name is not null.
    name = jsonpath.jsonpath(json_request, f'name')
    assert name[0] is not None or name != ''

    # Assert if parent category does not has parent ID.
    parent = jsonpath.jsonpath(json_request, f'parent')
    assert parent[0] is None

