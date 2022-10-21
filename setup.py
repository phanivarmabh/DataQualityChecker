from setuptools import setup
setup(
    name = 'datachecker-cli',
    version = '0.1.0',
    packages = ['datachecker'],
    entry_points = {
        'console_scripts': [
            'datachecker = datachecker.__main__:main'
        ]
    })