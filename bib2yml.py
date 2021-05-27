from pybtex.database import parse_file
import sys
import codecs


bib_data = parse_file(sys.argv[1])
bib_data.to_file(sys.argv[2], "yaml")
