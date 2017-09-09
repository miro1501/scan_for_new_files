import argparse
import os
from os.path import isfile
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description='Scan the folder for Srednoselecs new pictures and videos',
    )
    parser.add_argument(
        '-s', '--dir', type=str, help='Direcory for scan', required=True)
    args = parser.parse_args()
    return args

def list_all_files_in_dir(dirname):
    dirs = os.listdir(dirname)
    for file in dirs:
        if os.path.isfile(file):
            print("Found file",file)


def main():
    dirname = get_args().dir
    if os.path.isdir(dirname):
        list_all_files_in_dir(dirname)
    else:
        print("Given arg is <{}> is not directory".format(dirname))



if __name__ == "__main__":
    main()
