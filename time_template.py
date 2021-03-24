# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from time import strftime,localtime

def time_template():
    print("\n" + str(strftime("%Y-%m-%d %H:%M:%S", localtime())))