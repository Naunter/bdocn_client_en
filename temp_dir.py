# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from tempfile import mkdtemp
from time_template import time_template

def temp_loc_dir():
    time_template()
    print("temp_dir.py >>> temp_loc_dir()")
    dir = mkdtemp(prefix='loc_temp_')
    print("temp_dir.py >>> temp_loc_dir() >>> dir: "+str(dir))
    return dir