# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.

TOKEN = '384967572:AAGdrllBDim9TcyPRAnupNnsbkILJMDOJI0' # Nuestro tokken del bot (el que @BotFather nos dió).

text_messages = {

	'hello':
		u'Hello!\n\n'
		u'My name is Fezzik and I am here to help you in many task you even do not imagine.\n'
		u'Just check my command list typing /commands or check the buttons available below.\n'
		u'And nice to meet you!'

#	'info':
#        	u'My name is Fezzik,\n'
#        	u'I am a bot created to serve yourself in the most of task I am able\n'
#        	u'However, I am under development, so perhaps I need some changes to do my best.\n'
#        	u'Suggestions are always welcome, just send them to me using the command /suggest!',

#	'command_list':
#		u'The commands available right now are:\n\n'
#		u'\t/help\n'
#		u'\t/info\n'
#		u'\t/commands\n'
}


bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

@bot.message_handler(commands=['info', 'help'])
def command_help(message): # Definimos una función que resuleva lo que necesitemos.
	bot.reply_to(message, text_messages['hello'])
	return

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener)

bot.polling(none_stop=True)
