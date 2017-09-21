import argparse
import os
from helper_scan import check_file_informations
from helper_output import create_dirs
from helper_output import copy_move_files


def get_args():
    parser = argparse.ArgumentParser(
        description='Scan the directory (input_dir) for Srednoselecs pictures and videos.' \
                    'The program firstly copy them to output_dir and afterwards move them to output_dir2',
    )

    parser.add_argument(
        '-i', '--input_dir', type=str, help='Direcory for scan. Input directory', required=True)
    parser.add_argument(
        '-oc', '--output_copy_dir', type=str, help='Destination directory. Output directory. The files will be copied', required=True)
    parser.add_argument(
        '-om', '--output_move_dir', type=str, help='Destination directory. Output directory. The files will be moved', required=True)

    args = parser.parse_args()
    return args


def check_if_dir(input_dir, output_copy_dir, output_move_dir):
    if not os.path.isdir(input_dir):
        print("Given arg1 (input_dir or -i) is <{}> is not directory".format(input_dir))
        exit(0)
    if not os.path.isdir(output_copy_dir):
        print("Given arg2 (output_copy_dir or -oc) is <{}> is not directory".format(output_copy_dir))
        exit(0)
    if not os.path.isdir(output_move_dir):
        print("Given arg3 (output_move_dir or -om) is <{}> is not directory".format(output_move_dir))
        exit(0)


def main():
    input_dirname = get_args().input_dir
    output_copy_dirname = get_args().output_copy_dir
    output_move_dirname = get_args().output_move_dir
    check_if_dir(input_dirname, output_copy_dirname, output_move_dirname)
    list_of_files = check_file_informations.list_all_files_in_dir(input_dirname)
    all_information_of_the_files = check_file_informations.check_crea_month_year(list_of_files, input_dirname)
    for file in all_information_of_the_files:
        year = file[1]
        month = file[2]
        create_dirs.create_direcory_for_files(output_copy_dirname, year, month)
        create_dirs.create_direcory_for_files(output_move_dirname, year, month)

    for file in all_information_of_the_files:
        file_name = file[0]
        print(file_name)
        source_file_path = input_dirname
        destination_copy_file_path = output_copy_dirname + '/' + file[1] + '/' + file[2]
        destination_move_file_path = output_move_dirname + '/' + file[1] + '/' + file[2]
        copy_move_files.copy_files(file_name, source_file_path, destination_copy_file_path)
        copy_move_files.move_files(file_name, source_file_path, destination_move_file_path)


if __name__ == "__main__":
    main()
