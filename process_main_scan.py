import argparse
import os
from helper_scan import check_file_informations
from helper_output import create_dirs
from helper_output import copy_files


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
    list_of_files = check_file_informations.list_all_files_in_dir(input_dirname)
    all_informations_of_the_files = check_file_informations.check_crea_month_year(list_of_files, input_dirname)
    for file in all_informations_of_the_files:
        year = file[1]
        month = file[2]
        create_dirs.create_direcory_for_files(output_dirname, year, month)

    for file in all_informations_of_the_files:
        file_name = file[0]
        print(file_name)
        source_file_path = input_dirname
        print(source_file_path)
        destination_file_path = output_dirname + '/' + file[1] + '/' + file[2]
        print(destination_file_path)
        copy_files.copy_files(file_name, source_file_path, destination_file_path)


if __name__ == "__main__":
    main()
