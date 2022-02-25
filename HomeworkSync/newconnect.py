import getpass as gp
import requests
import json


class Api():
    """

    """

    def __init__(self):
        """

        """
        print("Launching... Please wait !")
        if self.__password or self.__mail:
            self.__mail = input("Email ? :")
            self.__password = gp.getpass(prompt="Password ? :")
            print("Ready")

    def gettoken(self):
        url = "https://api.ecoledirecte.com/v3/login.awp"
        headers = {}
        payload = "data={\n\t\"identifiant\": \"" + self.__mail + "\",\n\t\"motdepasse\": \"" + self.__password + "\"\n}"
        result = requests.request("POST", url, headers, data=payload)
        print(result.status_code)
        return json.load(result)

def newaccount(db: list):
    swap = Api()
    db += swap


DB = []
newaccount(DB)
