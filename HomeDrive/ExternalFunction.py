import tarfile
import threading
import zipfile
from datetime import datetime
from glob import glob
import os
import shutil
from os.path import basename
import shutil

import time

from config import logger

from __init__ import app
from flask import send_from_directory, send_file


def single_dir(path):
    file_dir = {}
    folder_dir = {}
    for item in glob(path+"/*"):
        state = item.split("\\")[-1]

        if state[0] == "/":
            state = state[1::]
        if os.path.isfile(item):

            file_dir[state] = cal_size(item)
        elif os.path.isdir(item):
            folder_dir[state] = cal_size(item)
        else:
            file_dir[state] = cal_size(item)

    return [folder_dir,file_dir]


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def cal_size(file_name):
    if os.path.isfile(file_name):
        file_info = os.stat(file_name)
        return convert_bytes(file_info.st_size)

def round_fun(path,li):
    for item in glob(path+"/*"):
            if os.path.isfile(item):
                li[path].append(item)
            else:
                li[path].append(item)
                li[item] = []
                round_fun(item,li)
    return li

def make_zip(path,obj,list_folders,remove_dir):
    for item in list_folders[path]:
        if item not in list_folders:
            obj.write(item,basename(item))
        else:
            temp = item
            new_zip_obj = zipfile.ZipFile(temp+".zip","w",zipfile.ZIP_DEFLATED)
            make_zip(item,new_zip_obj,list_folders,remove_dir)
            new_zip_obj.close()
            obj.write(temp+".zip",basename(temp+".zip"))
            remove_dir.insert(0,temp+".zip")

def remove_zip_file(remove_dir):
    for item in remove_dir:
        os.remove(item)


def check_folder(path):
    if os.path.isdir(path):
        return True
    else:
        return False


class myThread(threading.Thread):
    def __init__(self,  li):
        threading.Thread.__init__(self)
        self.li = li

    def run(self):
                time.sleep(3)
                while (len(self.li) != 0):
                    try:
                        os.remove(self.li[0])
                        (self.li).pop(0)
                    except:
                        temp = self.li[0]
                        (self.li).pop(0)
                        self.li.append(temp)
                        time.sleep(3)



def build_tar_file(main_path,list_of_paths):
    file_name = "-".join(str( datetime.now().time() ).split(":")[:3])+".tar.gz"
    tar = tarfile.open(file_name,"w")
    for item in list_of_paths:
        tar.add(main_path+"\\"+item)
    tar.close()
    return file_name


def extract_folder(path,file_name):
    zip_ref = zipfile.ZipFile(path+file_name, 'r')
    zip_ref.extractall(path)
    zip_ref.close()


