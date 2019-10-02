import logging

pattern = '%(asctime)s [%(levelname)s] - %(module)s: %(message)s'


def create_logger(name):
    """Create logger with custom name"""
    formatter = logging.Formatter(fmt=pattern)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
