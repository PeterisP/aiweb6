# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'
__version__ = '1.2.0'

import re, six
from publications.models import Publication, Type


# special character mapping
special_chars = (
	(r'\"{a}', 'ä'), (r'{\"a}', 'ä'), (r'\"a', 'ä'), (r'H{a}', 'ä'),
	(r'\"{A}', 'Ä'), (r'{\"A}', 'Ä'), (r'\"A', 'Ä'), (r'H{A}', 'Ä'),
	(r'\"{o}', 'ö'), (r'{\"o}', 'ö'), (r'\"o', 'ö'), (r'H{o}', 'ö'),
	(r'\"{O}', 'Ö'), (r'{\"O}', 'Ö'), (r'\"O', 'Ö'), (r'H{O}', 'Ö'),
	(r'\"{u}', 'ü'), (r'{\"u}', 'ü'), (r'\"u', 'ü'), (r'H{u}', 'ü'),
	(r'\"{U}', 'Ü'), (r'{\"U}', 'Ü'), (r'\"U', 'Ü'), (r'H{U}', 'Ü'),
	(r'{‘a}', 'à'), (r'\‘A', 'À'),
	(r'{‘e}', 'è'), (r'\‘E', 'È'),
	(r'{‘o}', 'ò'), (r'\‘O', 'Ò'),
	(r'{‘u}', 'ù'), (r'\‘U', 'Ù'),
	(r'{’a}', 'á'), (r'\’A', 'Á'),
	(r'{’e}', 'é'), (r'\’E', 'É'),
	(r'{’o}', 'ó'), (r'\’O', 'Ó'),
	(r'{’u}', 'ú'), (r'\’U', 'Ú'),
	(r'{\=a}', 'ā'), (r'{\=A}', 'Ā'), 
	(r'{\v{c}}', 'č'), (r'{\v{C}}', 'Č'), 
	(r'{\=e}', 'ē'), (r'{\=E}', 'Ē'), 
	(r'{\`g}', 'ģ'), (r'{\`G}', 'Ģ'), 
	(r'{\=i}', 'ī'), (r'{\=I}', 'Ī'), 
	(r'{\=\i}', 'ī'), (r'{\=\I}', 'Ī'), 
	(r'{\c{k}}', 'ķ'), (r'{\c{K}}', 'Ķ'), 
	(r'{\c{l}}', 'ļ'), (r'{\c{L}}', 'Ļ'), 
	(r'{\c{n}}', 'ņ'), (r'{\c{N}}', 'Ņ'), 
	(r'{\v{s}}', 'š'), (r'{\v{S}}', 'Š'),
	(r'{\=u}', 'ū'), (r'{\=U}', 'Ū'), 
	(r'{\v{z}}', 'ž'), (r'{\v{Z}}', 'Ž'),
	(r'\`a', 'à'), (r'\`A', 'À'),
	(r'\`e', 'è'), (r'\`E', 'È'),
	(r'\`u', 'ù'), (r'\`U', 'Ù'),
	(r'\`o', 'ò'), (r'\`O', 'Ò'),
	(r'\^o', 'ô'), (r'\^O', 'Ô'),
	(r'\ss', 'ß'),
	(r'\ae', 'æ'), (r'\AE', 'Æ'),

	(r'{{', '{'), (r'}}', '}'))

