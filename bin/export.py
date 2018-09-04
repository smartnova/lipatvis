#!/usr/bin/env python

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

import pypandoc

drop_keys = set('rating note annote read'.split())
for i in range(10):
    drop_keys = drop_keys | set(['bdsk-file-' + str(i), 'bdsk-url-' + str(i)])

with open('survey.bib') as bib:
    db = bibtexparser.load(bib)
    for entry in db.entries:
        for key in drop_keys & entry.keys():
            del entry[key]

    keys = set()
    for entry in db.entries:
        keys = keys | entry.keys()
    # for key in sorted(keys): print(key)

with open('survey-export.bib', 'w') as bib:
    bib.write(BibTexWriter().write(db))
