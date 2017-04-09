#/bin/bash

TEMP=$(sensors | grep Package | awk '{print "Temperatura de la CPU: " $4}')
TEMP1=$(sensors | grep Core | awk '{print "Temperatura del núcleo " $2, $3}')
echo -e "$TEMP \n$TEMP1"
