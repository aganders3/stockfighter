import requests
from .api_key import auth_header

class Stock():
    def __init__(self, ticker, venue, account=None):
        self._url = "https://api.stockfighter.io/ob/api/"
        self.ticker = ticker
        self.venue = venue
        self.account = account

    def get_quote(self):
        pass

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

    def order(self, account, venue, stock, price, qty, direction, order_type):
        """Place an order by specifying all aspects"""
        url = self._url + '/venues/{}/stocks/{}/orders'.format(venue, stock)
        order = {'account' : account,
                 'venue' : venue,
                 'stock' : stock,
                 'price' : price,
                 'qty' : qty,
                 'direction' : direction,
                 'order_type' : order_type}
        r = requests.post(url, data=order, headers=auth_header)
        return r.json()
