import os
import time
from datetime import datetime
from PIL import Image


class CheckFileInformations:
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
            try:
                img = Image.open(input_dir + '/' + file)
                exif_data = img._getexif()
                strImageDate = exif_data[36867]
                year = time.strptime(strImageDate, "%Y:%m:%d %H:%M:%S").tm_year
                month_tmp = time.strptime(strImageDate, "%Y:%m:%d %H:%M:%S").tm_mon
                month = str(month_tmp).zfill(2)
                print("Crea: Year {}".format(year))
                print("Crea: Month {}".format(month))
            except:
                print("Not image")
                year = time.strftime('%Y', time.gmtime(os.path.getmtime(input_dir + '/' + file)))
                month = time.strftime('%m', time.gmtime(os.path.getmtime(input_dir + '/' + file)))

            tmp_list.append(file)
            tmp_list.append(str(year))
            tmp_list.append(str(month))
            files_infomation.append(tmp_list)
        return files_infomation
