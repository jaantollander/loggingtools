import tempfile
import logging
from loggingtools.setup_logging import setup_logging
from loggingtools.log_with import log_with
from loggingtools.config import CONF_PATHS, LOGGER_NAME


def test_setup_logging():
    for conf_file in CONF_PATHS:
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_logging(conf_file, logdir=tmpdir)
            logger = logging.getLogger(LOGGER_NAME)
            logger.info('')
            assert True

            logging.shutdown()


def test_log_with():
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_logging(CONF_PATHS[0], logdir=tmpdir)
        logger = logging.getLogger(LOGGER_NAME)

        @log_with(logger)
        def with_args(a, b, c, d):
            return True

        assert with_args('a', 1, 'c', 3)

        @log_with()
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
