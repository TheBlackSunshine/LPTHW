try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Experimenting with Python automated testing',
	'author': 'Adam Matheson',
	'url': 'www.adammatheson.com/Projects',
	'download_url': 'www.adammatheson.com/projects/ex47_automated_testing',
	'author_email': 'adam.matheson@ntlworld.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47_automated_testing'],
	'scripts': [],
	'name': 'ex47_automated_testing',
}

setup(**config)