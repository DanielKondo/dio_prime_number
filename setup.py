from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="prime_number_package",
    version="0.0.1",
    author="Daniel Kondo",
    author_email="kondo.yoshie.daniel@gmail.com",
    description="A small package to check whether a number is prime",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanielKondo/dio_prime_number.git",
    packages=find_packages(),
    install_requires=requirements,
    pyhton_requires='>=3.8',
)