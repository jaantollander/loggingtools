from loggingtools.log_with import log_with
from loggingtools.setup_logging import setup_logging
from ._version import get_versions

__all__ = """
setup_logging
log_with
""".split()

__author__ = 'Jaan Tollander de Balsch'
__email__ = 'jaan.tollander@gmail.com'
__version__ = get_versions()['version']
__github_repo__ = 'jaantollander/loggingtools'
__license__ = 'MIT'

del get_versions
