# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from webbrowser import open_new
from time_template import time_template

def hyperlinks(var):
    time_template()
    print("hyperlinks.py >>> def hyperlinks(var): ")
    if var == 1 :
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        open_new(r"https://github.com/Naunter/bdocn_client_en")
    elif var == 2:
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        open_new(r"https://www.bilibili.com/video/BV1yf4y1s75B")