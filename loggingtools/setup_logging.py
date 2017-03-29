import json
import logging.config
import os


def load_config(filepath):
    """Config dictionary

    Args:
        filepath (str):

    Returns:
        dict:

    Raises:
        ImportError:
        FileNotFoundError:
    """
    if os.path.exists(filepath):
        _, ext = os.path.splitext(filepath)
        if ext == '.json':
            with open(filepath, 'rt') as fp:
                return json.load(fp)
        elif ext in ('.yml', '.yaml'):
            try:
                from ruamel import yaml
            except ImportError():
                import yaml
            except ImportError():
                raise ImportError('Install ruamel.yaml or pyyaml in \n'
                                  'order to use load dictionary \n'
                                  'configuration from yaml file. \n')
            with open(filepath, 'rt') as fp:
                return yaml.safe_load(fp.read())
        raise ValueError('File extension {ext} is not supported.'.format(
            ext=ext))
    else:
        raise FileNotFoundError(
            'Configuration file: "{path}" doesn\'t exist.'.format(
                path=filepath))


def setup_logging(path_or_config, logdir='.logs', env_key='LOG_CFG'):
    """Setup logging configurations defined by dict configuration.

    Args:
        path_or_config (str|dict):
            - dict: Dictionary config
            - str: Path to load dictionary configuration from. Can be json or yaml file.
        logdir (str|None):
            - None: Saves logfiles to current working directory
            - str: Saves logfiles to specified directory.
        env_key (str):
            Environment key for setting path to logging conf.

    References:
        - https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

    Todo:
        - Add support for .ini and .cfg files
    """
    path_or_config = os.getenv(env_key, path_or_config)

    if isinstance(path_or_config, str):
        config = load_config(path_or_config)
    elif isinstance(path_or_config, dict):
        config = path_or_config
    else:
        raise TypeError("Argument 'path_or_config' should be string or "
                        "dictionary.")

    # Configure directory to save logfiles
    if logdir:
        # Create directory if it doesnt already exist.
        try:
            os.makedirs(logdir, 0o700, exist_ok=True)
        except FileExistsError:
            pass

        # Prepend directory path to filenames.
        for name in config['handlers']:
            handler = config['handlers'][name]
            if 'filename' in handler:
                handler['filename'] = os.path.join(logdir, handler['filename'])

    # Configure logging for config dictionary
    logging.config.dictConfig(config)
