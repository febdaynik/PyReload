from setuptools import setup


def get_description():
	with open('README.md', 'r', encoding='utf-8') as readme_file:
		return readme_file.read()


version = "0.1~0"

long_description = "A module that allows you to make changes to a running python script and reload it"

setup(
	name="python-reload",
	version=version,
	license='MIT',
	author="Feb",
	author_email="drons_dron@mail.ru",

	description = long_description,
	long_description=get_description(),
	long_description_content_type = 'text/markdown',

	url = "https://github.com/febdaynik/PyReload",

	packages=["pyreload"],
)

