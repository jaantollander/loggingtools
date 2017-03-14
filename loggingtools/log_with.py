import functools
import inspect
import logging


class log_with(object):
    """Logging decorator that allows you to log with a specific logger.

    Todo:
        - Indent message by function call stack level
    """
    def __init__(self, logger=None, loglevel=logging.INFO):
        """Initialize log_with

        Args:
            logger (Logger|None):
                Instance of a logger
            loglevel (int):
                Level of logging
        """
        self.logger = logger
        self.loglevel = loglevel

    @staticmethod
    def format_args(args, kwargs, arg_names):
        def items():
            for i, name in enumerate(arg_names):
                if i < len(args):
                    yield name, args[i]
                elif name in kwargs:
                    yield name, kwargs[name]

        d = ', '.join(('{}: {}'.format(*m) for m in items()))
        return '{' + d + '}'

    @staticmethod
    def format_func(function):
        return '<' + function.__name__ + '>'

    def __call__(self, function):
        if not self.logger:
            # If logger is not set, set module's logger.
            self.logger = logging.getLogger(function.__module__)

        # Function signature
        sig = inspect.signature(function)
        arg_names = sig.parameters.keys()

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            msg = ' '.join((self.format_func(function),
                            self.format_args(args, kwargs, arg_names)))

            self.logger.log(self.loglevel, msg)

            result = function(*args, **kwargs)
            return result

        return wrapper
