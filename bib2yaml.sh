#!/bin/bash
echo "Bib 2 yaml"
python bib2yml.py $1 temp1.yml
echo "Fixing yml formatting"
python fix.py temp1.yml temp2.yml
echo "Adding bib back into yml"
python fold.py lab.bib temp2.yml $2
echo "Copy into _data directory."