from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Reynaldo Luevano',
    author_email='reynaldoluevano@gmail.com',
    packages=find_packages('src'),
    description='A utility for backing up PostgreSQL Databases',
    long_description=long_description,
    long_description_content_type='text/markdown'
)