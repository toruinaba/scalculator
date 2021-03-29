from setuptools import setup, find_packages

setup(
    name="scalculator",
    version="0.0.1",
    description="",
    author="dtkoushi",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
)
