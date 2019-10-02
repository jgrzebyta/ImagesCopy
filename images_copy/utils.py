import logging
import os
from os import walk


class FilePath(object):
    """Representation of the full file path: directory and filename."""
    __slots__ = ['directory', 'filename']

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def as_path(self):
        return self.directory + os.path.sep + self.filename

    def extension(self):
        return self.filename.split('.')[-1].lower()


def list_files(directory):
    """List all files inside a [[directory]]"""
    logger = logging.getLogger('root')
    logger.debug('process directory %s', directory)
    out_array = []
    for (dirpath, _, filenames) in walk(directory):
        for fs in filenames:
            out_array.append(FilePath(dirpath, fs))
    return out_array
