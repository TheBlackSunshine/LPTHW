try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Expanding the functionality of ex48_advanced_input',
	'author': 'Adam Matheson',
	'url': 'www.adammatheson.com/Projects',
	'download_url': 'www.adammatheson.com/projects/ex49_sentence_parsing',
	'author_email': 'adam.matheson@ntlworld.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex49_sentence_parsing'],
	'scripts': [],
	'name': 'ex49_sentence_parsing',
}

setup(**config)