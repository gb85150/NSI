import requests, json, getpass

mail = input("Email ? : ")
password = getpass.getpass("Password ? : ")

url = "https://api.ecoledirecte.com/v3/login.awp"
headers = {}
payload = "data={\n\t\"identifiant\": \"" + mail + "\",\n\t\"motdepasse\": \"" + password + "\"\n}"
result = requests.request("POST", url, headers=headers, data=payload)
print("Etat de la requête : {}".format(result.status_code))
# Save raw_json in a file
with open('raw_json.json', 'w') as outfile:
    outfile.write(str(result.raw))