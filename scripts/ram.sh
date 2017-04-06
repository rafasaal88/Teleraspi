#/bin/bash
TOTAL=$(free -m | grep 'Mem:' | awk {'print $2'})
FREE=$(free -m | grep 'Mem:' | awk {'print $4'})
STOTAL=$(free -m | grep 'Swap:' | awk {'print $2'})
SFREE=$(free -m | grep 'Swap:' | awk {'print $4'})

echo "RAM disponible: $TOTAL MB"
echo "RAM libre: $FREE MB"
echo "Swap disponible: $STOTAL MB"
echo "Swap libre: $SFREE MB"
