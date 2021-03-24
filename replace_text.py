# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from re import sub,M

from time_template import time_template

def change_res_id(path):
    time_template()
    print("replace_text.py >>> def change_res_id(path)")

    with open(path, 'r+') as f:
        content = f.read()
        new_content = sub(r"(RES=.*)", r"RES=_PT_", content, flags = M)
        f.seek(0)
        f.write(new_content)
        f.truncate()