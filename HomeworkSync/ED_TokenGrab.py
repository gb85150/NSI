import requests as r
import json, LoginPrompt
class UserAccounts:
    """Classe regroupant toutes les informations nécessaires à la création d'un compte utilisateur"""
    def __init__(self, token = None):
        if token == None:
            username, password = LoginPrompt.login()
            self.__token = self.connectAPI(username, password)
        else:
            self.__token = token

    def connectAPI(self, username, password):
        """Connexion à l'API d'EcoleDirecte"""
        url = "https://api.ecoledirecte.com/v3/login.awp"
        username = "\"" + username + "\""
        password = "\"" + password + "\""
        data = "data={\"identifiant\": "+username+",\"motdepasse\": "+password+"}"
        response = r.get(url, data)
        print(response.status_code)
        self.data = {}
        self.data = json.loads(response.text)
        return json.loads(response.text)["token"]
    
    def getToken(self):
        """Renvoie le token de l'utilisateur"""
        return self.__token
    def __print__(self):
        print(self.data)
    

def bckup(user):
    """Fonction de sauvegarde de la classe UserAccounts"""
    with open("UserAccounts.json", "w") as f:
        json.dump(user.__dict__, f)

if __name__ == "__main__":
    user = UserAccounts()
    bckup(user)
    print(user)
    
    