def parse(string):
	"""
	Takes a string in BibTex format and returns a list of BibTex entries, where
	each entry is a dictionary containing the entries' key-value pairs.

	@type  string: string
	@param string: bibliography in BibTex format

	@rtype: list
	@return: a list of dictionaries representing a bibliography
	"""

	# bibliography
	bib = []

	# make sure we are dealing with unicode strings
	if not isinstance(string, six.text_type):
		string = string.decode('utf-8')

	# replace special characters
	for key, value in special_chars:
		string = string.replace(key, value)

	# split into BibTex entries
	entries = re.findall(r'(?u)@(\w+)[ \t]?{[ \t]*([^,\s]*)[ \t]*,?\s*((?:[^=,\s]+\s*\=\s*(?:"[^"]*"|{(?:[^{}]*|{[^{}]*})*}|[^,}]*),?\s*?)+)\s*}', string)

	for entry in entries:
		# parse entry
		pairs = re.findall(r'(?u)([^=,\s]+)\s*\=\s*("[^"]*"|{(?:[^{}]*|{[^{}]*})*}|[^,]*)', entry[2])

		# add to bibliography
		bib.append({'type': entry[0].lower(), 'key': entry[1]})

		for key, value in pairs:
			# post-process key and value
			key = key.lower()
			if value and value[0] == '"' and value[-1] == '"':
				value = value[1:-1]
			if value and value[0] == '{' and value[-1] == '}':
				value = value[1:-1]
			if key not in ['booktitle', 'title']:
				value = value.replace('}', '').replace('{', '')
			value = value.strip()
			value = re.sub(r'\s+', ' ', value)

			# store pair in bibliography
			bib[-1][key] = value

	return bib


# mapping of months
MONTHS = {
	'jan': 1, 'january': 1,
	'feb': 2, 'february': 2,
	'mar': 3, 'march': 3,
	'apr': 4, 'april': 4,
	'may': 5,
	'jun': 6, 'june': 6,
	'jul': 7, 'july': 7,
	'aug': 8, 'august': 8,
	'sep': 9, 'september': 9,
	'oct': 10, 'october': 10,
	'nov': 11, 'november': 11,
	'dec': 12, 'december': 12}

def import_bibtex_data(bib):
	# container for error messages
	errors = {}

	# publication types
	types = Type.objects.all()

	# check for errors
	if not bib:
		errors['bibliography'] = "Couldn't parse bibliography"

	if not errors:
		publications = []

		# try adding publications
		for entry in bib:
			if 'title' in entry and \
			   'author' in entry and \
			   'year' in entry:
				# parse authors
				authors = entry['author'].split(' and ')
				for i in range(len(authors)):
					author = authors[i].split(',')
					author = [author[-1]] + author[:-1]
					authors[i] = ' '.join(author)
				authors = ', '.join(authors)

				# add missing keys
				keys = [
					'journal',
					'booktitle',
					'publisher',
					'institution',
					'url',
					'doi',
					'isbn',
					'keywords',
					'note',
					'abstract',
					'month']

				for key in keys:
					if not key in entry:
						entry[key] = ''

				# map integer fields to integers
				entry['month'] = MONTHS.get(entry['month'].lower(), 0)
				entry['volume'] = entry.get('volume', None)
				entry['number'] = entry.get('number', None)

				# determine type
				type_id = None

				for t in types:
					if entry['type'] in t.bibtex_type_list:
						type_id = t.id
						break

				if type_id is None:
					errors['bibliography'] = 'Type "' + entry['type'] + '" unknown.'
					break

				# add publication
				publications.append(Publication(
					type_id=type_id,
					citekey=entry['key'],
					title=entry['title'],
					authors=authors,
					year=entry['year'],
					month=entry['month'],
					journal=entry['journal'],
					book_title=entry['booktitle'],
					publisher=entry['publisher'],
					institution=entry['institution'],
					volume=entry['volume'],
					number=entry['number'],
					note=entry['note'],
					url=entry['url'],
					doi=entry['doi'],
					isbn=entry['isbn'],
					external=False,
					abstract=entry['abstract'],
					keywords=entry['keywords']))
			else:
				errors['bibliography'] = 'Make sure that the keys title, author and year are present.'
				break

	if not errors and not publications:
		errors['bibliography'] = 'No valid BibTex entries found.'

	msg = ''
	if not errors:
		try:
			# save publications
			for publication in publications:
				publication.save()
		except:
			msg = 'Some error occured during saving of publications.'
		else:
			if len(publications) > 1:
				msg = 'Successfully added ' + str(len(publications)) + ' publications.'
			else:
				msg = 'Successfully added ' + str(len(publications)) + ' publication.'

	return {'errors':errors, 'msg':msg, 'publications':publications}

