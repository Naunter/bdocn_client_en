# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from threading import Thread
from time_template import time_template

def thread_it(func, *args):
    time_template()
    print("thread_function.py >>> def thread_it(func, *args)")

    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()