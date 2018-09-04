#!/usr/bin/env python

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

import pypandoc

with open('survey.bib') as bib:
    db = bibtexparser.load(bib)
    for item in db.entries:
        if item.get('address', False) and item.get('location', False):
            del item['address']
        annote = item.get('annote', False)
        if annote:
            item['annote'] = pypandoc.convert_text(annote, 'tex', format='md')
        item['citeno'] = '0'
        keywords = item.get('keywords', False)
        if keywords:
            item['categories'] = keywords
            del item['keywords']

with open('misc/survey-annote.bib', 'w') as bib:
    bib.write(BibTexWriter().write(db))
