import telebot
import time
import urllib
import platform
from subprocess import Popen,PIPE,STDOUT,call
from telebot import types
import os
import subprocess
import credenciales

API_TOKEN = credenciales.API_TOKEN #token del bot, el id se encuentra en el modulo credenciales
bot = telebot.TeleBot(API_TOKEN) #abrimos una conexión con el servidor
admin = credenciales.admin
#knownUsers = [] #todo: save these in a file,
userStep = {}   #so they won't reset every time the bot restarts

################################MENUS DEL BOT##############################
def menu_principal():
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Sistema')
	itembtnb = types.KeyboardButton('Torrents')
	itembtnc = types.KeyboardButton('Archivos')
	markup.row(itembtna)
	markup.row(itembtnb)
	markup.row(itembtnc)
	bot.send_message(admin, "Selecciona una opción:", reply_markup=markup)

def menu_cancelar():
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Cancelar')
	itembtnz = types.KeyboardButton('Volver al menu principal')
	markup.row(itembtna)
	markup.row(itembtnz)
	bot.send_message(admin, "Envia el fichero:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "/start")
def command_sistema(m):
	bot.send_message(admin, "Bienvenido a Teleraspi")
	menu_principal()

menu_principal()

@bot.message_handler(func=lambda message: message.text == "Volver al menu principal")
def command_sistema(m):
	menu_principal()

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text':
                print ("[" + str(admin) + "] : " + m.text)
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.


@bot.message_handler(func=lambda message: message.text == "Sistema")
def command_sistema(m):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Información del dispositivo')
	itembtnb = types.KeyboardButton('Consumo de RAM')
	itembtnc = types.KeyboardButton('Temperatura de la CPU')
	itembtnd = types.KeyboardButton('Procesos')
	itembtne = types.KeyboardButton('Reiniciar')
	itembtnf = types.KeyboardButton('Apagar')
	itembtnz = types.KeyboardButton('Volver al menu principal')
	markup.row(itembtna)
	markup.row(itembtnb, itembtnc)
	markup.row(itembtnd, itembtne)
	markup.row(itembtnf, itembtnz)
	bot.send_message(admin, "Selecciona una opción:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Archivos")
def command_sistema(m):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Enviar')
	itembtnz = types.KeyboardButton('Volver al menu principal')
	markup.row(itembtna)
	markup.row(itembtnz)
	bot.send_message(admin, "Selecciona una opción:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Torrents")
def command_sistema(m):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Añadir torrent')
	itembtnb = types.KeyboardButton('Estado actual de las descargas')
	itembtnc = types.KeyboardButton('Iniciar todos los torrents')
	itembtne = types.KeyboardButton('Parar todos los torrents')
	itembtnz = types.KeyboardButton('Volver al menu principal')
	markup.row(itembtna, itembtnb)
	markup.row(itembtnc, itembtne)
	markup.row(itembtnz)
	bot.send_message(admin, "Selecciona una opción:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Añadir torrent")
def command_sistema(m):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Enviar torrent')
	itembtnz = types.KeyboardButton('Volver al menu principal')
	markup.row(itembtna)
	markup.row(itembtnz)
	bot.send_message(admin, "Selecciona una opción:", reply_markup=markup)

def getUserStep(uid):
	if uid in userStep:
		return userStep[uid]
	else:
		knownUsers.append(uid)
		userStep[uid] = 0
		print ("Nuevo usuario detectado que todavia no ha usado \"/start\"")

def next_step_handler(uid):
	if uid not in userStep:
		userStep[uid] = 0
	return userStep[uid]

##############################################################################
######################### FUNCIONES DEL BOT ##################################
##############################################################################

#################### Funciones del sistema ###################################


@bot.message_handler(func=lambda message: message.text == "Información del dispositivo")
def command_sistema(m):
	all_data="Nombre: " + str(platform.uname()[1]) + "\n" + "Sistema Operativo: " + str(platform.uname()[0]) + "\n" + "Arquitectura: " + str(platform.machine()) + "\n" + "CPU: " + str(platform.processor()) + "\n" + "Distribucion: " + str(platform.linux_distribution()) + "\n" + "Kernel: " + str(platform.release()) + "\n"
	bot.send_message(admin, all_data)




@bot.message_handler(func=lambda message: message.text == "Consumo de RAM")
def command_ram(m):
	os.system("sh scripts/ram.sh >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)




@bot.message_handler(func=lambda message: message.text == "Temperatura de la CPU")
def command_cpu(m):
	os.system("sh scripts/cpu.sh >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)




@bot.message_handler(func=lambda message: message.text == "Procesos")
def command_cpu(m):
	os.system("ps -a | awk {'print $1, $4'} >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)





@bot.message_handler(func=lambda message: message.text == "Reiniciar")
def command_reboot(m):
	bot.send_message("Reiniciando dispositivo...")
	os.system("reboot")




@bot.message_handler(func=lambda message: message.text == "Apagar")
def command_shutdown(m):
	os.system("shutdown -P 00")
	bot.send_message("Apagando dispositivo...")




######################Funciones de archivos###############################



@bot.message_handler(func=lambda message: message.text == "Enviar")
def command_descargar(m):
	cid = m.chat.id
	if cid == admin:
		bot.send_chat_action(cid, 'typing')
		menu_cancelar()
		userStep[cid] = 'enviar_archivo'

	else:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "No tienes permiso para hacer esto")




@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'enviar_archivo', content_types=['document'])
def step_descargar(m):
	cid = m.chat.id
	userStep[cid] = 0
	name = m.document.file_name
	info = bot.get_file(m.document.file_id)
	bot.send_chat_action(cid, 'typing')
	bot.send_message(cid, "Descargando: " + name)
	downloaded_file = bot.download_file(info.file_path)
	with open("ficheros/"+name, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.send_chat_action(cid, 'typing')
	#proc=Popen("", shell=True, stdout=PIPE, )
	bot.send_message(cid, "Fichero recibido")
	os.system("sh scripts/clasificar.sh >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)
	menu_principal()




@bot.message_handler(func=lambda message: message.text == "Cancelar")
def command_cancelar(m):
	cid = m.chat.id
	uid = m.from_user.id

	if next_step_handler(cid) != 0:
		userStep[cid] = 0
		bot.send_chat_action(cid, 'typing')
		menu_principal()
		bot.send_message(cid, "Comando cancelado")

	else:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "No hay nada que cancelar")





########################################################################
######################Funciones de torrent##############################
########################################################################



##Funciones para recoger torrent enviado por el usuario#################
@bot.message_handler(func=lambda message: message.text == "Enviar torrent")
def command_descargar(m):
	cid = m.chat.id
	if cid == admin: #Comprobamos que el usuario es el admin
		bot.send_chat_action(cid, 'typing')
		menu_cancelar()
		userStep[cid] = 'enviar_torrent' #Llamamos a la siguiente funcion

	else:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "No tienes permiso para hacer esto")


@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'enviar_torrent', content_types=['document'])
def step_descargar(m):
	name = m.document.file_name ##Recogemos el nombre del fichero
	info = bot.get_file(m.document.file_id) ##Comenzamos la descarga del fichero
	bot.send_chat_action(admin, 'typing')
	bot.send_message(admin, "Descargando: " + name)
	downloaded_file = bot.download_file(info.file_path)
	with open("scripts/torrent/"+name, 'wb') as new_file: #escribimos el fichero que hemos descargado en la ruta
		new_file.write(downloaded_file)
	bot.send_chat_action(admin, 'typing')
	bot.send_message(admin, "Fichero recibido") #enviamos un mensaje de que el fichero ha sido recibido
	os.system("sh scripts/add_torrent.sh >> temp.txt") #llamamos al script para que añada el torrent a transmission si es posible.
	fichero = open('temp.txt')
	contenido=fichero.read() #guardamos la salida del script en la variable contenido
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido) #enviamos la salida del script al usuario
	menu_principal()
########################################################################


@bot.message_handler(func=lambda message: message.text == "Estado actual de las descargas")
def command_cpu(m):
	os.system("sh scripts/status_torrent.sh >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)


@bot.message_handler(func=lambda message: message.text == "Iniciar todos los torrents")
def command_cpu(m):
	os.system("sh scripts/start_all_torrent.sh >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)


@bot.message_handler(func=lambda message: message.text == "Parar todos los torrents")
def command_cpu(m):
	os.system("sh scripts/stop_all_torrent.sh >> temp.txt")
	fichero = open('temp.txt')
	contenido=fichero.read()
	fichero.close()
	os.system("rm temp.txt")
	bot.send_message(admin, contenido)


bot.polling()
