import os

class CreateDirs:
    def create_direcory_for_files(output_dir, year, month):
        year_path = output_dir + '/' + year
        month_path = year_path + '/' + month
        if not os.path.exists(year_path):
            os.makedirs(year_path)
        else:
            print("Path {} exists.".format(year_path))

        if not os.path.exists(month_path):
            os.makedirs(month_path)
        else:
            print("Path {} exists.".format(month_path))
