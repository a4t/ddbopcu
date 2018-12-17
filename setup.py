from setuptools import setup, find_packages
import sys

sys.path.append('./ddbopcu')
sys.path.append('./tests')

setup(
    name='ddbopcu',
    version='0.0.1',
    description='DynamoDB output capacity units',
    author='a4t',
    author_email='iwanomoto@gmail.com',
    url='https://github.com/a4t/ddbopcu',
    install_requires=['boto3'],
    packages=find_packages(exclude=('tests')),
    test_suite='tests')
