import requests

from newconnect import newaccount


def gethomework(TOKEN):
    url = """
    https://api.ecoledirecte.com/v3/Eleves/3868/cahierdetexte.awp?verbe=get
    """

    payload = "data={\n\t\"token\": \"" + TOKEN + "\"\n}"
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


# url = "https://api.ecoledirecte.com/v3/login.awp"
# payload="data={\n\t\"identifiant\": \"\",\n\t\"motdepasse\": \"PASSWORD\"\n}"
# headers = {}
# response = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)


def json_to_dict(json):
    return json.loads(json)

if __name__ == '__main__':
    TOKEN = newaccount()
    print(json_to_dict(gethomework(TOKEN)))
