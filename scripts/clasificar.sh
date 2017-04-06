#!/bin/bash
dirimg="imagenes/"
dirdoc="documentos/"
dirtor="torrents/"
dirarc="archivos/"
dirmus="musica/"

cd ficheros/
# imagenes

ls -1 *.jpg *.png *.bmp *.gif | while read archivo
do
   echo "La imagen $archivo ha sido copiada a la carpeta imagenes"
   mkdir -p "$dirimg"
   mv "$archivo" "$dirimg"
done

ls -1 *.pdf *.docx *.txt *.doc *.odt *.odf *.pps *.ppt *.pot | while read archivo
do
   echo "El documento $archivo ha sido copiada a la carpeta documentos"
   mkdir -p "$dirdoc"
   mv "$archivo" "$dirdoc"
done

ls -1 *.torrent | while read archivo
do
   echo "El torrent $archivo ha sido copiado a la carpeta torrent"
   mkdir -p "$dirtor"
   mv "$archivo" "$dirtor"
done

ls -1 *.mp3 | while read archivo
do
   echo "$archivo ha sido copiado a la carpeta musica"
   mkdir -p "$dirmus"
   mv "$archivo" "$dirmus"
done

ls -1 *.* | while read archivo
do
   echo "El archivo $archivo ha sido copiado a la carpeta archivos"
   mkdir -p "$dirarc"
   mv "$archivo" "$dirarc"
done
