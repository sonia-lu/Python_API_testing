import requests as re
import base64
import json

URL = "https://allegro.pl/auth/oauth/token"
CLIENT_ID = ''  # here insert your client_id
CLIENT_SECRET = ''  # here instert your client_secret

client_string = CLIENT_ID + ":" + CLIENT_SECRET
client_string_bytes = client_string.encode("ascii")

authorization = base64.b64encode(client_string_bytes)
authorization = authorization.decode('ascii')

headers = {"Authorization": f"Basic {authorization}", "Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials"}

result = re.post(url=URL, data=data, headers=headers)

if result.status_code != 200:
    print("Error - could not get token")
    print(f"{result.status_code} - {result.text}")
else:
    with open("config.json", "w") as config_file:
        config_file.write(result.text)