import requests
import json


class EXMO_API():
    def __init__(self):
        self.data = 0
        self.pair = 0

    def get_pair_data(self, pair='BTC_USD'):
        url = "https://api.exmo.com/v1.1/ticker"

        payload = {}
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        self.data = response.json()[pair]
        self.pair = pair
