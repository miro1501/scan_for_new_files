import unittest, os
import shutil, tempfile
from scan_for_new_files.copy_move_files import CopyMoveFiles


class CopyMoveFilesTestCase( unittest.TestCase ):
	def setUp(self):
	    #create temp direcroties
	    self.test_dir_1 = tempfile.mkdtemp()
	    self.test_dir_2 = tempfile.mkdtemp()
	    #create one temp file
	    self.file = tempfile.NamedTemporaryFile(dir=self.test_dir_1)
	    print(self.test_dir_1)
	    print(self.test_dir_2)
	    print(self.file)

	def tearDown(self):
	    #remove the directories after the test
            shutil.rmtree(self.test_dir_1)		
            shutil.rmtree(self.test_dir_2)		

	def test_copy_file(self):
	    CopyMoveFiles.move_files(self.file, self.test_dir_1, self.test_dir_2)
