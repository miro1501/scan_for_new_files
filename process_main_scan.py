import argparse
import os
import time

def get_args():
    parser = argparse.ArgumentParser(
        description='Scan the folder for Srednoselecs new pictures and videos',
    )

    parser.add_argument(
        '-i', '--input_dir', type=str, help='Direcory for scan. Input directory', required=True)
    parser.add_argument(
        '-o', '--output_dir', type=str, help='Destination directory. Output directory', required=True)

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

def check_if_dir(input_dir, output_dir):
    if not os.path.isdir(input_dir):
        print("Given arg1 (input_dir or -i) is <{}> is not directory".format(input_dir))
        exit(0)
    if not os.path.isdir(input_dir):
        print("Given arg2 (output_dir or -o) is <{}> is not directory".format(output_dir))
        exit(0)



def main():
    input_dirname = get_args().input_dir
    output_dirname = get_args().output_dir
    check_if_dir(input_dirname, output_dirname)
    list_of_files = list_all_files_in_dir(input_dirname)
    all_informations_of_the_files = check_crea_month_year(list_of_files)


if __name__ == "__main__":
    main()
