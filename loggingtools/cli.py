import json
import os

import click
import ruamel.yaml as yaml

from loggingtools import __version__
from loggingtools.config import FORMATS, CONFIG_DICT


def yaml_dump(filepath):
    """Dumps configuration dictionary into yaml file"""
    with open(filepath, 'w') as fp:
        yaml.dump(CONFIG_DICT, fp,
                  default_flow_style=False,
                  indent=2,
                  Dumper=yaml.RoundTripDumper)


def json_dump(filepath):
    """Dumps configuration dictionary into json file"""
    with open(filepath, 'w') as fp:
        json.dump(CONFIG_DICT, fp,
                  indent=2)


@click.group()
@click.version_option(__version__)
def cli():
    """Command line client"""


@cli.command()
@click.option('--filename', '-n', default='logging', type=str)
@click.option('--fileformat', '-f', default='yml', type=click.Choice(FORMATS))
@click.option('--overwrite', is_flag=True, help='Overwrite existing file.')
def config(filename, fileformat, overwrite):
    """Create new logging configuration file.
    
    >>> config('logging', 'yml')
    
    or 
    
    >>> config('logging', 'json')
    """
    click.secho('Creating "{}.{}"'.format(filename, fileformat))

    filename, _ = os.path.splitext(filename)
    filepath = filename + '.' + fileformat

    if os.path.exists(filepath) and overwrite:
        raise FileExistsError(
            'File: "{}" already exists. If you want to overwrite existing '
            'configuration please supply "--overwrite" flag'.format(filepath))

    {'yml': yaml_dump, 'json': json_dump}[fileformat](filepath)
