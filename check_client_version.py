# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from urllib.request import build_opener,install_opener,urlopen
from socket import timeout

from time_template import time_template

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

def get_version():
    time_template()
    print("check_client_version.py >>> def check_version()")

    url = 'https://github.com/Naunter/bdocn_client_en/raw/main/CHECK/CLIENT_VERSION'
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        a = urlopen(url, timeout=5)
    except:
        print("check_client_version.py >>> def check_version(): something wrong, maybe timeout")
        version = False
    else:
        version = a.read().decode('utf-8').strip()
    return version
