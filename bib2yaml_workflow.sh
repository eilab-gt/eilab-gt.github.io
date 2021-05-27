#!/bin/bash
echo "Bib 2 yaml"
python bib2yml.py lab.bib temp1.yml
echo "Fixing yml formatting"
python fix.py temp1.yml temp2.yml
echo "Adding bib back into yml"
python fold.py lab.bib temp2.yml pubs.yml
echo "Copy into _data directory."
mv pubs.yml _data