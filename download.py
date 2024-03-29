# @Time    : 2021/03/23
# @Author  : Naunter
# @Page    : https://github.com/Naunter
# @Page    : https://github.com/Naunter/bdocn_client_en

from urllib.request import build_opener,install_opener,urlretrieve,urlopen
from re import findall
from socket import timeout
from tkinter.messagebox import showinfo

from time_template import time_template
import temp_dir

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

def download_file(url, todir, tofilename):
    time_template()
    print("download.py >>> download_file(url, todir, tofilename):" + " url: " + str(url) + " todir: " + str(todir) + " tofilename: " + str(tofilename))
    
    timeout(10)
    path = todir + r'/' + tofilename
    print("download.py >>> download_file(url, todir, tofilename): path: " + str(path))
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        urlretrieve(url, path)
    except:
        print("download.py >>> download_file(url, todir, tofilename) >>> something wrong, maybe timeout")
        showinfo('download_file()','Downloading Timeout，Pleae retry！')
    else:
        pass

# check and get the language.loc version number (fil_version)
def download_loc_en(todir):
    time_template()
    print("download.py >>> def download_loc_en() >>> todir: " + str(todir))
    en_loc_ver = 'http://dn.sea.playblackdesert.com/UploadData/ads_files'
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        a = urlopen(en_loc_ver, timeout=5)
    except:
        print("download.py >>> def download_loc_en(): something wrong, maybe timeout")
        showinfo('languagedata_en.loc','Downloading Timeout，Pleae retry！')
        version = False
    else:
        version = a.read().decode('utf-8')

# Use this lines if you need number version        
# use the version number (fil_version) to download the latest loc file
    if version != False:
        fil_version = findall(r'languagedata_en.loc\t(\d+)', version)
        url = 'http://dn.sea.playblackdesert.com/UploadData/ads/languagedata_en/' + "".join(fil_version) + '/languagedata_en.loc'
        # no need to change this languagedata_en.loc, relate to execute_list.py
        tofilename = 'languagedata_en.loc'
        download_file(url, todir, tofilename)
    else:
        pass
# line end
 
"""
# Use this lines if you don't need version number and only has one url.
# And remember to comment the upper lines.

# if you don't need a file version number, and only has one url, then just change the "url=" at below to yours.
    url = 'http://this.is.an.example/change it to something else/languagedata_en.loc'
# no need to change this languagedata_en.loc, relate to execute_list.py
    tofilename = 'languagedata_en.loc'
    download_file(url, todir, tofilename)
 
# line end 
"""
