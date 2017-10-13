from setuptools import setup, find_packages

setup(
    name="scan_for_new_files",
    version=__version__,
    packages=find_packages(),
    install_requires=["pillow"]
)