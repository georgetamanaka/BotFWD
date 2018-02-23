#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# BotFWD - A telegram bot to forward random messages from a channel

"""
Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import random as rd
import logging, spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, Job)

# API Authorization for Spotify
client_credentials_manager = SpotifyClientCredentials(client_id='d859b7310236443a85af5b2c4dd8f169', client_secret='853138e3fc6b42c3857b3fc03e6ea48d')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Olá! Eu sou o BotFWD e existo unicamente para'
                              ' causar o desconforto nas pessoas!')
    bot.send_message(chat_id=update.message.chat_id, 
                     text="Meus comandos:\n"
                          "Iniciar o bot: /start\n"
                          "Mensagem aleatória: /random\n"
                          "Ajuda: /help")

def help(bot, update):
    update.message.reply_text('Sem ajuda malandro!')
    bot.send_message(chat_id=update.message.chat_id, 
                     text="Quer ajudar a desenvolver o bot?\n"
                          "https://goo.gl/x3jDri")

def random(bot, update):
    # update.message.reply_text('Em manutenção :(')
    messageID = rd.randint(6, 175)
    try:
        bot.forwardMessage(update.message.chat_id, '@botFwdTeste', messageID)
        print("Success => message_id %d" % messageID)
    except:
        print("Error => message_id %d does not exist" % messageID)
        random(bot, update)

def debug(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                     text="Toschi, para de tentar fazer merda de novo.")

   # print("Chat id %d" % update.message.chat_id) 
   # print("Message id %d" % update.message.message_id) 
   # for x in range(0, 175):
   #     try:
   #         # bot.forwardMessage(update.message.chat_id, '@ofwdnovo', messageID)
   #         bot.forwardMessage(update.message.chat_id, '@botFwdTeste', x)
   #         print("Success => message_id %d" % x)
   #     except:
   #         print("Error => message_id %d does not exist" % x)
   #         continue

def lero(bot, update):
    t0 = [  'Caros amigos, ',
            'Por outro lado, ',
            'Assim mesmo, ',
            'No entanto, não podemos esquecer que ',
            'Do mesmo modo, ',
            'A prática cotidiana prova que ',
            'Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ',
            'As experiências acumuladas demonstram que ',
            'Acima de tudo, é fundamental ressaltar que ',
            'O incentivo ao avanço tecnológico, assim como ',
            'Não obstante, ',
            'Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ',
            'Pensando mais a longo prazo, ',
            'O que temos que ter sempre em mente é que ',
            'Ainda assim, existem dúvidas a respeito de como ',
            'Gostaria de enfatizar que ',
            'Todavia, ',
            'A nível organizacional, ',
            'O empenho em analisar ',
            'Percebemos, cada vez mais, que ',
            'No mundo atual, ',
            'É importante questionar o quanto ',
            'Neste sentido, ',
            'Evidentemente, ',
            'Por conseguinte, ',
            'É claro que ',
            'Podemos já vislumbrar o modo pelo qual ',
            'Desta maneira, ',
            'O cuidado em identificar pontos críticos n',
            'A certificação de metodologias que nos auxiliam a lidar com ' ]

    t1 = [  'a execução dos pontos do programa ',
            'a complexidade dos estudos efetuados ',
            'a contínua expansão de nossa atividade ',
            'a estrutura atual da organização ',
            'o novo modelo estrutural aqui preconizado ',
            'o desenvolvimento contínuo de distintas formas de atuação ',
            'a constante divulgação das informações ',
            'a consolidação das estruturas ',
            'a consulta aos diversos militantes ',
            'o início da atividade geral de formação de atitudes ',
            'o desafiador cenário globalizado ',
            'a mobilidade dos capitais internacionais ',
            'o fenômeno da Internet ',
            'a hegemonia do ambiente político ',
            'a expansão dos mercados mundiais ',
            'o aumento do diálogo entre os diferentes setores produtivos ',
            'a crescente influência da mídia ',
            'a necessidade de renovação processual ',
            'a competitividade nas transações comerciais ',
            'o surgimento do comércio virtual ',
            'a revolução dos costumes ',
            'o acompanhamento das preferências de consumo ',
            'o comprometimento entre as equipes ',
            'a determinação clara de objetivos ',
            'a adoção de políticas descentralizadoras ',
            'a valorização de fatores subjetivos ',
            'a percepção das dificuldades ',
            'o entendimento das metas propostas ',
            'o consenso sobre a necessidade de qualificação ',
            'o julgamento imparcial das eventualidades ' ]

    t2 = [  'nos obriga à análise ',
            'cumpre um papel essencial na formulação ',
            'exige a precisão e a definição ',
            'auxilia a preparação e a composição ',
            'garante a contribuição de um grupo importante na determinação ',
            'assume importantes posições no estabelecimento ',
            'facilita a criação ',
            'obstaculiza a apreciação da importância ',
            'oferece uma interessante oportunidade para verificação ',
            'acarreta um processo de reformulação e modernização ',
            'pode nos levar a considerar a reestruturação ',
            'representa uma abertura para a melhoria ',
            'ainda não demonstrou convincentemente que vai participar na mudança ',
            'talvez venha a ressaltar a relatividade ',
            'prepara-nos para enfrentar situações atípicas decorrentes ',
            'maximiza as possibilidades por conta ',
            'desafia a capacidade de equalização ',
            'agrega valor ao estabelecimento ',
            'é uma das consequências ',
            'promove a alavancagem ',
            'não pode mais se dissociar ',
            'possibilita uma melhor visão global ',
            'estimula a padronização ',
            'aponta para a melhoria ',
            'faz parte de um processo de gerenciamento ',
            'causa impacto indireto na reavaliação ',
            'apresenta tendências no sentido de aprovar a manutenção ',
            'estende o alcance e a importância ',
            'deve passar por modificações independentemente ',
            'afeta positivamente a correta previsão ' ]

    t3 = [  'das condições financeiras e administrativas exigidas.',
            'das diretrizes de desenvolvimento para o futuro.',
            'do sistema de participação geral.',
            'das posturas dos órgãos dirigentes com relação às suas atribuições.',
            'das novas proposições.',
            'das direções preferenciais no sentido do progresso.',
            'do sistema de formação de quadros que corresponde às necessidades.',
            'das condições inegavelmente apropriadas.',
            'dos índices pretendidos.',
            'das formas de ação.',
            'dos paradigmas corporativos.',
            'dos relacionamentos verticais entre as hierarquias.',
            'do processo de comunicação como um todo.',
            'dos métodos utilizados na avaliação de resultados.',
            'de todos os recursos funcionais envolvidos.',
            'dos níveis de motivação departamental.',
            'da gestão inovadora da qual fazemos parte.',
            'dos modos de operação convencionais.',
            'de alternativas às soluções ortodoxas.',
            'dos procedimentos normalmente adotados.',
            'dos conhecimentos estratégicos para atingir a excelência.',
            'do fluxo de informações.',
            'do levantamento das variáveis envolvidas.',
            'das diversas correntes de pensamento.',
            'do impacto na agilidade decisória.',
            'das regras de conduta normativas.',
            'do orçamento setorial.',
            'do retorno esperado a longo prazo.',
            'do investimento em reciclagem técnica.',
            'do remanejamento dos quadros funcionais.' ]

    leroLero = rd.choice(t0) + rd.choice(t1) + rd.choice(t2) + rd.choice(t3)
    bot.send_message(chat_id=update.message.chat_id, text=leroLero)

def wordGenerate(bot, update):
    consonants = 'bcdfghjlmnpqrstvxz'
    vowels = 'aeiou'
    syllables = rd.randint(2, 10)
    result = ''

    for i in range(syllables):
        consonant = rd.choice(consonants)
        this_vowels = vowels
        if consonant == 'q':
            consonant += 'u'
            this_vowels = 'aeio'
        result += consonant + rd.choice(this_vowels)
        if i > 0 and result[-2] in 'bp' and rd.randint(0, 5) == 0:
            result = result[:-2] + 'm' + result[-2:]
        if i > 0 and result[-2] in 'cglrst' and rd.randint(0, 5) == 0:
            result = result[:-2] + 'n' + result[-2:]

    return result

def word(bot, update):
    result = wordGenerate(bot, update)
    bot.send_message(chat_id=update.message.chat_id, text=result)

def aplicacaonumafrase(bot, update):
    word = wordGenerate(bot, update)

    with open('aplicacaonumafrase.txt') as f:
        frases = [l.rstrip('\n') for l in f]

    result = rd.choice(frases).format(word=word)
    
    bot.send_message(chat_id=update.message.chat_id, text=result)

def filme(bot, update):
    palavrasM = ['cu', 'pinto', 'ânus', 'pipi', 'temer', 'caralho']
    palavrasF = ['rola', 'vagina', 'dilma']

    with open('filmeM.txt') as f:
        frasesM = [l.rstrip('\n') for l in f]
    with open('filmeF.txt') as f:
        frasesF = [l.rstrip('\n') for l in f]

    rPalavras = rd.randint(0, len(palavrasM) + len(palavrasF) - 1)
    if rPalavras < len(palavrasM): # M
        result = rd.choice(frasesM).format(word=palavrasM[rPalavras])
        result = result.replace('ânuss', 'ânus') # caso de borda
    else: # F
        rPalavras -= len(palavrasM)
        result = rd.choice(frasesF).format(word=palavrasF[rPalavras])

    bot.send_message(chat_id=update.message.chat_id, text=result)


def musica(bot, update):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
     # Some chars have lower values for the default max offset
    max_offset_special = {'h': 68587, 'q': 21550, 'w': 65601, 'z': 60495, '0': 57375}

    # Randomly get one of the chars
    rand_query = chars[rd.randint(0, 35)] 

    # Verify special cases in the max offset
    if rand_query in max_offset_special:
        max_offset = max_offset_special.get(rand_query)
    else:
        max_offset = 100000

    # Gets the result depending of the previously defined variables
    # 'results' contains a lot of information about the track selected, such as artist, track name, album, etc
    results = spotify.search(q = rand_query, limit=1, offset = rd.randint(0, int(max_offset)))

    # Get only the track id from the 'results'
    for i, t in enumerate(results['tracks']['items']):
        url = 'https://open.spotify.com/track/' + t['id']
        bot.send_message(chat_id=update.message.chat_id, text=url)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("390975324:AAG57sa1pBQ9Swk7ry-I4FJijWOc1XZYM5s")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("random", random))
    dp.add_handler(CommandHandler("fwd", random))
    dp.add_handler(CommandHandler("lero", lero))
    dp.add_handler(CommandHandler("lerolero", lero))
    dp.add_handler(CommandHandler("word", word))
    dp.add_handler(CommandHandler("palavra", word))
    dp.add_handler(CommandHandler("aplicacaonumafrase", aplicacaonumafrase))
    dp.add_handler(CommandHandler("frase", aplicacaonumafrase))
    dp.add_handler(CommandHandler("filme", filme))
    dp.add_handler(CommandHandler("musica", musica))
    dp.add_handler(CommandHandler("debug", debug))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    print('==== BOT started ====')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
