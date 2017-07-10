try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'Adam Matheson',
	'url': 'www.adammatheson.com/Projects',
	'download_url': 'www.adammatheson.com/projects/My_Project',
	'author_email': 'adam.matheson@ntlworld.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname',
}

setup(**config)