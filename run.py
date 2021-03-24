# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

import tkinter as tk
from tkinter.messagebox import askyesno,showinfo
from subprocess import run

from time_template import time_template
from thread_function import thread_it
from hyperlinks import hyperlinks
import check_client_version
import save_bdocn_conf
import select_bdo_game_dir
import ui4

root = tk.Tk()
root.title('BDO Language Replace by Naunter')
root.resizable(False, False)
app = ui4.Application(root)

time_template()
print("run.py >>>")

if save_bdocn_conf.check_save_bdo_gamepath() != False:
    selected_dir = save_bdocn_conf.check_save_bdo_gamepath()
    print("run.py >>> def select_game_path(self) >>> if selected_dir: "+str(selected_dir))
    app.insert_save_path_entry(selected_dir)

ask_run_bdo = askyesno('Notice', 'Do you want to run BDO on Steam')
if ask_run_bdo == True:
    run("cmd /c start steam://run/582660")
    showinfo('Notice', 'Please wait for the BDO launcher complete the update before you replace the language file!')
else:
    showinfo('Notice', 'Please run the BDO launcher and wait for it complete the update before you replace the language file!')

check = check_client_version.get_version()
if check != '2021032300' or check is False:
    print("run.py >>> check_client_version.get_version() is True")
    a = askyesno('Notice', 'New tool update, check it?')
    if a == True:
        hyperlinks(1)
        thread_it(app.run(), '')
    else:
        thread_it(app.run(), '')
else:
    thread_it(app.run(), '')

