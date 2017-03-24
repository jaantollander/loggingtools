from loggingtools.setup_logging import setup_logging
from loggingtools.log_with import log_with

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


__author__ = 'Jaan Tollander de Balsch'
__github_repo__ = 'jaantollander/loggingtools'

__all__ = """
setup_logging
log_with
""".split()
