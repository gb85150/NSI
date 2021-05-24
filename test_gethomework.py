import requests


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
