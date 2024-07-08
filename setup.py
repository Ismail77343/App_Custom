from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alfrasapp/__init__.py
from alfrasapp import __version__ as version

setup(
	name="alfrasapp",
	version=version,
	description="Alfrasapp",
	author="ismail haimi",
	author_email="himiismail123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
