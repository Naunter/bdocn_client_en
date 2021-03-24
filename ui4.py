# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

import tkinter as tk
from tkinter.messagebox import showinfo,askyesno
from pathlib import Path

from time_template import time_template
from hyperlinks import hyperlinks
from thread_function import thread_it
import save_bdocn_conf
import select_bdo_game_dir
import execute_list
import replace_text

class Application:
    def __init__(self, master=None):
        self.main_window = tk.Frame(master)
        self.main_window.config(background='#f2f2f2', height='450', width='600')
        self.main_window.pack(side='top')
        self.left_panel_body = tk.LabelFrame(self.main_window)
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_panel_body.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#ff8000', height='300', text='How to use')
        self.left_panel_body.config(width='200')
        self.left_panel_body.place(anchor='nw', height='370', width='290', x='0', y='0')
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', relief='flat')
        self.left_panel_body_text.config(state='disabled', width='50')
        client_notice = r'''1. Please run the BDO launcher and wait for it complete the update before you replace the language file!

2. Select the BDO root directory

3. Select your region code

4. Run the tool to replace language file to English

* Example for BDO root directory: 
C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online\

5. If you have any questions, please submit issues on Github

'''
        self.left_panel_body_text.configure(state='normal')
        self.left_panel_body_text.insert('0.0', client_notice)
        self.left_panel_body_text.configure(state='disabled')
        self.left_panel_body_text.place(anchor='nw', height='330', width='280', x='0', y='0')
        self.left_panel_bottom = tk.LabelFrame(self.main_window)
        self.left_panel_bottom.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {bold}', relief='groove')
        self.left_panel_bottom.config(text='Source', width='200')
        self.left_panel_bottom.place(anchor='nw', height='80', width='290', x='0', y='370')
        self.left_panel_bottom_text = tk.Text(self.left_panel_bottom)
        self.left_panel_bottom_text.config(background='#f2f2f2', font='{Microsoft YaHei} 8 {}', relief='flat')
        self.left_panel_bottom_text.config(state='disabled', width='50')
        _text_ = ''' Create by Naunter
 Version:    2021032300
 Date:   2021/03/23
'''
        self.left_panel_bottom_text.configure(state='normal')
        self.left_panel_bottom_text.insert('0.0', _text_)
        self.left_panel_bottom_text.configure(state='disabled')
        self.left_panel_bottom_text.place(anchor='nw', height='50', width='150', x='0', y='0')
        self.left_panel_bottom_button_1 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_1.config(text='Project Home')
        self.left_panel_bottom_button_1.place(anchor='nw', height='26', width='90', x='190', y='0')
        self.left_panel_bottom_button_1.configure(command=lambda :thread_it(self.hyperlinks(1)))
        self.left_panel_bottom_button_2 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_2.config(text='Video')
        self.left_panel_bottom_button_2.place(anchor='nw', height='26', width='90', x='190', y='30')
        self.left_panel_bottom_button_2.configure(command=lambda :thread_it(self.hyperlinks(2)))
        self.save_path = tk.LabelFrame(self.main_window)
        self.save_path.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#0000ff', height='200', relief='groove')
        self.save_path.config(text='1. Select BDO directory', width='200')
        self.save_path.place(anchor='nw', height='80', width='300', x='300', y='0')
        self.save_path_entry_label = tk.Label(self.save_path)
        self.save_path_entry_label.configure(text='Please select the BDO root directory:')
        self.save_path_entry_label.place(anchor='nw', height='15', x='3', y='3')
        self.save_path_entry = tk.Entry(self.save_path)
        self.save_path_entry.config(font='{Microsoft YaHei} 10 {}')
        self.save_path_entry_text = ''''''
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', self.save_path_entry_text)
        self.save_path_entry.place(anchor='nw', height='25', width='210', x='5', y='23')
        self.save_path_button = tk.Button(self.save_path)
        self.save_path_button.config(font='{Microsoft YaHei} 9 {}', text='Open...')
        self.save_path_button.configure(command=lambda :thread_it(self.select_bdo_game_dir))
        self.save_path_button.place(anchor='nw', height='30', width='70', x='220', y='20')
        self.hanhua_method = tk.LabelFrame(self.main_window)
        self.hanhua_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#008080', height='200', text='2. Select your BDO region code')
        self.hanhua_method.config(width='200')
        self.hanhua_method.place(anchor='nw', height='220', width='300', x='300', y='80')
        self.hmVar=tk.IntVar()
        self.hmVar.set(1)
        self.hanhua_method_radiobutton_1 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_1.config(font='{Microsoft YaHei} 10 {}', text='pt (languagedata_pt.loc)', variable=self.hmVar, value='1')
        self.hanhua_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.hanhua_method_radiobutton_2 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_2.config(font='{Microsoft YaHei} 10 {}', text='tw (languagedata_tw.loc)', variable=self.hmVar, value='2')
        self.hanhua_method_radiobutton_2.place(anchor='nw', x='0', y='30')
        self.hanhua_method_radiobutton_3 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_3.config(font='{Microsoft YaHei} 10 {}', text='id (languagedata_id.loc)', variable=self.hmVar, value='3')
        self.hanhua_method_radiobutton_3.place(anchor='nw', x='0', y='60')
        self.hanhua_method_radiobutton_4 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_4.config(font='{Microsoft YaHei} 10 {}', text='undefined 4', variable=self.hmVar, value='4', state='disabled')
        self.hanhua_method_radiobutton_4.place(anchor='nw', x='0', y='90')
        self.hanhua_method_radiobutton_5 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_5.config(font='{Microsoft YaHei} 10 {}', text='undefined 5', variable=self.hmVar, value='5', state='disabled')
        self.hanhua_method_radiobutton_5.place(anchor='nw', x='0', y='120')
        self.hanhua_method_radiobutton_6 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_6.config(font='{Microsoft YaHei} 10 {}', text='undefined 6', variable=self.hmVar, value='6', state='disabled')
        self.hanhua_method_radiobutton_6.place(anchor='nw', x='0', y='150')
        self.usefontVar = tk.StringVar(value='1')
        self.process_panel = tk.LabelFrame(self.main_window)
        self.process_panel.config(font='{Microsoft YaHei} 12 {bold}', foreground='#008000', height='200', text='3. Replace language to English', width='200')
        self.process_panel.place(anchor='nw', height='150', width='300', x='300', y='300')
        self.process_panel_button_1 = tk.Button(self.process_panel)
        self.process_panel_button_1.config(font='{Microsoft YaHei} 12 {bold}', background='#008000', foreground='white', text='RUN')
        self.process_panel_button_1.configure(command=lambda :thread_it(self.start_button))
        self.process_panel_button_1.place(anchor='nw', height='100', width='285', x='5', y='10')
 
        self.mainwindow = self.main_window

    def hyperlinks(self, var):
        time_template()
        print("ui4.py >>> def hyperlinks(self, var)")
        hyperlinks(var)

    def lock_start_button(self):
        self.process_panel_button_1.config(state='disabled')

    def unlock_start_button(self):
        self.process_panel_button_1.config(state='normal')

    def insert_save_path_entry(self, path):
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', path)
    
    def select_bdo_game_dir(self):
        time_template()
        print("ui4.py >>> def user_select_bdo_game_dir(self)")

        selected_dir = select_bdo_game_dir.select_dir()
        print("ui4.py >>> def select_bdo_game_dir(self) >>> selected_dir: "+str(selected_dir))
        self.insert_save_path_entry(selected_dir)

    def output_bdo_game_dir(self):
        time_template()
        print("ui4.py >>> def output_bdo_game_dir(self)")

        inserted_path = str(self.save_path_entry.get())
        print("ui4.py >>> def output_bdo_game_dir(self) >>> inserted_path:"+str(inserted_path))

        if select_bdo_game_dir.output_selected_bdo_game_dir(inserted_path) != False:
            print("ui4.py >>> def output_bdo_game_dir(self) >>> inserted_path != False")
            return inserted_path
        else:
            self.save_path_entry.delete('0', 'end')
            return False

    def start_button(self):
        time_template()
        print("ui4.py >>> def start_button(self)")

        hm = str(self.hmVar.get())

        print("ui4.py >>> def start_button(self):"+" hm: "+ hm)
        a = askyesno('Notice', 'Do you want to execute this task?')

        def bdo_game_dir():
            if a is True and self.output_bdo_game_dir() != False:
                bdo_game_dir = self.output_bdo_game_dir()
                print("bdo_game_dir: "+str(bdo_game_dir))
                return bdo_game_dir
            else: 
                return False

        if bdo_game_dir() != False:
            bdo_game_dir = str(bdo_game_dir())

            if hm == '1':
                print("ui4.py >>> def start_button(self):1")
                self.lock_start_button()
                execute_list.hm1(bdo_game_dir)
                self.unlock_start_button()
                showinfo('Notice','Replace completed!')
            elif hm == '2':
                print("ui4.py >>> def start_button(self):2")
                self.lock_start_button()
                execute_list.hm2(bdo_game_dir)
                self.unlock_start_button()
                showinfo('Notice','Replace completed!')
            elif hm == '3':
                print("ui4.py >>> def start_button(self):3")
                self.lock_start_button()
                execute_list.hm3(bdo_game_dir)
                self.unlock_start_button()
                showinfo('Notice','Replace completed!')
            elif hm == '4':
                print("ui4.py >>> def start_button(self):4")
                self.lock_start_button()
                execute_list.hm4(bdo_game_dir)
                self.unlock_start_button()
                showinfo('Notice','Replace completed!')
            elif hm == '5':
                print("ui4.py >>> def start_button(self):5")
                self.lock_start_button()
                execute_list.hm5(bdo_game_dir)
                self.unlock_start_button()
                showinfo('Notice','Replace completed!')
            elif hm == '6':
                print("ui4.py >>> def start_button(self):6")
                self.lock_start_button()
                execute_list.hm6(bdo_game_dir)
                self.unlock_start_button()
                showinfo('Notice','Replace completed!')
            else:
                pass

            if Path(save_bdocn_conf.create_bdocn_conf_dir()).is_dir() is True:
                print("ui4.py >>> Path(save_bdocn_conf.create_bdocn_conf_dir()).is_dir() is: " + str(save_bdocn_conf.create_bdocn_conf_dir))
                save_bdocn_conf.save_bdo_gamepath(bdo_game_dir)
            else:
                pass

    def run(self):
        time_template()
        print("ui4.py >>> def run(self)")
        self.mainwindow.mainloop()