user='pi'
pass='pi'

if (transmission-remote -n $user:$pass -t all -S)
    then
    echo "Todos los torrents se han parado"
else
    echo "Transmission no se encuentra activo"
fi
