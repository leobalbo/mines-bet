import os
from termcolor import colored
import telebot
from random import randint
from datetime import datetime, timedelta
import time

telegram_token = "6222047362:AAF6ScZQFK-IQAQ6hB1RL-QNFjZpugO7oa0"
chat_id = "-1001926927184"


bot = telebot.TeleBot(telegram_token,parse_mode='HTML')

####################
#  CONFIGURAR AQUI #
####################

tempo_possivel_msg = randint(35,40) # Tempo em segundos primeiro valor é o minimo, segundo valor é o maximo. (Ex: Vai gerar um numero entre 45 e 70)
tempo_espera = 4 # Tempo que o bot vai enviar a mensagem de green.
tempo_proxima_msg = 120 # Em segundos para enviar possivel sinal depois de dar green.
link_afiliado = "https://bit.ly/b1betminesb1bet"
link_jogo = "https://www.b1.bet/#/game/casino?st=Mines&p=0&t=1000&g=spribe-1725-mines&f=false"
mensagem_possivel = '🌟Possíveis entradas detectadas\n\nSINAIS APENAS PARA O SITE DA B1BET\n <a href="'+link_afiliado+'">🔗 Cadastre-se aqui</a>\n\n 💰 Banca recomendada, acima de R$20,00'

quantia_mensagem = 25 # Quantia de mensagem abaixo -1 (Ex: deu 26 linhas você tira 1 linha e da 25 não apagar a linha)
lista_mensagem = [
                    "🟦🟦🟦⭐🟦\n🟦⭐🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦⭐🟦🟦🟦",
                    "🟦⭐🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦⭐⭐🟦🟦\n⭐🟦🟦🟦🟦",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n⭐🟦🟦🟦⭐\n🟦🟦🟦🟦🟦\n🟦🟦🟦⭐🟦",
                    "🟦⭐🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦⭐⭐🟦🟦\n🟦🟦🟦🟦🟦",
                    "⭐🟦🟦🟦⭐\n🟦🟦🟦🟦🟦\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n🟦⭐🟦🟦🟦",
                    "🟦🟦⭐🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦🟦🟦⭐🟦",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦⭐🟦\n⭐🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦⭐🟦⭐🟦",
                    "🟦🟦🟦⭐⭐\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦🟦🟦\n⭐🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦🟦🟦🟦⭐",
                    "🟦🟦🟦🟦🟦\n⭐🟦🟦⭐⭐\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦⭐",
                    "🟦🟦🟦🟦⭐\n🟦🟦🟦🟦🟦\n⭐🟦🟦🟦🟦\n🟦⭐⭐🟦🟦\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦⭐🟦🟦🟦",
                    "⭐🟦🟦🟦🟦\n🟦🟦🟦⭐⭐\n⭐🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦🟦🟦\n⭐🟦🟦⭐🟦\n🟦🟦🟦🟦⭐\n🟦🟦🟦🟦🟦\n⭐🟦🟦🟦🟦",
                    "🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦\n🟦⭐🟦⭐🟦",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦⭐⭐\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦🟦🟦\n🟦⭐🟦🟦⭐\n🟦🟦🟦🟦🟦\n🟦⭐🟦🟦🟦\n🟦🟦🟦🟦⭐",
                    "🟦⭐🟦🟦⭐\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n⭐🟦🟦🟦🟦\n🟦🟦🟦🟦🟦",
                    "🟦⭐🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n⭐🟦⭐🟦🟦\n🟦🟦🟦🟦⭐",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⭐\n🟦⭐🟦⭐🟦\n🟦🟦🟦⭐🟦",
                    "🟦🟦🟦⭐🟦\n🟦🟦🟦⭐🟦\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n⭐🟦🟦🟦🟦",
                    "🟦⭐🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⭐\n🟦🟦🟦⭐⭐\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦🟦⭐\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n⭐🟦🟦🟦🟦\n🟦🟦🟦🟦🟦",
                    "🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦⭐🟦\n🟦🟦🟦🟦🟦\n🟦🟦⭐🟦🟦",
                    "🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n⭐🟦⭐🟦🟦\n⭐🟦🟦🟦🟦\n⭐🟦🟦🟦🟦"
                  ]

os.system('title Zety')
print(colored('\n[Info]', 'dark_grey'), colored('Developer:', 'white'), colored('zety#7505', 'cyan'))
print(colored('''
     ______     ______     ______   __  __   
    /\___  \   /\  ___\   /\__  _\ /\ \_\ \   
    \/_/  /__  \ \  __\   \/_/\ \/ \ \____ \  
      /\_____\  \ \_____\    \ \_\  \/\_____\ 
      \/_____/   \/_____/     \/_/   \/_____/ 
                  Bot - v0.1\n\n''', 'cyan'))
print(colored('\n[Info]', 'dark_grey'), colored('Bot Iniciado com sucesso', 'green'))

while True:
    bot.send_message(chat_id=chat_id, text=mensagem_possivel)

    time.sleep(tempo_possivel_msg)

    date = datetime.now()
    date_futur = date + timedelta(minutes=tempo_espera)
    date_futur_format = date_futur.strftime('%H:%M')

    rangom_message = randint(0,quantia_mensagem)
    bot.send_message(chat_id=chat_id, text='🔔 Entrada Cofirmada 🔔\n\n💣 Minas: 3\n🎯 Nº de tentativas: 2\n🕗 Sinal Valido até: ' + date_futur_format + '\n\n🔗 Cadastre-se aqui: <a href="'+link_jogo+'">Entrar</a> \n\n' + lista_mensagem[rangom_message])

    time.sleep(tempo_espera*60)
    date_now = datetime.now()
    date_now_format = date_futur.strftime('%H:%M')
    bot.send_message(chat_id=chat_id, text='🔹 Sinal Finalizado 🔹\n\n🕑 Finalizado às: '+date_now_format+'\n✅✅✅GREEN✅✅✅')
    time.sleep(tempo_proxima_msg)