#!/usr/bin/python3
import sys

# Procesamiento de la entrada del Mapper
for line in sys.stdin:
    line = line.strip()
    if line == '"CITING","CITED"':
        continue
    try:
        citing, cited = line.split(',')
        print("%s\t%s" % (cited, citing))
    except ValueError:
        sys.stderr.write(f"Skipping line (mapper): {line}\n")
        continue
