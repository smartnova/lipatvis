#!/usr/bin/env python

import re

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

category_sep = re.compile('[,;]  *')
section_rx = re.compile(r'[0-9][0-9]*\.')

with open('survey.bib') as bib:
    db = bibtexparser.load(bib)
    for entry in db.entries:
        categories = entry.get('categories', False)
        if categories:
            categories = category_sep.split(entry.get('categories', ''))
            entry['categories'] = '; '.join(categories)
            entry['n_secs'] = str(len(list(filter(lambda s: section_rx.match(s), categories))))

with open('misc/svy.bib', 'w') as bib:
    bib.write(BibTexWriter().write(db))
