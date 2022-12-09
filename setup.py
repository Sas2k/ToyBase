from setuptools import setup, find_packages

long_description = open("README.md", "r", encoding="utf-8").read()

setup(
    name="ToyBase",
    version="1.0.2",
    author="Sasen Perera",
    packages=find_packages(),
    author_email="sas8.communications@gmail.com",
    description="A Toy Database System written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sas2k/ToyBase"
)