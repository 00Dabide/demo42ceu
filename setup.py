from setuptools import setup, find_packages
import os
from pathlib import Path
os.path.dirname(os.path.abspath('__file__'))


setup(
    name="demo42ceu",
    version="1.1",
    author="Dabide",
    author_email="",
    description="Demo package",
    url="",
    license="MIT",
    install_requires=[],
    packages=find_packages(),
    long_description='This is a long description',
    long_description_content_type='text/markdown'
)
