import discord
import math
import random
import os
import urllib
import time
import random
import requests
import json
import csv
import pandas as pd
from replit import db
from keep_alive import keep_alive
from os import system
from time import sleep
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request

# db.db_url = os.environ['DB']

client = discord.Client()

# AOTY Set main url to scrap from
my_url = Request(
    'https://www.metacritic.com/browse/albums/release-date/new-releases/date',
    headers={'User-Agent': 'Mozilla/5.0'})
uClient = uReq(my_url)
time.sleep(0.5)
page_html = uClient.read()
time.sleep(0.5)
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

release_date = page_soup.findAll("div", {"class": "clamp-details"})
album_artist_title = page_soup.findAll("div", {"class": "artist"})
album_title = page_soup.findAll("a", {"class": "title"})
album_cover = page_soup.findAll("div", {"class": "browse_list_wrapper"})
album_rating = page_soup.findAll("div", {"class": "clamp-score-wrap"})
album_summary = page_soup.findAll("div", {"class": "summary"})

# ALLTIME
file = pd.read_csv('1000.txt')
lista = pd.DataFrame(file)
lista = file.transpose()


def update_album(user, album):
    if str(user) in db.keys():
        lista1 = db[str(user)]
        lista1.append(album)
        db[str(user)] = lista1
    else:
        db[str(user)] = [album]


def delete_album(user, album):
    if str(user) in db.keys():
        lista1 = db[str(user)]
        if str(album) in lista1:
            print(str(album))
            lista1.remove(album)
        else:
            print('Não existe esse álbum na lista')
        # db[str(user)] = lista1
    else:
        print('Não funciona')


def unique_roll():
    roll = random.randint(0, len(db['2022']) - 1)
    album = db['2022'][roll]
    return album


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

# ALL TIME
    if message.content.startswith('!roll alltime'):
        alltime_album_number = random.randint(0, 1099)
        alltime_album_name = lista.iloc[alltime_album_number].name[4:]
        album = str(alltime_album_number) + ' - ' + str(alltime_album_name)
        db[str(message.author) + '_temp_list'] = album
        await message.channel.send(
            f'Bem-vindo ao desafio, @{message.author}. \nO álbum escolhido para você foi o nº: {alltime_album_number} - {alltime_album_name}\n\nVocê tem 24 horas para dar uma audição nesse álbum.\n Ao final, adicione-o à sua lista, simplesmente digitando !update'
        )

    # 2022
    if message.content.startswith('!roll 2022'):
        roll = random.randint(0, len(db['2022']) - 1)
        album = db['2022'][roll]
        while album in db[str(message.author)]:
            print('já tem')
            album = unique_roll()
            album = album
        await message.channel.send(
            f'Bem-vindo ao desafio dos lançamentos de 2022, {message.author}. \nO álbum escolhido para você foi o **{album["artist"]} - {album["album"]}**\n\nVocê tem 24 horas para dar uma audição nesse álbum.\n Ao final, adicione-o à sua lista, simplesmente digitando !update\n{album["spotify"]}'
        )
        db[str(message.author) + '_temp_list'] = album

    if message.content.startswith('!update'):
        album_novo = db[str(message.author) + "_temp_list"]
        update_album(message.author, album_novo)
        del db[str(message.author) + '_temp_list']
        if type(album_novo) is not str:
            await message.channel.send(
                f'**{album_novo["artist"]} - {album_novo["album"]}** inserido com sucesso à sua lista!'
            )
        else:
            await message.channel.send(
                f'**{album_novo}** inserido com sucesso à sua lista!')

    if message.content.startswith('!del_album'):
        album_number = int(message.content.split('!del_album ', 1)[1])
        album_name = lista.iloc[album_number].name[4:]
        album_to_delete = f'{album_number} - {album_name}'
        delete_album(message.author, album_to_delete)
        await message.channel.send(
            f'Álbum {album_to_delete} excluído da sua lista com sucesso!')

    if message.content.startswith('!2022status'):
        await message.channel.send(
            f"A lista de lançamentos de 2022 tem **{len(db['2022'])} álbuns** adicionados."
        )

    if message.content.startswith('!mystatus'):
        total = len(db[(str(message.author))])
        list_2022 = []
        total_alltime = total - len(list_2022)
        for album in db[(str(message.author))]:
            if type(album) is not str:
                list_2022.append(album)
        percentage_2022 = (len(list_2022) / total) * 100
        try:
            await message.channel.send(
                f'**{message.author}**\n- Você ouviu um total de **{total} álbuns** do desafio:\n    - **{len(list_2022)} álbuns** da lista de lançamentos de 2022 - (progresso: **{round(percentage_2022, 1)}%**).\n    - **{total - len(list_2022)} álbuns** da lista de alltime albums do server'
            )
        except:
            await message.channel.send(
                f'**{message.author}**\n- Você ouviu um total de **{total} álbuns** do desafio'
            )
        try:
            await message.channel.send(
                f'- Seu último álbum adicionado à lista foi o **{db[str(message.author)][-1]["artist"]} - {db[str(message.author)][-1]["album"]}**'
            )
        except:
            await message.channel.send(
                f'- Seu último álbum adicionado à lista foi o **{db[str(message.author)][-1]}**'
            )
        try:
            if db[str(message.author) + '_temp_list']:
                try:
                    await message.channel.send(
                        f'- No momento, você tem o seguinte álbum do desafio para ouvir: **{db[str(message.author) + "_temp_list"]["artist"]} - {db[str(message.author) + "_temp_list"]["album"]}**'
                    )
                except:
                    await message.channel.send(
                        f'- No momento, você tem o seguinte álbum do desafio para ouvir: **{db[str(message.author) + "_temp_list"]}**'
                    )
        except:
            await message.channel.send(
                f'- No momento, parece que você não tem nenhum álbum rollado para ouvir.'
            )

