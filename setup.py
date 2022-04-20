from importlib.metadata import entry_points
from setuptools import find_packages, setup

setup(
    name='Simple Todo CLI',
    version=0.1,
    packages=find_packages(),
    entrypoints={
        'console_script': [
            'todo=Main:main'
        ]
    }
)