#!/usr/bin/python3
import sys
from collections import defaultdict

patentes = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    cited, citings_str = line.split('\t')
    cited = int(cited)
    citings = map(int, citings_str.split(','))
    patentes[cited].extend(citings)

for cited in sorted(patentes.keys()):
    citinglist = sorted(set(patentes[cited]))  # Sort and remove duplicates
    citinglist_str = ','.join(map(str, citinglist))
    print(f"{cited}\t{citinglist_str}")


    
