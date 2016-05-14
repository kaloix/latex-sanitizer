#!/usr/bin/env python3

import fileinput
import string
import sys

DELETE = ''
REPLACE = {'“': '``',
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


def main():
    all_deleted, all_replaced, all_specials = set(), set(), set()
    for line in fileinput.input():
        line, deleted = delete(line, DELETE)
        all_deleted.update(deleted)
        line, replaced = replace(line, REPLACE)
        all_replaced.update(replaced)
        specials = special_characters(line)
        all_specials.update(specials)
        sys.stdout.write(line)
    print('Deleted characters: {}'.format(' '.join(sorted(all_deleted))),
          file=sys.stderr)
    print('Replaced characters: {}'.format(' '.join(sorted(all_replaced))),
          file=sys.stderr)
    prtxt = 'Remaining special characters: {}'
    print(prtxt.format(' '.join(sorted(all_specials))),
          file=sys.stderr)


def delete(text, illegals):
    deleted = {char for char in illegals if char in text}
    table = {char: None for char in illegals}
    text = text.translate(str.maketrans(table))
    return text, deleted


def replace(text, table):
    replaced = {char for char in table if char in text}
    text = text.translate(str.maketrans(table))
    return text, replaced


def special_characters(text):
    return {char for char in text if char not in string.printable}


if __name__ == '__main__':
    main()
