import os
import tempfile
import logging
from loggingtools.setup_logging import setup_logging


def filepath(conf_file: str) -> str:
    return os.path.join(os.path.dirname(__file__), 'files', conf_file)


def test_setup_logging():
    for conf_file in ('logging.yaml', 'logging.json'):
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_logging(filepath(conf_file), logdir=tmpdir)
            logger = logging.getLogger('package_name')
            logger.info('This should work.')
            assert True
