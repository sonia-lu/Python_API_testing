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
    print(request)
    assert status == 200
    print(request.content)

    # Assert if parameter is required.
    json_request = json.loads(request.text)
    required_par = jsonpath.jsonpath(json_request, f'required')
    assert required_par is False

    # # Assert if parameter is required for product.
    # required_par_prod = jsonpath.jsonpath(json_request, f'requiredForProduct')
    # assert required_par_prod[0] is False

    # # Assert if user can add custom parameter.
    # custom_param = jsonpath.jsonpath(json_request, f'customValuesEnabled')
    # assert custom_param[0] is True


def _get_category_request(test):
    api_url = 'https://api.allegro.pl/sale/categories' + test
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJhbGxlZ3JvOmFwaTpvcmRlcnM6cmVhZCIsImFsbGVncm86YXBpOnByb2ZpbGU6d3JpdGUiLCJhbGxlZ3JvOmFwaTpzYWxlOm9mZmVyczp3cml0ZSIsImFsbGVncm86YXBpOmJpbGxpbmc6cmVhZCIsImFsbGVncm86YXBpOmNhbXBhaWducyIsImFsbGVncm86YXBpOmRpc3B1dGVzIiwiYWxsZWdybzphcGk6c2FsZTpvZmZlcnM6cmVhZCIsImFsbGVncm86YXBpOmJpZHMiLCJhbGxlZ3JvOmFwaTpvcmRlcnM6d3JpdGUiLCJhbGxlZ3JvOmFwaTphZHMiLCJhbGxlZ3JvOmFwaTpwYXltZW50czp3cml0ZSIsImFsbGVncm86YXBpOnNhbGU6c2V0dGluZ3M6d3JpdGUiLCJhbGxlZ3JvOmFwaTpwcm9maWxlOnJlYWQiLCJhbGxlZ3JvOmFwaTpyYXRpbmdzIiwiYWxsZWdybzphcGk6c2FsZTpzZXR0aW5nczpyZWFkIiwiYWxsZWdybzphcGk6cGF5bWVudHM6cmVhZCIsImFsbGVncm86YXBpOm1lc3NhZ2luZyJdLCJhbGxlZ3JvX2FwaSI6dHJ1ZSwiZXhwIjoxNjMxMzk5MzEzLCJqdGkiOiJiMjNjZDQyMC1hYWIwLTRmZjctOTZjNS1lMTZlY2EwNzhkMTUiLCJjbGllbnRfaWQiOiJiZGZkNGExMmQwODU0YTg1YTBmMWQ5YWIxNjNmODFjNiJ9.BAcGqGB9H3Nr_1hpB_s2sJxBP7oQbRF7bjhH9BPIagU4OGKV90zjN3ki8v1Y2wH6lYC6c0ydtQdnKN3bC86Fkrz20V-BZGySu_zazgm86Xt-pGOB3-QFajdOT32saAAAQCx3AMsU97Hy6Qz2h-HI2U4xB9tdMHTeoBa_3fnx47SEW8NPk1xjWencBqtb5ZCwERW2qpnbsGUT0Ce6PQNpwMdoVkgKPdj-zqDuMogAOg-Uys0mCmUZTqro098GB24IbvgqPdr9uyNpfxGM5mboINw5x476gxT4TzUnvZKo4WeCgK0pn7shH7Acj910nC7D-VT7VPGP1VZUXndo637rug'

    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.allegro.public.v1+json"}
    ch = requests.get(api_url, data='', headers=headers)
    return ch

