import os
from termcolor import colored
import telebot
# from random import randint, random
import random
from datetime import datetime, timedelta
import time
import pytz

telegram_token = "SEU TOKEN AQUI"
chat_id = "ID DO CHAT AQUI"

tz = pytz.timezone('America/Sao_Paulo')

bot = telebot.TeleBot(telegram_token,parse_mode='HTML')

####################
#  CONFIGURAR AQUI #
####################

tempo_possivel_msg = random.randint(35,40) # Tempo em segundos primeiro valor é o minimo, segundo valor é o maximo. (Ex: Vai gerar um numero entre 45 e 70)
tempo_espera = 4 # Tempo que o bot vai enviar a mensagem de green.
tempo_proxima_msg = 120 # Em segundos para enviar possivel sinal depois de dar green.

# Definir o número mínimo e máximo de estrelas
min_stars = 3
max_stars = 4

link_afiliado = "LINK DA PLATAFORMA"
link_jogo = "LINK DA PLATAFORMA"
mensagem_possivel = '🌟Possíveis entradas detectadas\n\nSINAIS APENAS PARA O SITE DA 7KBET\n <a href="'+link_afiliado+'">🔗 Cadastre-se aqui</a>\n\n 💰 Banca recomendada, acima de R$30,00'

os.system('title Zety')
print(colored('\n[Info]', 'dark_grey'), colored('Developer:', 'white'), colored('zety#7505', 'cyan'))
print(colored('\n[Info]', 'dark_grey'), colored('Bot Iniciado com sucesso', 'green'))

while True:

  line = "🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n"
  empty_spaces = [i for i in range(25) if line[i] == "🟦"]
  num_stars = random.randint(min_stars, max_stars)
  if len(empty_spaces) >= num_stars:
    for i in range(num_stars):
      index = random.choice(empty_spaces)
      line = line[:index] + "⭐" + line[index+1:]
      empty_spaces.remove(index)
  else:
    for i in range(len(empty_spaces)):
      index = empty_spaces[i]
      line = line[:index] + "⭐" + line[index+1:]
    for i in range(num_stars - len(empty_spaces)):
      index = random.choice([x for x in range(25) if x not in empty_spaces])
      line = line[:index] + "⭐" + line[index+1:]

  bot.send_message(chat_id=chat_id, text=mensagem_possivel, disable_web_page_preview=True)

  time.sleep(tempo_possivel_msg)

  date = datetime.now(tz)
  date_futur = date + timedelta(minutes=tempo_espera)
  date_futur_format = date_futur.strftime('%H:%M')

  bot.send_message(chat_id=chat_id, text='🔔 Entrada Cofirmada 🔔\n\n💣 Minas: 3\n🎯 Nº de tentativas: 2\n🕗 Sinal Valido até: ' + date_futur_format + '\n\n🔗 Cadastre-se aqui: <a href="'+link_jogo+'">Entrar</a> \n\n' + line.strip(), disable_web_page_preview=True)

  time.sleep(tempo_espera*60)
  date_now = datetime.now(tz)
  date_now_format = date_futur.strftime('%H:%M')
  bot.send_message(chat_id=chat_id, text='🔹 Sinal Finalizado 🔹\n\n🕑 Finalizado às: '+date_now_format+'\n✅✅✅ GREEN ✅✅✅')
  time.sleep(tempo_proxima_msg)
