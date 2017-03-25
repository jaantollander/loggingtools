import contextlib
import os
from tempfile import TemporaryDirectory

import pytest
from click.testing import CliRunner

from loggingtools.cli import config


@pytest.fixture(scope='module')
def tmpdir():
    """Temporary directory"""
    with TemporaryDirectory() as directory:
        @contextlib.contextmanager
        def remember_cwd():
            curdir = os.getcwd()
            try:
                os.chdir(directory)
                yield
            finally:
                os.chdir(curdir)
        yield remember_cwd


@pytest.mark.parametrize('fileformat', ['yml', 'json'])
def test_cli(tmpdir, fileformat):
    filename = 'logging'
    runner = CliRunner()
    with tmpdir():
        result = runner.invoke(config, ['-n', filename, '-f', fileformat])
        assert result.exit_code == 0
        assert os.path.exists(filename + '.' + fileformat)
