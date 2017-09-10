import os
import time


def list_all_files_in_dir(dirname):
    list_of_files = []
    dirs = os.listdir(dirname)
    for files in dirs:
        print(files)
        list_of_files.append(files)
    return list_of_files


def check_crea_month_year(files, input_dir):
    files_infomation = []
    for file in files:
        tmp_list = []
        year = time.strftime('%Y', time.gmtime(os.path.getmtime(input_dir + '/' + file)))
        month = time.strftime('%m', time.gmtime(os.path.getmtime(input_dir + '/' + file)))
        tmp_list.append(file)
        tmp_list.append(year)
        tmp_list.append(month)
        files_infomation.append(tmp_list)
    return files_infomation
