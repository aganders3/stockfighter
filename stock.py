import requests
import json
from .api_key import auth_header

class Stock():
    def __init__(self, ticker, venue, account=None):
        self._url = "https://api.stockfighter.io/ob/api/"
        self.ticker = ticker
        self.venue = venue
        self.account = account

    def book(self):
        url = (self._url
               + 'venues/{}/'.format(self.venue)
               + 'stocks/{}'.format(self.ticker))
        r = requests.get(url, headers=auth_header)
        r_dict = r.json()
        return (r_dict['bids'], r_dict['asks'], r_dict['ts'])

    def quote(self):
        url = (self._url
               + 'venues/{}/'.format(self.venue)
               + 'stocks/{}/quote'.format(self.ticker))
        r = requests.get(url, headers=auth_header)
        r_dict = r.json()
        try:
            return (r_dict['ask'], r_dict)
        except KeyError:
            return (None, r_dict)

    def buy(self, quantity, account=None, order_type='market', price=0):
        if account is None and self.account is not None:
            account = self.account
        elif account is None and self.account is None:
            raise ValueError("No account specified")

        if order_type is 'market':
            price = 0
        elif price == 0:
            raise ValueError("Price must be > $0 for a non-market order.")

        return self.order(account, self.venue, self.ticker, price,
                          quantity, 'buy', order_type)

    def sell(self, quanityt, account=None, order_type='market', price=0):
        if account is None and self.account is not None:
            account = self.account
        elif account is None and self.account is None:
            raise ValueError("No account specified")

        if order_type is 'market':
            price = 0
        elif price == 0:
            raise ValueError("Price must be > $0 for a non-market order.")

        return self.order(account, self.venue, self.ticker, price,
                          quantity, 'sell', order_type)

    def order_status(self, order_id):
        url = (self._url
               + 'venues/{}/'.format(self.venue)
               + 'stocks/{}/'.format(self.ticker)
               + 'orders/{}'.format(order_id))
        r = requests.get(url, headers=auth_header)
        return (r.json()['open'], r.json())

    def cancel(self, order_id):
        url = (self._url
               + 'venues/{}/'.format(self.venue)
               + 'stocks/{}/'.format(self.ticker)
               + 'orders/{}'.format(order_id))
        r = requests.delete(url, headers=auth_header)
        return (r.json()['open'], r.json())

    def order(self, account, venue, stock, price, qty, direction, order_type):
        """Place an order by specifying all aspects"""
        url = self._url + '/venues/{}/stocks/{}/orders'.format(venue, stock)
        order = {'account' : account,
                 'venue' : venue,
                 'stock' : stock,
                 'price' : price,
                 'qty' : qty,
                 'direction' : direction,
                 'orderType' : order_type}
        print(order)
        r = requests.post(url, json=order, headers=auth_header)
        r_dict = r.json()
        if r_dict['ok']:
            return (r_dict['id'], r_dict)
        else:
            return (None, r_dict)
