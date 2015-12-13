import requests
from .api_key import auth_header

class SFLevelCreationError(Exception):
    """Raise this for any errors that occur when instantiating a level"""
    pass

class Level():
    def __init__(self, name, timeout=5):
        self._url = 'https://www.stockfighter.io/gm/'
        init_url = self._url+'levels/{}'.format(name)
        r = requests.post(init_url, headers=auth_header, timeout=timeout)
        r_dict = r.json()
        if not r_dict['ok']:
            raise SFLevelCreationError(r_dict['error'])
        else:
            self.name = name
            self.info = r_dict
            self.account = r_dict['account']
            self.instance_id = r_dict['instanceId']
            self.tickers = r_dict['tickers']
            self.venues = r_dict['venues']

    def restart(self):
        restart_url = self._url+'instances/{}/restart'.format(self.instance_id)
        r = requests.post(restart_url, headers=auth_header)
        return r.json()

    def stop(self):
        stop_url = self._url+'instances/{}/stop'.format(self.instance_id)
        r = requests.post(stop_url, headers=auth_header)
        return r.json()

    def resume(self):
        resume_url = self._url+'instances/{}/resume'.format(self.instance_id)
        r = requests.post(resume_url, headers=auth_header)
        return r.json()

    def status(self):
        status_url = self._url+'instances/{}'.format(self.instance_id)
        r = requests.post(status_url, headers=auth_header)
        return r.json()

    def time_left(self):
        """return the approximate remaining time before timeout (in seconds)"""
        r_dict = self.status()
        if r_dict['ok']:
            return 5 * (r_dict['details']['endOfTheWorldDay']
                        - r_dict['details']['tradingDay'])
        else:
            return -1

