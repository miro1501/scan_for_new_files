# following libs are needed:
# sudo apt-get install zlib1g-dev
# sudo apt-get install libjpeg-dev
from setuptools import setup

setup(
    name='scan_for_new_files',
    packages = ['scan_for_new_files'],
    install_requires = ['Pillow >= 2.0.0']
)