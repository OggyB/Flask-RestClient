import requests
import client


class EndPoint():
    def __init__(self, token):
        self.base_url = 'https://sandbox-reporting.rpdpymnt.com/'
        self.token = token
        self.status = {"APPROVED", "WAITING", "DECLINED", "ERROR"}
        self.paymentMethod = {"CREDITCARD", "CUP", "IDEAL", "GIROPAY", "MISTERCASH", "STORED", "PAYTOCARD", "CEPBANK",
                              "CITADEL"}
        self.errorCode = {"Do not honor", "Invalid Transaction", "Invalid Card", "Not sufficient funds",
                          "Incorrect PIN", "Invalid country association", "Currency not allowed",
                          "3-D Secure Transport Error", "Transaction not permitted to cardholder"}
        self.filterField = {"Transaction UUID", "Customer Email", "Reference No", "Custom Data", "Card PAN"}

    def getTransactionsReport(self, fromDate, toDate):
        url = self.base_url + 'api/v3/transactions/report'

        payload = {
            'fromDate': fromDate,
            'toDate': toDate
        }

        files = [

        ]
        header = {
            'Authorization': self.token

        }

        response = requests.post(url, headers=header, data=payload)
        data = response.json()
        if (response.status_code == 401):
            return 'Expired'
        else:
            return data

    def getTransactionQuery(self, fromDate, toDate):
        url = self.base_url + 'api/v3/transaction/list'

        payload = {
            'fromDate': fromDate,
            'toDate': toDate
        }

        files = [

        ]
        header = {
            'Authorization': self.token

        }

        response = requests.post(url, headers=header, data=payload)
        data = response.json()
        if (response.status_code == 401):
            return 'Expired'
        else:
            return data

    def getTransaction(self, TransactionId):
        url = self.base_url + 'api/v3/transaction'
        payload = "{\n\t\"transactionId\" : \"" + TransactionId + "\"\n}"
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        if (response.status_code == 401):
            return 'Expired'
        else:
            return data


    def getClient(self, transactionId):
        url = self.base_url + 'api/v3/client'
        payload = "{\n\t\"transactionId\" : \"" + transactionId + "\"\n}"
        headers = {
        'Authorization': self.token,
        'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        if (response.status_code == 401):
            return 'Expired'
        else:
            return data
