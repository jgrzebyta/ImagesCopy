import unittest
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
