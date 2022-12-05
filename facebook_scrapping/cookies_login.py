import requests

res = requests.Session()

URL = 'https://free.facebook.com/'

def login(cookie):
    # cookie = {'cookie': cookie}
    RESPONSE = res.get(
            URL,headers = {'cookie': cookie}
            )
    if 'mbasic_logout_button' in RESPONSE.text:
        return cookie
    else:
        exit('\n(!) Invalid Facebook Cookies')
        return False
