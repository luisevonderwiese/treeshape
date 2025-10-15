from setuptools import find_packages
from setuptools import setup

setup(
    name='treeshapy',
    version='0.0.1',
    install_requires=['numpy', 'ete3'],
    packages=find_packages('.'),
    package_dir={'': '.'},
    package_data={'treeshapy' :['treeshapy/resources/*']},
    url='https://github.com/luisevonderwiese/treeshapy',
    license='GNU',
    author='Luise Häuser',
    author_email='luise.haeuser@h-its.org',
    description='Implementation of various tree shape indices in python'
)
