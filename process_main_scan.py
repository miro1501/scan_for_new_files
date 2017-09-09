import argparse
import os
import time

def get_args():
    parser = argparse.ArgumentParser(
        description='Scan the folder for Srednoselecs new pictures and videos',
    )
    parser.add_argument(
        '-s', '--dir', type=str, help='Direcory for scan', required=True)
    args = parser.parse_args()
    return args


def list_all_files_in_dir(dirname):
    list_of_files = []
    dirs = os.listdir(dirname)
    for files in dirs:
        list_of_files.append(dirname + '/' + files)
    return list_of_files

def check_crea_month_year(files):
    files_infomation = []
    for file in files:
        tmp_list = []
        year = time.strftime('%Y', time.gmtime(os.path.getmtime(file)))
        month = time.strftime('%m', time.gmtime(os.path.getmtime(file)))
        tmp_list.append(file)
        tmp_list.append(year)
        tmp_list.append(month)
        files_infomation.append(tmp_list)
    return files_infomation

def main():
    dirname = get_args().dir
    list_of_files = []
    if os.path.isdir(dirname):
        list_of_files = list_all_files_in_dir(dirname)
    else:
        print("Given arg is <{}> is not directory".format(dirname))

    all_informations_of_the_files = check_crea_month_year(list_of_files)
    print(all_informations_of_the_files)

if __name__ == "__main__":
    main()
