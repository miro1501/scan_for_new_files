import unittest, os, shutil
from scan_for_new_files.copy_move_files import CopyMoveFiles


class CopyMoveFilesTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("setUp")
        self.dir1 = "dir1"
        os.mkdir(self.dir1)
        self.dir2 = "dir2"
        os.mkdir(self.dir2)
        self.file1 = "test_file1"
        self.file2 = "test_file2"
        os.mknod(self.dir1 + "/test_file1")
        os.mknod(self.dir2 + "/test_file2")				

    def test_move_file(self):
        print("test_move_file")			
        CopyMoveFiles.move_files(self.file1, self.dir1, self.dir2)
        self.assertEqual(os.path.isfile("dir2/test_file1"), True)

    def test_copy_file(self):
        print("test_copy_file")			
        CopyMoveFiles.copy_files(self.file2, self.dir2, self.dir1)
        self.assertEqual(os.path.isfile("dir1/test_file2"), True)

    @classmethod
    def tearDown(self):
        # remove the directories after the test
        print("teardown")
        shutil.rmtree(self.dir1)
        shutil.rmtree(self.dir2)