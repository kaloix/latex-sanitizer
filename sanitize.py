#!/usr/bin/python3

import string
import sys

# read stdin
text = sys.stdin.read()

# replace printable characters
replacement = [
	('“', '``'),
	('”', '\'\''),
	('’', '\''),
	('\\', '\\textbackslash '),
	('*', '\\textasteriskcentered '),
	('_', '\\_'),
	('#', '\\#'),
	('$', '\\$'),
	('%', '\\%'),
	('{', '\\{'),
	('}', '\\}'),
	('&', '\\&'),
	('…', '\\dots '),
	('~', '\\~{}'),
	('^', '\\^{}')
]
illegal = set()
for old, new in replacement:
	if old in text:
		text = text.replace(old, new)
		illegal.add(old)
if illegal:
	print('Replaced characters: "{}"'.format(''.join(illegal)), file=sys.stderr)

# delete special characters
allowed = set(string.ascii_letters)
allowed |= set(string.digits)
allowed |= set(string.punctuation)
allowed.add('\n')
illegal = set(text) - allowed
for char in illegal:
	text = text.replace(char, ' ')
if illegal:
	print('Deleted characters: "{}"'.format(''.join(illegal)), file=sys.stderr)

# write stdout
print(text)
