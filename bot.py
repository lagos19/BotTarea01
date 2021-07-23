import telebot
import time

from telebot.types import Message

bot = telebot.TeleBot("1906701890:AAE1V60meqDHUUDNtJSgsFR4ibb4x366ILE")

@bot.message_handler(commands=["start" ])
def start (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3) 
    bot.reply_to(mensaje, "Hola,Un gusto saludarte.")

@bot.message_handler(commands=["comoestas"])
def comoestas (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3) 
    bot.reply_to(mensaje, "Me siento muy bien. \nGracias")
    
@bot.message_handler(commands=["cualestunombre"]) 
def cualestunombre (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3) 
    bot.reply_to (mensaje, "Mi nombre es BotLagos. ¿En que puedo ayudarte?")

@bot.message_handler(commands=["cualestuedad"]) 
def cualestuedad (mensaje):
     bot.send_chat_action (1500506100, 'typing')
     time.sleep(3)
     bot.reply_to(mensaje, "Me siento joven y eso es lo importante")   

@bot.message_handler(commands=["dedondeeres"]) 
def dedondeeres (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3)
    bot.reply_to(mensaje, "No tengo una respuesta para eso .. Dime te puedo ayudar en otra cosa?")

@bot.message_handler(commands=["cualestuedad"]) 
def cualestuedad (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3)
    bot.reply_to(mensaje, "No tengo una edad definida por ende no cumplo años, mi dueño puede apagarme cuando quiera")

bot.polling()