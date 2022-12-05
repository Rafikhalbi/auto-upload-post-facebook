import requests,re
from bs4 import BeautifulSoup as parser

res = requests.Session()

URL = 'https://free.facebook.com'


def upload(caption,cookie,time_now):
    message = f'''
    {caption}\n\npost from python time {time_now}
    '''
    # print(message)
    RESPONSE = res.get(
            URL+'/profile.php',headers={
                'cookie': cookie
                }
            ).text
    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',str(RESPONSE))[1]
    jazoest = re.search('name="jazoest" value="(.*?)"',str(RESPONSE))[1]
    privacyx = re.search('name="privacyx" value="(.*?)"',str(RESPONSE))[1]
    target = re.search('name="target" value="(.*?)"',str(RESPONSE))[1]
    
    post_url = parser(RESPONSE,'html.parser')
    for i in post_url.find_all('form'):
        s = i['action']
        if '/composer/mbasic/' in s:
            POSTURL = URL+i['action']

    data = {
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'privacyx': privacyx,
            'r2a': '1',
            'xhpc_timeline': '1',
            'target': target,
            'c_src': 'timeline_self',
            'cwevent': 'composer_entry',
            'referrer': 'timeline',
            'ctype': 'inline',
            'cver': 'amber',
            'rst_icv': '',
            'xc_message': message,
            'view_post': 'Posting'
            }
    try:
        POSTING = res.post(
                POSTURL,data=data,headers={'cookie': cookie}
                )
        return True
    except:
        return False
