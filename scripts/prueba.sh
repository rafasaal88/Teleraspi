#!/bin/bash
#
# Comprobando terminacion de un comando
#


COMANDO="ls *.torrent"

if $COMANDO
    then
    echo "Existe"
else
    echo "No existe"
fi
