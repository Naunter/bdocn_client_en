# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from tkinter.messagebox import showwarning
from tkinter.filedialog import askdirectory
from pathlib import Path

from time_template import time_template
from save_bdocn_conf import check_save_bdo_gamepath

def select_dir():
    time_template()
    print("select_bdo_game_dir.py >>> def select_dir()")

    if check_save_bdo_gamepath() != False:
        path = check_save_bdo_gamepath()
    else:
        path = r'/'

    selected_dir = askdirectory(title="Please select the BDO root directory", initialdir = path)
    print("select_bdo_game_dir.py >>> def select_dir() >>> select_dir: " + str(selected_dir))

    return selected_dir

def check_bdo_loc_dir(dir):
    time_template()
    print("select_bdo_game_dir.py >>> def check_bdo_loc_dir()")

    bdo_dir = dir
    bdo_dir_ads = bdo_dir + r'/ads'
    print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> bdo_dir: "+str(bdo_dir))
    print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> bdo_dir_ads: "+str(bdo_dir_ads))

    if bdo_dir == '':
        print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> if bdo_dir == " + str(bdo_dir))
        showwarning("Warning","The directory is empty, please re-select! \n\ne.g.: " + r"C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online")
        return False
    elif Path(bdo_dir_ads).is_dir() is False:
        print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> Path(bdo_dir_ads).is_dir() is: " + str(Path(bdo_dir_ads).is_dir()))
        showwarning("Warning","Can't find the ads folder，please verify the integrity of the game files! \n\n:e.g. " + r"C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online\ads")
        return False
    else:
        print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> return bdo_dir_ads: "+str(bdo_dir_ads))
        return bdo_dir_ads

def output_selected_bdo_game_dir(dir):
    time_template()
    print("select_bdo_game_dir.py >>> def output_selected_bdo_game_dir()")

    if check_bdo_loc_dir(dir) != False:
        #create_bdo_font_dir(dir)
        return dir
    else:
        return False
