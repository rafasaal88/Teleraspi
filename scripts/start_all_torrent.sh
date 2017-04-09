user='pi'
pass='pi'

if (transmission-remote -n $user:$pass -t all -s)
    then
    echo "Todos los torrents se han iniciado"
else
    echo "Transmission no se encuentra activo"
fi
