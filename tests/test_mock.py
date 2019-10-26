import unittest
import hashlib
import logging
from unittest.mock import Mock

logger = logging.getLogger('root')


class SimpleService():
    def __init__(self, connector):
        self.connector = connector

    def get_hash(self, resource):
        output = self.connector.connect(resource)
        logger.info("output: %s", output)
        return hashlib.sha1(bytes(output, 'utf-8')).hexdigest()


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.mock_connector = Mock()
        self.service = SimpleService(self.mock_connector)

    def test_service(self):
        resource = 'https://docs.python.org/3/'
        self.mock_connector.connect.return_value = 'mock page content'
        self.service.get_hash(resource)
        self.mock_connector.connect.assert_called()
