#!/bin/bash
cd bibs
echo "Bib 2 json"
python bib2yml.py lab.bib temp1.json
echo "Fixing yml formatting"
python fix.py temp1.yml temp2.yml
echo "Adding bib back into yml"
python fold.py lab.bib temp2.yml pubs.yml
echo "Copy into _data directory."
mv pubs.yml ../_data