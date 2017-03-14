import os
import tempfile
import logging
from loggingtools.setup_logging import setup_logging
from loggingtools.log_with import log_with


conf_files = ('logging.yaml', 'logging.json')


def filepath(conf_file: str) -> str:
    return os.path.join(os.path.dirname(__file__), 'files', conf_file)


def test_setup_logging():
    for conf_file in conf_files:
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_logging(filepath(conf_file), logdir=tmpdir)
            logger = logging.getLogger('package_name')
            logger.info('This should work.')
            assert True


def test_log_with():
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_logging(filepath(conf_files[0]), logdir=tmpdir)
        logger = logging.getLogger('package_name')

        @log_with(logger)
        def with_args(a, b, c, d):
            return True

        assert with_args('a', 1, 'c', 3)

        @log_with(logger)
        def with_args_kwargs(a, b, c='c', d=3):
            return True

        assert with_args_kwargs('a', 1, c='c')
