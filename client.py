import requests

class User():
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password
        self.token = ""

    def getUserName(self):
        return self.userName

    def getToken(self):
        url = "https://sandbox-reporting.rpdpymnt.com/api/v3/merchant/user/login"

        payload = {'email': self.userName,
                   'password': self.password}
        files = [

        ]
        headers = {
            'Content-Type': 'multipart/form-data; boundary=--------------------------023968074109650296261902'
        }

        response = requests.post( url, data=payload)
        if(str(response.status_code) == '200'):

            data = response.json()
            return data["token"]
        else:
            return False

    def ıs_auth(self, token):

        url = "https://sandbox-reporting.rpdpymnt.com/api/v3/transaction/list"

        payload = "{\n\t\n}"
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        response = requests.post(url, data=payload,headers=headers)
        data = response.json()

        if response.status_code == 401:
            return False
        else:
            return True










