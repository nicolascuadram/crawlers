#!/bin/bash

archivo_original="post150.md"  # Cambia esto por el nombre de tu archivo
cantidad=2000                      # Número de copias que quieres hacer

for i in $(seq 1 $cantidad); do
    cp "$archivo_original" "${archivo_original%.*}_$i.${archivo_original##*.}"
done
