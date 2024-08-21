#!/usr/bin/python3
import sys
from collections import defaultdict

# Procesamiento de la entrada del Combiner
patentes = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    cited, citing = line.split(',')
    cited = int(cited)
    citing = int(citing)
    patentes[cited].append(citing)

for cited, citings in patentes.items():
    citings_str = ','.join(map(str, citings))
    print(f"{cited}\t{citings_str}")
