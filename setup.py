from setuptools import setup, find_packages
import os
from pathlib import Path
os.path.dirname(os.path.abspath('__file__'))
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



setup(
    name="demo42ceu",
    version="1.1",
    author="Dabide",
    author_email="",
    description="Demo package",
    url="",
    license="MIT",
    install_requires=[],
    packages=find_packages()
)

