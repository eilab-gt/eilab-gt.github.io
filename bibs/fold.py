import re
import sys
import codecs

###
# argv[1]: input bib file
# argv[2]: input yaml file
# argv[3]: output yaml file
###

### Store a hash table of index: bib entry
bibs_hash = {}

### Get all the bibs into the bib_hash
bib = ''
for line in codecs.open(sys.argv[1], 'r', 'utf-8'):
   if '@' in line:
      # Ending a previous bib and starting a new one
      if len(bib) > 0:
         # get the index
         match = re.match(r'\@[a-zA-Z]+\{([\w\:\-\_]+),', bib, re.DOTALL)
         if match is not None and len(match.groups()) > 0:
            # If we have an index, then we are done with an old bib
            index = match.groups()[0]
            bibs_hash[index] = bib.strip()
      # Start a new bib
      bib = line
   else: 
      # continuing a bib
      bib = bib + line

yaml = ''
for line in codecs.open(sys.argv[2], 'r', "utf-8"):
   # Add the line to the yaml
   yaml = yaml + line
   # Look for a bibtexkey
   match = re.match(r'([\s]*)BIBTEXKEY\:[\s]+([\w\:\-\_]+)', line)
   if match is not None and len(match.groups()) > 1:
      # We just found a BIBTEXKEY with a valid index
      spaces = match.groups()[0]
      index = match.groups()[1]
      # Get the original bib entry
      bib = bibs_hash[index].strip()
      # Insert the original bib into the yaml
      yaml = yaml + ' '*(len(spaces)) + 'BIBTEX: |\n' 
      for b in bib.split('\n'):
         yaml = yaml + ' '*(len(spaces)+2) + b.strip() + '\n'

with codecs.open(sys.argv[3], 'w', "utf-8") as f:
   f.write(yaml.decode('utf-8', 'ignore'))