# FUNCIONANDO!!!
    if message.content.startswith('!users'):
        # total = len(db.keys())
        nivel = len(db[(str(message.author))])
        await message.channel.send('Usuários participando do desafio:\n')
        for user in db.keys():
            if '_temp_list' not in str(user):
                sender = len(db[(str(user))])
                await message.channel.send(f'{user}, Challenger +{sender}')

    if message.content.startswith('!leaderboard'):
        # total = len(db.keys())
        nivel = len(db[(str(message.author))])
        await message.channel.send(f'Leaderboard:\n')
        leaderboard = []
        excluders = ['2022releases', 'list', 'temp', '2022']
        for user in db.keys():
            clean_user = user.split('_')[-1]
            if clean_user != 'list' and user not in excluders:
                badges = len(db[(str(user))])
                sender1 = {'name': user, 'nbadges': badges}
                leaderboard.append(sender1)
        for user in sorted(leaderboard,
                           key=lambda i: i['nbadges'],
                           reverse=True):
            await message.channel.send(
                f"{user.get('nbadges')} - {user.get('name')}\n")

    if message.content.startswith('!del_users'):
        for n in db.keys():
            del db[n]

    if message.content.startswith('!commands'):
        await message.channel.send(
            f'Comandos do bot:\n\n**!newalbum - ARTISTA - ALBUM - SPOTIFY**   Adiciona um álbum à lista de lançamentos de 2022.\n**!roll alltime**   Seleciona um álbum aleatório da lista de melhores álbuns rankeados de todos os tempos.\n**!roll 2022**   Seleciona um álbum aleatório da nossa lista de lançamentos de 2022.\n**!update**   Atualiza sua lista de álbuns ouvidos com o último álbum rollado.\n**!mystatus**   Exibe seus status no desafio.\n**!2022status**   Exibe a quantidade de álbuns da lista de lançamentos de 2022.\n**!listall**   Exibe todos os álbuns já adicionados à lista de lançamentos de 2022.\n**!list LETRA**   Comando para listar todos os artistas adicionados na lista de lançamentos de 2022 que comecem com a LETRA escolhida.\n**!users**   Exibe todos os usuários participantes do desafio.\n**!leaderboard**   Exibe a leaderboard do desafio.'
        )

    if message.content.startswith('!newalbum'):
        album_novo = message.content.split(' - ')
        album = album_novo[2]
        artist = album_novo[1]
        spotify = album_novo[3]

        new = {'artist': artist, 'album': album, 'spotify': spotify}
        if '2022' in db.keys():
            if new in db['2022']:
                await message.channel.send(
                    f'Não foi possível adicionar esse álbum pois ele já está na lista.'
                )
            else:
                db['2022'].append(new)
                await message.channel.send(
                    f'**{new["artist"]} - {new["album"]}** inserido à lista de lançamentos de 2022 com sucesso!'
                )
        else:
            db['2022'] = [new]

    if message.content.startswith('!teste'):
        await message.channel.send(f'bot funcionando normalmente.')

    if message.content.startswith('!listall'):
        new_entries = [[v for v in d.values()][:-1] for d in db['2022']]
        new_entries2 = []
        counter = 0
        number = 1
        for item in new_entries:
            new_entries2.append(f'{number}. {item[0]} - {item[1]}')
            counter += 1
            number += 1
        await message.channel.send(
            'Álbuns já adicionados à lista de lançamentos de 2022:\n')
        for album in new_entries2:
            await message.channel.send(album)

    if message.content.startswith('!list '):
        letter = message.content.split(' ')[-1][0]
        new_entries = [[v for v in d.values()][:-1] for d in db['2022']]
        new_entries2 = []
        for item in new_entries:
            new_entries2.append(f'{item[0]} - {item[1]}')
        await message.channel.send(
            f'Álbuns de artistas que começam com a letra **{letter.upper()}** já adicionados à lista de lançamentos de 2022:\n'
        )
        number = 0
        for album in new_entries2:
            if album[0].lower() == letter.lower():
                await message.channel.send(album)
                number += 1
        await message.channel.send('--------------------------------')
        if number == 0:
            await message.channel.send(
                f'Nenhum artista com a letra **{letter.upper()}**')
        elif number == 1:
            await message.channel.send(
                f'- **{number}** artista com a letra **{letter.upper()}**')
        else:
            await message.channel.send(
                f'- **{number}** artistas com a letra **{letter.upper()}**')

#############################################################################

# Bring latest 4 albums
    if message.content.startswith('!getnew'):
        for number in range(4):
            await message.channel.send(
                f'\n{album_artist_title[number].getText()[40::].strip()} - {album_title[number].getText()}\n'
                f'Release date: {release_date[number].findChild("span").getText()} —— '
                f'Rating: {album_rating[number].contents[1].getText().strip()}'
            )
            time.sleep(0.5)
            await message.channel.send('...\n')
        await message.channel.send(
            f'\nsource: https://www.metacritic.com/browse/albums/release-date/new-releases/date'
        )


#############################################################################

my_secret = process.env['TOKEN']

keep_alive()
try:
    client.run(my_secret)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')
