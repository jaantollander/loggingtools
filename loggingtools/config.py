import os

import ruamel.yaml as yaml

FORMATS = ('yml', 'json')
BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
CONF_PATHS = [os.path.join(TEMPLATE_DIR, filename) for filename in
              ('logging.yml', 'logging.json')]
LOGGER_NAME = 'loggingtools'
YAML_CONFIG, JSON_CONFIG = CONF_PATHS

with open(YAML_CONFIG) as fp:
    CONFIG_DICT = yaml.load(fp, Loader=yaml.RoundTripLoader)
