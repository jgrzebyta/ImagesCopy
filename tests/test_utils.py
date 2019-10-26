import unittest
import os
from collections.abc import Iterable
from images_copy import utils, log
from images_copy.utils import FilePath

logger = log.create_logger('root')
tested_directory = '.'


class TestUtils(unittest.TestCase):

    def test_list_files(self):
        expected = {'./images_copy/__init__.py', './images_copy/log.py',
                    './images_copy/utils.py'}
        actual = utils.list_files(tested_directory)
        # logger.info('actual: %s', actual)
        self.assertTrue(isinstance(actual, Iterable))
        actual_paths = set(map(lambda x: x.as_path(), actual))
        self.assertTrue(expected.issubset(actual_paths))

    def test_txt_extension(self):
        mockTextFile = FilePath('/tmp/mock_fdata', 'some_file.txt')
        self.assertEqual('txt', mockTextFile.extension())

    def test_TXT_extension(self):
        mockTextFile = FilePath('/tmp/mock_fdata', 'some_file.TXT')
        self.assertEqual('txt', mockTextFile.extension())

    def test_filename_without_ext(self):
        mockTextFile = FilePath('/tmp/mock_fdata', 'some_file.txt')
        self.assertEqual('some_file', mockTextFile.file_prefix())

    def test_long_filename_without_ext(self):
        mockTextFile = FilePath('/tmp/mock_fdata', 'some_file.tar.gz')
        self.assertEqual('some_file.tar', mockTextFile.file_prefix())

    def test_copy_file(self):
        original = FilePath('./images_copy', 'utils.py')
        target_directory = '/tmp'
        actual = utils.copy_file(original, target_directory)
        self.assertTrue(isinstance(actual, FilePath))
        self.assertTrue(os.path.exists(actual.as_path()))

    def test_files_filter(self):
        mock_directory = '/tmp/in_data/Some dir'
        in_files = [FilePath(mock_directory, 'file1.jpg'),
                    FilePath(mock_directory, 'file2.JPG'),
                    FilePath(mock_directory, 'file3.json'),
                    FilePath(mock_directory, 'file4.mp4'),
                    FilePath(mock_directory, 'file5.html')]
        actual = list(filter(utils.is_picture, in_files))
        expected = [FilePath(mock_directory, 'file1.jpg'),
                    FilePath(mock_directory, 'file2.JPG'),
                    FilePath(mock_directory, 'file4.mp4')]
        self.assertTrue(3, actual.__sizeof__)
        self.assertEqual(expected, actual)
        logger.info('Actual files: %s', actual)
