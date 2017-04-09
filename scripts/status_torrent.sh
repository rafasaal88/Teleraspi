user='pi'
pass='pi'

if (transmission-remote -n $user:$pass -l)
    then
    echo " "
else
    echo "Transmission no se encuentra activo actualmente"
fi
