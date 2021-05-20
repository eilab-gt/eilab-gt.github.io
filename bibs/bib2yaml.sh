#!/bin/bash
Rscript bib2json.r $1 temp.json
python json2yaml.py temp.json temp.yml
python fix.py temp.yml $2