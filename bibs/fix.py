import sys
import re

count = 0    # count the entries and use it as an index value

with open(sys.argv[2], "w") as outfile:
   outfile.write("bibs:\n")
   with open(sys.argv[1], "r") as infile:
      for line in infile:
         #line = line.replace('~', ' ')
         line = re.sub(r'[\{\}\^\\]', '', line)
         line = re.sub(r'\\\'', '', line)
         if line[0] == '-':
            # begining of record
            # Always seem to be `- AUTHOR:`
            # Replace with `- bib:` and move author to the next line
            outfile.write('  - bib: "'+str(count)+'"\n')
            outfile.write('    '+line[1:].strip()+'\n')
            count = count + 1
         elif line.strip()[0] == '-':
            # This line is indented and has a dash
            # Assume it's a name
            # Deal with bibtex inverted names
            # Remove tildes
            names = line.strip()[1:].split(',')
            name = ''
            if len(names) > 1:
               # flip the order
               name = ' '.join([names[1].strip(), names[0].strip()])
            else:
               name = names[0]
            outfile.write('      - name: "'+name.strip()+'"\n')
         else:
            # This line should be fine as is
#            if line.count(':') > 1:
#               line = re.sub(r'([\s]+[A-Z]+:\s)([\w\s:\-\(\),]+\Z)', r'\1"\2"', line[:-1])
#            else:
            line = line[:-1]
            outfile.write('  '+line+'\n')