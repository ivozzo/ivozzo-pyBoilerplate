import logging


def init_logger(logging_level, path, filename):
    global logger

    loggerDictionary = {"INFO": logging.INFO, "WARN": logging.WARN, "DEBUG": logging.DEBUG, "ERROR": logging.ERROR}

    logging.basicConfig(
        level=loggerDictionary[logging_level],
        format="%(asctime)s|[%(threadName)-12.12s]|[%(levelname)-5.5s]| %(message)s",
        handlers=[
            logging.FileHandler("{0}/{1}".format(path, filename)),
            logging.StreamHandler()
        ])

    return logging.getLogger()
