user='pi'
pass='pi'

cd scripts/torrent/


if (ls *.torrent)
    then
      if (transmission-remote -n $user:$pass -a *.torrent)
        then
          rm *.torrent
          echo "Torrent añadido"
      else
          echo "El torrent no se ha podido añadir, transmission no se encuentra activo"
          rm *.torrent
      fi
else
    rm *.*
    echo "El fichero que has mandado no es un torrent"
fi
