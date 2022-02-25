import getpass as gp
from unittest import result
import requests
import json


class Api(__password=None,__username=None,__url=None, __token=None):
    """
    Classe d'interaction avec l'API de Ecoledirecte
    Les fonctions sont les suivantes :
    - gettoken() : Récupère le token d'authentification
    - getinfos() : Récupère les informations de l'utilisateur
    - getcours() : Récupère les cours de l'utilisateur
    - getnotes() : Récupère les notes de l'utilisateur
    - getabsences() : Récupère les absences de l'utilisateur
    - __init__() : Constructeur de la classe
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
    
    def getinfos(self):
        url = "https://api.ecoledirecte.com/v3/login.awp"
        headers = {}
        payload = "data={\n\t\"identifiant\": \"" + self.__mail + "\",\n\t\"motdepasse\": \"" + self.__password + "\"\n}"
        result = requests.request("POST", url, headers, data=payload)
        print("Etat de la requête : {}".format(result.status_code))
        return json.load(result.raw)

def newaccount(db: list):
    swap = Api()
    db += swap


DB = []
newaccount(DB)