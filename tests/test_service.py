import unittest
from images_copy.utils import FilePath
from images_copy import service


class TestService(unittest.TestCase):
    def test_files_filter(self):
        mock_directory = '/tmp/in_data/Some dir'
        in_files = [FilePath(mock_directory, 'file1.jpg'),
                    FilePath(mock_directory, 'file2.JPG'),
                    FilePath(mock_directory, 'file3.json'),
                    FilePath(mock_directory, 'file4.mp4'),
                    FilePath(mock_directory, 'file5.html')]
        actual = list(filter(service.is_picture, in_files))
        expected = [FilePath(mock_directory, 'file1.jpg'),
                    FilePath(mock_directory, 'file2.JPG'),
                    FilePath(mock_directory, 'file4.mp4')]
        self.assertTrue(3, actual.__sizeof__)
        self.assertEqual(expected, actual)
