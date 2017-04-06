user='pi'
pass='pi'

cd scripts/torrent/

COMANDO="ls *.torrent"

if $COMANDO
    then
    transmission-remote -n $user:$pass -a *.torrent
    rm *.torrent
    echo "Torrent añadido"
else
    rm *.*
    echo "El fichero que has mandado no es un torrent"
fi
