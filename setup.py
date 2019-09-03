from setuptools import setup

setup(
    name='firemansam',
    version='1.0.0',
    packages=['firemansam', 'firemansam.tests'],
    test_suite='firemansam.tests',
    url='https://github.com/anthonyblanchflower/firemansam',
    author='Anthony Blanchflower',
    author_email='anthony.blanchflower@comparethemarket.com',
    description='Functions for extracting fixes data from directories containing py files'
)
