from setuptools import setup, find_packages

# Read in the requirements.txt file
with open("requirements.txt") as f:
    requirements = []
    for library in f.read().splitlines():
        requirements.append(library)

setup(
    name="dataexplorer",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
)
