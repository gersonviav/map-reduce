#!/usr/bin/python3
import sys

# Procesamiento de la entrada del Mapper
for line in sys.stdin:
    line = line.strip()
    persona, tienda, gasto = line.split(';')
    print(f"{persona};{tienda}\t{gasto}")
