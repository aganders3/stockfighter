import requests

def api_status():
    # Check that the API is up
    r = requests.get('https://api.stockfighter.io/ob/api/heartbeat')
    r_dict = r.json()

    return (r_dict['ok'], r_dict)
