import shutil

class CopyMoveFiles:
    def copy_files(file, source_dir_path, destination_dir_path):
        source_file_path = source_dir_path + '/' + file
        destination_file_path = destination_dir_path + '/' + file
        shutil.copyfile(source_file_path, destination_file_path)

    def move_files(file, source_dir_path, destination_dir_path):
        source_file_path = source_dir_path + '/' + file
        destination_file_path = destination_dir_path + '/' + file
        shutil.move(source_file_path, destination_file_path)
