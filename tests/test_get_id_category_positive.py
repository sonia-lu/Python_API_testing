import requests
import json
import jsonpath


"""
This Test Case is responsible for positive scenarios of acceptance testing for Get a category by ID
"""


# Testing parent ID (int) if has leaf=False; name!=null; parent=None
def test_parent_categories_id_int():
    _assert_parent_ID('/11763')


# Testing parent ID (UUID) if has leaf=False; name!=null; parent=None
def test_parent_categories_id_UUID():
    _assert_parent_ID('/42540aec-367a-4e5e-b411-17c09b08e41f')


# Testing if first child of a parent has leaf=False; name!=null; parent!=None
def test_first_child_categories_id():
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
def test_lowest_child_categories_id():
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
    api_url = 'https://api.allegro.pl/sale/categories' + test
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJhbGxlZ3JvOmFwaTpvcmRlcnM6cmVhZCIsImFsbGVncm86YXBpOnByb2ZpbGU6d3JpdGUiLCJhbGxlZ3JvOmFwaTpzYWxlOm9mZmVyczp3cml0ZSIsImFsbGVncm86YXBpOmJpbGxpbmc6cmVhZCIsImFsbGVncm86YXBpOmNhbXBhaWducyIsImFsbGVncm86YXBpOmRpc3B1dGVzIiwiYWxsZWdybzphcGk6c2FsZTpvZmZlcnM6cmVhZCIsImFsbGVncm86YXBpOmJpZHMiLCJhbGxlZ3JvOmFwaTpvcmRlcnM6d3JpdGUiLCJhbGxlZ3JvOmFwaTphZHMiLCJhbGxlZ3JvOmFwaTpwYXltZW50czp3cml0ZSIsImFsbGVncm86YXBpOnNhbGU6c2V0dGluZ3M6d3JpdGUiLCJhbGxlZ3JvOmFwaTpwcm9maWxlOnJlYWQiLCJhbGxlZ3JvOmFwaTpyYXRpbmdzIiwiYWxsZWdybzphcGk6c2FsZTpzZXR0aW5nczpyZWFkIiwiYWxsZWdybzphcGk6cGF5bWVudHM6cmVhZCIsImFsbGVncm86YXBpOm1lc3NhZ2luZyJdLCJhbGxlZ3JvX2FwaSI6dHJ1ZSwiZXhwIjoxNjMxMzk5MzEzLCJqdGkiOiJiMjNjZDQyMC1hYWIwLTRmZjctOTZjNS1lMTZlY2EwNzhkMTUiLCJjbGllbnRfaWQiOiJiZGZkNGExMmQwODU0YTg1YTBmMWQ5YWIxNjNmODFjNiJ9.BAcGqGB9H3Nr_1hpB_s2sJxBP7oQbRF7bjhH9BPIagU4OGKV90zjN3ki8v1Y2wH6lYC6c0ydtQdnKN3bC86Fkrz20V-BZGySu_zazgm86Xt-pGOB3-QFajdOT32saAAAQCx3AMsU97Hy6Qz2h-HI2U4xB9tdMHTeoBa_3fnx47SEW8NPk1xjWencBqtb5ZCwERW2qpnbsGUT0Ce6PQNpwMdoVkgKPdj-zqDuMogAOg-Uys0mCmUZTqro098GB24IbvgqPdr9uyNpfxGM5mboINw5x476gxT4TzUnvZKo4WeCgK0pn7shH7Acj910nC7D-VT7VPGP1VZUXndo637rug'

    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.allegro.public.v1+json"}
    ch = requests.get(api_url, data='', headers=headers)
    return ch


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

