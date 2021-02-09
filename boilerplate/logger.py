import boilerplate.logging.initializer as initializer


class Logger:
    def __init__(self, path, filename, level):
        self.path = path
        self.filename = filename
        self.level = level
        self.logger = initializer.init_logger(logging_level=level, path=path, filename=filename)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)
