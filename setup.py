from setuptools import setup
from loggingtools import __version__


setup(
    name='loggingtools',
    version=__version__,
    packages=['loggingtools', 'loggingtools.tests'],
    url='https://github.com/jaantollander/loggingtools.git',
    license='MIT',
    author='Jaan Tollander de Balsch',
    author_email='jaan.tollander@gmail.com',
    description='Python logging dictionary configuration from yaml, json or Python dict',
    entry_points={
        'console_scripts': [
            'loggingtools=loggingtools.cli:cli',
        ]
    },
    install_requires=['typing', 'colorlog', 'colorama', 'ruamel.yaml', 'click']
)
