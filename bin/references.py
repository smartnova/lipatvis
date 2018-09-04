#!/usr/bin/env python

import re

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

import pypandoc

list_sep = re.compile('[;,] *')
category_prefix = re.compile('[a-z]+:')

with open('survey.bib') as bib:
    db = bibtexparser.load(bib)

sections = dict()
articles = dict()

for entry in db.entries:
    id = entry['ID']
    categories = list_sep.split(entry.get('categories', ''))
    # articles[id] = categories
    articles[id] = sorted([re.sub(category_prefix, '', category) for category in categories
                           if len(category) > 0 and not category[0].isnumeric()])
    for category in categories:
        if len(category) > 0  and category[0].isnumeric():
            sections[category] = sections.get(category, set([])) | set([id])

with open('misc/references-body.tex', 'w') as tex:
    for section in sorted(sections.keys()):
        tex.write(r'\begin {refsection}' + '\n')
        tex.write(r'\section [' + section + '] {' + section + '}' + '\n\n')
        tex.write(r'\begin {itemize}' + '\n')
        for entry in sections[section]:
            tex.write(r'\item \cite {' + entry + r'}:' + '\n')
            tex.write('    ' + ', '.join(articles[entry]) + '\n')
            #for tag in articles[entry]:
            #    tex.write(r'    \index {' + tag + '}\n')
            tex.write('\n\n')
        tex.write(r'\end {itemize}' + '\n')
        tex.write('\printbibliography\n')
        tex.write(r'\end {refsection}' + '\\pagebreak\n\n')
