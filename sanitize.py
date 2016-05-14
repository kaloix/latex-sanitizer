#!/usr/bin/env python3

import fileinput
import sys


REPLACE = {
	'“': '``',
	'”': '\'\'',
	'’': '\'',
	'\\': '\\textbackslash ',
	'*': '\\textasteriskcentered ',
	'_': '\\_',
	'#': '\\#',
	'$': '\\$',
	'%': '\\%',
	'{': '\\{',
	'}': '\\}',
	'&': '\\&',
	'…': '\\dots ',
	'~': '\\~{}',
	'^': '\\^{}'}
DELETE = ''

def main():
	replaced, deleted = set(), set()
	for line in fileinput.input():
		line, replaced_ = replace(line, REPLACE)
		replaced.update(replaced_)
		line, deleted_ = delete(line, DELETE)
		deleted.update(deleted_)
		sys.stdout.write(line)
	print('Replaced characters: {}'.format(' '.join(sorted(replaced))), file=sys.stderr)
	print('Deleted characters: {}'.format(' '.join(sorted(deleted))), file=sys.stderr)
	

def replace(text, table):
	text = text.translate(table)
	replaced = set(text) & set(table)
	return text, replaced

def delete(text, illegals):
	table = {char: None for char in illegals}
	text = text.translate(table)
	return text, ''

if __name__ == '__main__':
	main()
