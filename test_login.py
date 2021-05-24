import requests


def GetToken():
    Email = str(input("Email adress ? : "))
    Password = str(input("Password ? : "))
    url = "https://api.ecoledirecte.com/v3/login.awp"

    payload = "data={\n\t\"identifiant\": \"" + Email + "\",\n\t\"motdepasse\": \"" + Password + "\"\n}"
    headers = {}
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


print(GetToken())
