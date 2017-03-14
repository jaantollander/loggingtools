import json
import logging.config
import os
from typing import Union, Optional


def _config_dictionary(path_or_config: Union[str, dict]) -> dict:
    """Config dictionary

    Args:
        path_or_config (str|dict):

    Returns:
        dict:

    Raises:
        ImportError:
        FileNotFoundError:
    """
    if isinstance(path_or_config, dict):
        return path_or_config
    elif isinstance(path_or_config, str):
        if os.path.exists(path_or_config):
            _, ext = os.path.splitext(path_or_config)
            if ext == '.json':
                with open(path_or_config, 'rt') as fp:
                    return json.load(fp)
            elif ext in ('.yml', '.yaml'):
                try:
                    from ruamel import yaml
                except ImportError:
                    import yaml
                except Exception:
                    raise ImportError('Install ruamel.yaml or pyyaml in \n'
                                      'order to use load dictionary \n'
                                      'configuration from yaml file. \n')
                with open(path_or_config, 'rt') as fp:
                    return yaml.safe_load(fp.read())
            raise ValueError('File extension {ext} is not supported.'.format(
                ext=ext))
        else:
            raise FileNotFoundError(
                'Configuration file: "{path}" doesn\'t exist.'.format(
                    path=path_or_config))


def setup_logging(path_or_config: Union[str, dict],
                  logdir: Optional[str] = '.logs',
                  default_level: int = logging.INFO,
                  env_key: str = 'LOG_CFG') -> None:
    """Setup logging configurations defined by dict configuration.

    Args:
        path_or_config (str):
            - dict: Dictionary config
            - str: Path to load dictionary configuration from. Can be json or yaml file.
        logdir (str|None):
            - None: Saves logfiles to current working directory
            - str: Saves logfiles to specified directory.
        default_level (int|str):
            Default logging level to use if dict config is not configured.
        env_key (str):
            Environment key for setting path.

    References:
        - https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

    Todo:
        - Read configs from config (.cfg) file
    """
    path_or_config = os.getenv(env_key, path_or_config)
    config = _config_dictionary(path_or_config)

    if config:
        # Configure directory to save logfiles
        if logdir:
            # Create directory if it doesnt already exist.
            if not os.path.exists(logdir):
                os.mkdir(logdir)

            # Prepend directory path to filenames.
            for name in config['handlers']:
                handler = config['handlers'][name]
                if 'filename' in handler:
                    handler['filename'] = os.path.join(logdir, handler['filename'])

        # Configure logging for config dictionary
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
