import unittest, os, shutil
from scan_for_new_files.create_dirs import CreateDirs

class CopyMoveFilesTestCase(unittest.TestCase):				

    def test_create_dir(self):
        print("test_create_dir")
        current_dir = os.getcwd() + "/test/"        
        CreateDirs.create_direcory_for_files(current_dir,"1977","01")	
        self.assertEqual(os.path.isdir(current_dir + "1977/01"), True)

        CreateDirs.create_direcory_for_files(current_dir,"1977","01")	
        self.assertEqual(os.path.isdir(current_dir + "1977/01"), True)

    @classmethod
    def tearDown(self):
        # remove the directories after the test
        print("teardown")
        current_dir = os.getcwd() + "/test/"
        shutil.rmtree(current_dir + "/1977")
