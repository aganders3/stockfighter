import requests
from .api_key import auth_header

class Venue():
    def __init__(self, symbol, name=None):
        self._url = "https://api.stockfighter.io/ob/api/"
        self.symbol = symbol
        self.name = name

    def status(self, timeout=5):
        url = self._url + '/venues/{}/heartbeat'.format(self.symbol)
        r = requests.get(url, headers=auth_header, timeout=timeout)
        return r.json()['ok']

    def stocks(self):
        url = self._url + '/venues/{}/stocks'.format(self.symbol)
        r = requests.get(url, headers=auth_header)
        if r.json()['ok']:
            return r.json()['symbols']
        else:
            return []
