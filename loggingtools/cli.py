import json

import click
import ruamel.yaml as yaml

from loggingtools import __version__
from loggingtools.config import FORMATS, CONFIG_DICT


@click.group()
@click.version_option(__version__)
def cli():
    """Command line client"""


@cli.command()
@click.option('--filename', '-n', default='logging', type=str)
@click.option('--fileformat', '-f', default='yml', type=click.Choice(FORMATS))
def config(filename: str, fileformat: str):
    """Create new logging configuration file.
    
    >>> config('logging', 'yml')
    """
    click.secho('Creating "{}.{}"'.format(filename, fileformat))

    if fileformat in 'yml':
        with open(filename + '.yml', 'w') as fp:
            yaml.dump(CONFIG_DICT, fp, default_flow_style=False, indent=2,
                      Dumper=yaml.RoundTripDumper)
    elif fileformat == 'json':
        with open(filename + '.json', 'w') as fp:
            json.dump(CONFIG_DICT, fp, indent=2)
