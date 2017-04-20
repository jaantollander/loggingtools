from setuptools import setup
from loggingtools import __version__, __license__, __author__, __email__


install_requires = [
    'colorlog',
    'colorama',
    'ruamel.yaml',
    'click',
]
tests_require = [
    'tox',
    'pytest',
    'pytest-cov',
]

setup(
    name='loggingtools',
    version=__version__,
    packages=['loggingtools', 'loggingtools.tests'],
    include_package_data=True,
    url='https://github.com/jaantollander/loggingtools.git',
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='Python logging dictionary configuration from yaml, json or '
                'dictionary.',
    entry_points={
        'console_scripts': [
            'loggingtools=loggingtools.cli:cli',
        ]
    },
    install_requires=install_requires,
    test_suite='tests',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
