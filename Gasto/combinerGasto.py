#!/usr/bin/python3
import sys

current_key = None
current_sum = 0.0
current_count = 0

# Procesamiento de la entrada del Combiner
for line in sys.stdin:
    line = line.strip()
    key, gasto = line.split('\t')
    gasto = float(gasto)
    
    if current_key is None:
        current_key = key
    
    if key == current_key:
        current_sum += gasto
        current_count += 1
    else:
        print(f"{current_key}\t{current_sum}\t{current_count}")
        current_key = key
        current_sum = gasto
        current_count = 1

# Emisión de la última clave
if current_key:
    print(f"{current_key}\t{current_sum}\t{current_count}")
