import os
import tempfile
import logging
from loggingtools.setup_logging import setup_logging
from loggingtools.log_with import log_with

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
CONF_FILES = [os.path.join(TEMPLATE_DIR, filename) for filename in
              ('logging.yml', 'logging.json')]
LOGGER_NAME = 'package_name'


def test_setup_logging():
    for conf_file in CONF_FILES:
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_logging(conf_file, logdir=tmpdir)
            logger = logging.getLogger(LOGGER_NAME)
            logger.info('')
            assert True

            logging.shutdown()


def test_log_with():
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_logging(CONF_FILES[0], logdir=tmpdir)
        logger = logging.getLogger(LOGGER_NAME)

        @log_with(logger)
        def with_args(a, b, c, d):
            return True

        assert with_args('a', 1, 'c', 3)

        @log_with(logger)
        def with_args_kwargs(a, b, c='c', d=3):
            return True

        assert with_args_kwargs('a', 1, c='c')

        class Foo:
            @log_with(logger)
            def method(self, a, b, c='c', d='d'):
                return True

        assert Foo().method('1', '2', c='3', d='4')
        assert Foo().method('a', 'b', d='d')

        logging.shutdown()
