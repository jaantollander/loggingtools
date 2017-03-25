import json
import os

import click
import ruamel.yaml as yaml

FORMATS = ('yaml', 'json')
path = os.path.join(os.path.dirname(__file__), 'templates', 'logging.yml')
with open(path) as fp:
    CONFIG_DICT = yaml.safe_load(fp)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option('--fileformat', '-f', default='yaml', type=click.Choice(FORMATS))
def create(filename, fileformat):
    """Create new logging configuration file."""
    if fileformat == 'yaml':
        with open(filename + '.yaml', 'w') as fp:
            yaml.dump(CONFIG_DICT, fp, default_flow_style=False, indent=2)
    elif fileformat == 'json':
        with open(filename + '.json', 'w') as fp:
            json.dump(CONFIG_DICT, fp, indent=2)
