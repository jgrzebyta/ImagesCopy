import unittest
import pykka
import logging
from unittest.mock import MagicMock, Mock
from pykka import ActorRef
from queue import LifoQueue
from images_copy import actors
from threading import Lock
from images_copy.actors import DirectoryTarget


logger = logging.getLogger('root')


class StubConsumer(pykka.ThreadingActor):
    def __init__(self):
        super(StubConsumer, self).__init__()


class TestLister(unittest.TestCase):
    def setUp(self):
        self.consumer_factory_mock = Mock()
        self.lister_actor = actors.LocalLister.start(self.consumer_factory_mock)
        self.actual_files = {}
        self.lock = Lock()

    def tear_down(self):
        logger.info('finish test')
        pykka.ActorRegistry.stop_all()

    def add_file(self, file):
        with self.lock:
            self.actual_files.add(file)

    def test_list_directory(self):
        listed_directory = DirectoryTarget(source=".")
        # expected = {'./images_copy/__init__.py', './images_copy/log.py',
        #             './images_copy/utils.py'}
        stub_consumer = MagicMock(spec=ActorRef)
        self.consumer_factory_mock.new.return_value = stub_consumer
        actual = self.lister_actor.ask(listed_directory)
        self.assertTrue(isinstance(actual, int))
        self.consumer_factory_mock.new.assert_called()
        consumer_args = stub_consumer.tell.call_args
        logger.info('Consumer args: %s', consumer_args)


class TestQueueManager(unittest.TestCase):
    def setup(self):
        self.mock_queue = MagicMock(spec=LifoQueue)
        self.queueManager = actors.QueueManager.start(queue=self.mock_queue)

    def test_put_message(self):
        None

    def test_get_message(self):
        None
