from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="python-terraform-registry",
    version="0.1.0",
    description="Python package to interact with the Terraform Registry.",
    long_description=readme,
    author="Patrick Lubach",
    author_email="plubach1994@gmail.com",
    url="https://github.com/patricklubach/python-terraform-registry",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
