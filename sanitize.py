#!/usr/bin/env python3

import fileinput
import sys

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
DELETE = ''


def main():
    all_replaced, all_deleted = set(), set()
    for line in fileinput.input():
        line, replaced = replace(line, REPLACE)
        all_replaced.update(replaced)
        line, deleted = delete(line, DELETE)
        all_deleted.update(deleted)
        sys.stdout.write(line)
    print('Replaced characters: {}'.format(' '.join(sorted(all_replaced))),
          file=sys.stderr)
    print('Deleted characters: {}'.format(' '.join(sorted(all_deleted))),
          file=sys.stderr)


def replace(text, table):
    replaced = {char for char in table if char in text}
    text = text.translate(str.maketrans(table))
    return text, replaced


def delete(text, illegals):
    deleted = {char for char in illegals if char in text}
    table = {char: None for char in illegals}
    text = text.translate(str.maketrans(table))
    return text, deleted


if __name__ == '__main__':
    main()
