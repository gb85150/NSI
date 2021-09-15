import getpass
import json
import requests


def GetToken():
    data = login()
    token = data["token"]
    return token


def login():
    Email = str(input("Email adress ? : "))
    Password = str(getpass.getpass(prompt="Password ? : "))
    url = "https://api.ecoledirecte.com/v3/login.awp"

    payload = "data={\n\t\"identifiant\": \"" + Email + "\",\n\t\"motdepasse\": \"" + Password + "\"\n}"
    headers = {}
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)["token"]
    print(data)
    return data


print(GetToken())
