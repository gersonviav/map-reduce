#!/usr/bin/python3
import sys

current_key = None
current_sum = 0.0
current_count = 0

# Procesamiento de la entrada del Reducer
for line in sys.stdin:
    line = line.strip()
    key, parcial_sum, parcial_count = line.split('\t')
    parcial_sum = float(parcial_sum)
    parcial_count = int(parcial_count)
    
    if current_key is None:
        current_key = key
    
    if key == current_key:
        current_sum += parcial_sum
        current_count += parcial_count
    else:
        persona, tienda = current_key.split(';')
        print(f"{persona};{tienda};{current_sum / current_count:.2f}")
        current_key = key
        current_sum = parcial_sum
        current_count = parcial_count

# Imprime el promedio para la última clave
if current_key:
    persona, tienda = current_key.split(';')
    print(f"{persona};{tienda};{current_sum / current_count:.2f}")
