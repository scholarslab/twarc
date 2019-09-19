import sys
import re
with open(sys.argv[1], 'r') as infile, open("clean_"+sys.argv[1], 'w') as outfile:
   for line in infile:
       r = re.compile(r"\\[uU][0-z]{4}")
       outfile.write(r.sub('*',line))
