import requests,re,json
from bs4 import BeautifulSoup as parser
res = requests.Session()
from facebook_scrapping import cookies_login as colog
from facebook_scrapping import facebook_upload as faceup

from datetime import datetime 

y = datetime.now().year
m = datetime.now().month
d = datetime.now().day 
h = datetime.now().hour
n = datetime.now().minute
s = datetime.now().second

time_now = f'{y}:{m}:{d}:{h}:{n}:{s}'
# print(time_now)

def login_cookies_facebook():
    COOKIES = input(
        '(?) Facebook Cookies: '
        )

    open('./storage/cookies.txt','w').write(colog.login(COOKIES))

def menu_upload(cookie=open('./storage/cookies.txt','r').read()):
    try:
        if 'mbasic_logout_button' in res.get('https://free.facebook.com/',headers={'cookie': cookie}).text:
            pass
        else:
            login_cookies_facebook()
    except:
        pass

    print('\n\t\t------------[Facebook Upload]------------')
    CAPTION = input(
            '\n(?) Caption Post: '
            )
    if faceup.upload(CAPTION,cookie,time_now):
        print('[✓] Succes Upload')
    else:
        print('[×] Wrong Upload')



if __name__ == '__main__':
    menu_upload()
