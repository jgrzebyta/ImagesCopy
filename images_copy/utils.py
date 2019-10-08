import logging
import os
import collections
import shutil
from os import walk
from os.path import sep


class FilePath(object):
    """Representation of the full file path: directory and filename."""
    __slots__ = ['directory', 'filename']

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def __eq__(self, other):
        if not isinstance(other, FilePath):
            return NotImplemented
        return self.directory == other.directory and self.filename == other.filename

    def as_path(self):
        return self.directory + os.path.sep + self.filename

    def extension(self):
        return self.filename.split('.')[-1].lower()

    def file_prefix(self):
        lastDot = self.filename.rindex('.')
        return self.filename[0:lastDot]


def list_files(directory):
    """List all files inside a [[directory]]"""
    logger = logging.getLogger('root')
    logger.debug('process directory %s', directory)
    out_array = []
    for (dirpath, _, filenames) in walk(directory):
        for fs in filenames:
            out_array.append(FilePath(dirpath, fs))
    return out_array


def copy_file(original, target_directory):
    logger = logging.getLogger('root')
    assert(isinstance(original, FilePath))
    assert(os.path.exists(target_directory))
    splited_dirs = collections.deque(original.directory.split(sep))
    splited_dirs.popleft()
    copy_directory = sep.join([target_directory, sep.join(splited_dirs)])
    target_file = FilePath(copy_directory, original.filename)
    try:
        os.makedirs(target_file.directory)
        shutil.copy2(original.as_path(), target_file.as_path())
        logger.info('%s -> %s', original.as_path(), target_file.as_path())
    except FileExistsError as err:
        logger.warning('File exists: %s', err.filename)
    return target_file
