import pykka
import logging
from collections import namedtuple
from images_copy import utils
from queue import LifoQueue
from images_copy.queue import QueueHolder

logger = logging.getLogger('root')


DirectoryTarget = namedtuple('DirectoryTarget', ['source'])


class LocalLister(pykka.ThreadingActor):
    def __init__(self, consumer_factory):
        super(LocalLister, self).__init__()
        self.consumer_factory = consumer_factory
        self.consumers = []

    def on_receive(self, message):
        logger.info("receive message '%s'", message)
        if isinstance(message, DirectoryTarget):
            files = utils.list_files(message.source)
            for file in files:
                consumer = self.consumer_factory.new()
                consumer.tell(file)
                self.consumers.append(consumer)
            return len(files)
        return message


class QueueManager(pykka.ThreadingActor):

    def __init__(self, queue=LifoQueue()):
        super(QueueManager, self).__init__()
        self.queue_holder = QueueHolder()
