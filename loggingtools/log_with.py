import functools
import inspect
import logging
from timeit import default_timer as timer

import math
import sys


def format_time(timespan, precision=3):
    """Formats the timespan in a human readable form

    Args:
        timespan (float):
            Time in seconds.
        precision (int):
            Desired precision.
    """

    if timespan >= 60.0:
        # we have more than a minute, format that in a human readable form
        # Idea from http://snipplr.com/view/5713/
        parts = [("d", 60 * 60 * 24), ("h", 60 * 60), ("min", 60), ("s", 1)]
        time = []
        leftover = timespan
        for suffix, length in parts:
            value = int(leftover / length)
            if value > 0:
                leftover %= length
                time.append(u'%s%s' % (str(value), suffix))
            if leftover < 1:
                break
        return " ".join(time)

    # Unfortunately the unicode 'micro' symbol can cause problems in
    # certain terminals.
    # See bug: https://bugs.launchpad.net/ipython/+bug/348466
    # Try to prevent crashes by being more secure than it needs to
    # E.g. eclipse is able to print a µ, but has no sys.stdout.encoding set.
    units = [u"s", u"ms", u'us', "ns"]  # the recordable value
    if hasattr(sys.stdout, 'encoding') and sys.stdout.encoding:
        try:
            u'\xb5'.encode(sys.stdout.encoding)
            units = [u"s", u"ms", u'\xb5s', "ns"]
        except:
            pass
    scaling = [1, 1e3, 1e6, 1e9]

    if timespan > 0:
        order = min(-int(math.floor(math.log10(timespan)) // 3), 3)
    else:
        order = 3
    # return u"%.*g %s" % (precision, timespan * scaling[order], units[order])
    return u"{:.1f} {}".format(timespan * scaling[order], units[order])


def format_args(args, kwargs, arg_names):
    """Format args

    Args:
        args (tuple):
        kwargs (dict):
        arg_names (List[str]):

    Returns:
        str:
    """

    def items():
        for i, name in enumerate(arg_names):
            if i < len(args):
                yield name, args[i]
            elif name in kwargs:
                yield name, kwargs[name]

    d = ', '.join(('{}: {}'.format(*m) for m in items()))
    return '{' + d + '}'


def format_func(function, qualname=False):
    """Format func

    Args:
        function (str):

    Returns:
        str:
    """
    if qualname:
        try:
            return '<' + function.__qualname__ + '>'
        except AttributeError:
            pass
    return '<' + function.__name__ + '>'


def log_with(logger=None, loglevel=logging.INFO, qualname=False, timed=False):
    """Logging decorator

    Args:
        logger (Logger|None):
            Instance of a logger
        loglevel (int):
            Level of logging
        qualname (bool): 
        timed (bool): 

    Examples:
        >>> @log_with(loglevel=logging.DEBUG)
        >>> def func():
        >>>     pass
    """
    def decorator(func):
        # If logger is not set, set module's logger.
        _logger = logger if logger else logging.getLogger(func.__module__)

        # Function signature
        arg_names = inspect.signature(func).parameters.keys()

        # Logger message
        msg = format_func(func, qualname) + ' {fmt}'

        if timed:
            @functools.wraps(func)
            def _func(*args, **kwargs):
                start = timer()
                result = func(*args, **kwargs)
                end = timer()
                _logger.log(loglevel, msg.format(
                    fmt='Time: {}'.format(format_time(timespan=(end - start)))))
                return result
        else:
            _func = func

        @functools.wraps(_func)
        def wrapper(*args, **kwargs):
            _logger.log(loglevel, msg.format(fmt=format_args(args, kwargs, arg_names)))
            result = _func(*args, **kwargs)
            return result
        return wrapper
    return decorator
