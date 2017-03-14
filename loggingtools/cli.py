import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option('--name', '-n')
def create():
    """Create new logging configuration file."""
    raise NotImplementedError()
