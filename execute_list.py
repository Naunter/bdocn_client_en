# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from time_template import time_template
from pathlib import Path
user_home = str(Path.home())
from shutil import copy2

import download
import check_hash
import select_bdo_game_dir

def hm1(dir):
    time_template()
    print("execute_list.py >>> def hm1(dir)")

    tofilename = r'languagedata_pt.loc'

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/' + tofilename

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client_en/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client_en/languagedata_en.loc'

    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_github_loc_en_sea_hash()
        if local_loc_hash != online_loc_hash:
            download.download_loc_en(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def hm1(dir): can not find: " +str(loc_path))
        download.download_loc_en(loc_dir)
        copy2(loc_path,loc_ads_path)

def hm2(dir):
    time_template()
    print("execute_list.py >>> def hm2(dir)")

    tofilename = r'languagedata_tw.loc'

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/' + tofilename

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client_en/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client_en/languagedata_en.loc'

    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_github_loc_en_sea_hash()
        if local_loc_hash != online_loc_hash:
            download.download_loc_en(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def hm1(dir): can not find: " +str(loc_path))
        download.download_loc_en(loc_dir)
        copy2(loc_path,loc_ads_path)

def hm3(dir):
    time_template()
    print("execute_list.py >>> def hm3(dir)")

    tofilename = r'languagedata_id.loc'

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/' + tofilename

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client_en/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client_en/languagedata_en.loc'

    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_github_loc_en_sea_hash()
        if local_loc_hash != online_loc_hash:
            download.download_loc_en(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def hm1(dir): can not find: " +str(loc_path))
        download.download_loc_en(loc_dir)
        copy2(loc_path,loc_ads_path)