import discord
import math
import random
import os
import pytz
import urllib
import time
import random
import requests
import json
import csv
import pandas as pd
import numpy as np
# from discord.ext import commands
from collections import OrderedDict
from datetime import datetime
from dotenv import load_dotenv
from replit import db
from keep_alive import keep_alive
from os import system
from time import sleep
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request
from functions.topalbums import *
from functions.status import *
from functions.ratings import *
from functions.reviews import *
from functions.helpers import *
from functions.user import *

# db.db_url = os.environ['DB']
REPLIT_DB_URL = os.getenv("DB")

client = discord.Client(intents=discord.Intents.default())

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

# 2022
file2022 = pd.read_csv('2022.txt')
lista2022 = pd.DataFrame(file2022)
lista2022 = file2022.transpose()


# album_list = []

# def update_badge(user, level):
#   if user in db.keys():
#     level in db[user]:
#     badges = db[user]
#     badges.append(level)
#     db[user] = badges
#   else:
#     db[user] = level


# db['2022'][id]['reviews'][str(user)] = review


# db['2022'][id]['reviews'][str(user)] = review


def update_album_genre(user, id, genre):
    if str(user) in db.keys():
        print('aqui a')
        # if str(user) not in db['2022'][id]['rating'].keys():
        #   db['2022'][id]['rating'][str(user)] = {}
        if id < 1000:
            print('aqui b')
            db['2022'][id]['genre'] = genre.lower()
        else:
            album_id = id - 1000
            print('aqui c')
            db['alltime'][album_id]['genre'] = genre.lower()
            print('aqui d')
    else:
        pass


def unique_roll(lista):
    roll = random.randint(0, len(db[lista]) - 1)
    album = db[lista][roll]
    print('album retornando da função', album)
    return album


def filtered_roll_random(add_filter):
    roll = random.randint(0, len(add_filter) - 1)
    album = add_filter[roll]
    print('Entrou aqui no random, e returnou:', album['artist'])
    return album


def remove_points(user):
    db['points'][user] -= 1


def customized_top(number):
    pass


def filtered_roll(user, filter_list, operator, genre):
    add_filter = []
    try:
        if operator == 'only':
            add_filter = [x for x in filter_list if type(x) is not str and genre in x['genre']]
        elif operator == 'ignore':
            add_filter = [x for x in filter_list if type(x) is not str and genre not in x['genre']]
        else:
            pass
    except:
        print('erro dentro do filtered_roll')
        pass
    album = filtered_roll_random(add_filter)
    return album


def top_genres():
    genre_sorting = {}
    metal_counter = 0
    rock_counter = 0
    indie_counter = 0
    hip_hop_counter = 0
    electronic_counter = 0
    for album in db['2022']:
        if type(album) is not str:
            if 'metal' in album['genre']:
                metal_counter += 1
            elif 'indie' in album['genre']:
                indie_counter += 1
            elif 'electronic' in album['genre']:
                electronic_counter += 1
            elif 'hip hop' in album['genre']:
                hip_hop_counter += 1
            elif 'rock' in album['genre']:
                rock_counter += 1
    genre_sorting['metal'] = metal_counter
    genre_sorting['rock'] = rock_counter
    genre_sorting['indie'] = indie_counter
    genre_sorting['hip_hop'] = hip_hop_counter
    genre_sorting['electronic'] = electronic_counter
    print(genre_sorting)
    sorted_genres = [v for v in sorted(genre_sorting.items(), key=lambda item: item[1], reverse=True)]
    return sorted_genres


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # DEBUGGER
    if message.content.startswith('!acabou'):
        await message.channel.send("https://thumbs.gfycat.com/AnchoredDesertedEft-size_restricted.gif")

    if message.content.startswith('!run'):
        pass
        # for user in db.keys():
        #   if "#" in user and "temp" not in user:
        #     for album in db[user]:
        #       try:
        #         del album['spotify']
        #       except:
        #         print(user, album['id'])
        #       try:
        #         del album['reviews']
        #       except:
        #         print(user, album['id'])
        #       try:
        #         del album['rating']
        #       except:
        #         print(user, album['id'])
        #       try:
        #         del album['genre']
        #       except:
        #         print(user, album['id'])
        #       try:
        #         del album['added_by']
        #       except:
        #         print(user, album['id'])
        #       try:
        #         del album['added_on_time']
        #       except:
        #         print(user, album['id'])

        # for album in db['2022']:
        #   album["added_on_day"] = 'Not Available'
        #   album["added_on_time"] = 'Not Available'
        #   try:
        #     del album['added_on']
        #   except:
        #     print('deu ruim')

        # genre_list = []
        # for album in db['2022']:
        #   add_genres = album['genre'].strip(' ').split(', ')
        #   for genre in add_genres:
        #     # print('gêneros', add_genres)
        #     # print('gênero', genre)
        #     # genre.strip(' ')
        #     genre_list.append(genre)
        # print('contagem post punk', genre_list.count('post-punk'))
        # dict1 = dict((i, genre_list.count(i)) for i in genre_list)
        # sorted_value_index = np.argsort(dict1.values())
        # dictionary_keys = list(dict1.keys())
        # sorted_dict = {dictionary_keys[i]: sorted(dict1.values())[i] for i in range(len(dictionary_keys))}

        # print(sorted_dict)

    if message.content.startswith('!dburl'):
        print(os.getenv("REPLIT_DB_URL"))
        await message.channel.send(os.getenv("REPLIT_DB_URL"))

        # counter = 1000
        # for item in db['alltime']:
        #   item['id'] = counter
        #   counter += 1

    # ALL TIME
    if message.content.startswith('!roll alltime'):
        roll = random.randint(0, len(db['alltime']) - 1)
        album = db['alltime'][roll]
        filter_list = []
        for item in db[str(message.author)]:
            try:
                if item['tag'] == 'alltime':
                    filter_list.append(item)
            except:
                continue
        filter_list2 = [x['album'] for x in filter_list]
        while album['album'] in filter_list2:
            album = unique_roll('alltime')
        await message.channel.send(
            f'Bem-vindo ao desafio da lista de alltime álbuns do RYM, {message.author}. \nO álbum escolhido para você foi o:\n{divider}**{album["id"]}. {album["artist"]} - {album["album"]}** - *{album["year"]}*{divider}Você tem 24 horas para dar uma audição nesse álbum. Ao final, adicione-o à sua lista, simplesmente digitando !update\n{album["spotify"]}'
        )
        db[str(message.author) + '_temp_list'] = album

    # 2022
    if message.content.startswith('!setgenre'):
        album_id = int(message.content.split(' ', 2)[1])
        album_genre = message.content.split(' ', 2)[-1]
        try:
            update_album_genre(message.author, album_id, album_genre)
            print('aqui 0')
            if album_id < 1000:
                print('aqui 1')
                await message.channel.send(
                    f'tag(s) **{album_genre}** atualizada(s) com sucesso para o álbum **{db["2022"][album_id]["id"]}. {db["2022"][album_id]["artist"]} - {db["2022"][album_id]["album"]}**')
            else:
                album_id = album_id - 1000
                await message.channel.send(
                    f'tag(s) **{album_genre}** atualizada(s) com sucesso para o álbum **{db["alltime"][album_id]["id"]}. {db["alltime"][album_id]["artist"]} - {db["alltime"][album_id]["album"]}**')
        except:
            await message.channel.send(
                f'Algo deu errado.')

    #######################################################

    if message.content.startswith('!filter'):
        filter = message.content.split(' ', 1)[-1]
        if filter.lower() == 'missing':
            result = [v for v in db['2022'] if not v['genre']]
            # result = [v for v in db['2022'] if len(v['genre']) < 2]
            if len(result) > 0:
                await message.channel.send(f'Álbuns que precisam ser taggeados:')
                for album in result:
                    await message.channel.send(f'**{album["id"]}**. {album["artist"]} - {album["album"]}\n')
            else:
                await message.channel.send(f'Todos os álbuns já foram taggeados.')
        else:
            result = [v for v in db['2022'] if filter in v['genre']]
            if len(result) < 1:
                await message.channel.send(f'Parece que não há nenhum álbum taggeado com o gênero **{filter}**')
            else:
                await message.channel.send(f'Álbuns taggeados com o(s) gênero(s) **{filter}**:\n{divider}')
                for album in result:
                    await message.channel.send(f'**{album["id"]}**. {album["artist"]} - {album["album"]}')
                await message.channel.send(f'{divider}')

    #######################################################

    if message.content.startswith('!country'):
        c = message.content.split(' ', 1)[1:]
        country = ' '.join(c).title()
        if country.lower() == 'missing':
            result = [v for v in db['2022'] if not v['country']]
            if len(result) > 0:
                await message.channel.send(f'Álbuns que precisam ser taggeados com o país:')
                for album in result:
                    await message.channel.send(f'**{album["id"]}**. {album["artist"]} - {album["album"]}\n')
            else:
                await message.channel.send(f'Todos os álbuns já foram taggeados com o país.')
        else:
            result = [v for v in db['2022'] if country in v['country']]
            if len(result) < 1:
                await message.channel.send(f'Parece que não há nenhum álbum do país **{country}**')
            else:
                await message.channel.send(f'Álbuns do país **{country}**:\n{divider}')
                for album in result:
                    await message.channel.send(f'**{album["id"]}**. {album["artist"]} - {album["album"]}')
                await message.channel.send(f'{divider}')

            #######################################################

    if message.content.startswith('!roll 2022'):
        check_user(str(message.author))
        roll = random.randint(0, len(db['2022']) - 1)
        filter1 = message.content.split(' ', 3)
        user_list = [x['id'] for x in db[str(message.author)] if type(x) is not str]
        filter_list = [x for x in db['2022'] if x['id'] not in user_list]
        album = db['2022'][roll]
        if len(filter_list) != 0:
            try:
                album = filtered_roll(str(message.author), filter_list, filter1[2], filter1[-1])
            except:
                roll = random.randint(0, len(filter_list) - 1)
                album = filter_list[roll]
        else:
            await message.channel.send(
                f'{str(message.author)}, parece que não há nenhum álbum disponível para você ouvir com estas configurações'
                )
        await message.channel.send(
            f'Bem-vindo ao desafio dos lançamentos de 2022, {message.author}. \nO álbum escolhido para você foi o:\n{divider}**{album["id"]}. {album["artist"]} - {album["album"]}**\n*{album["genre"]}*\n{divider}Você tem 24 horas para dar uma audição nesse álbum. Ao final, adicione-o à sua lista, simplesmente digitando !update\n{album["spotify"]}'
        )
        db[str(message.author) + '_temp_list'] = album

    if message.content.startswith('!update'):
        if not db[str(message.author) + "_temp_list"]:
            await message.channel.send(
                f'**{str(message.author)}**, parece que você não tem nenhum album rollado para atualizar.')
        else:
            to_update = db[str(message.author) + "_temp_list"]
            update_album(str(message.author), to_update)
            del db[str(message.author) + '_temp_list']
            if type(to_update) is not str:
                try:
                    await message.channel.send(
                        f'**{to_update["id"]}. {to_update["artist"]} - {to_update["album"]}** inserido com sucesso à sua lista!'
                    )
                except:
                    await message.channel.send(
                        f'**{to_update["artist"]} - {to_update["album"]}** inserido com sucesso à sua lista!')
            else:
                await message.channel.send(
                    f'**{to_update}** inserido com sucesso à sua lista!')

    if message.content.startswith('!review'):
        album_id = int(message.content.split(' ', 2)[1])
        album_review = message.content.split(' ', 2)[2:]
        # print('review type', type(album_review))
        # print('review', album_review)
        update_album_review(message.author, album_id, album_review[0])
        if db['2022'][album_id]['reviews'][str(message.author)]:
            await message.channel.send(
                f'Review do álbum **{album_id}. {db["2022"][album_id]["artist"]} - {db["2022"][album_id]["album"]}** atualizada com sucesso!'
            )
        else:
            await message.channel.send(
                f'erro')

    if message.content.startswith('!rating'):
        album_id = int(message.content.split(' ', 2)[1])
        album_rating = message.content.split(' ', 2)[-1]
        album_rating = album_rating.replace(',', '.')
        album_rating = float(album_rating.split('/')[0])
        update_album_rating(message.author, album_id, album_rating)
        lista = id_helper(album_id)
        if album_id > 999:
            album_id -= 1000
        try:
            if db[lista][album_id]['rating'][str(message.author)]:
                await message.channel.send(
                    f'Rating de **{album_rating}/10** adicionado ao álbum **{db[lista][album_id]["id"]}. {db[lista][album_id]["artist"]} - {db[lista][album_id]["album"]}** com sucesso!'
                )
        except:
            await message.channel.send(
                f'Algo deu errado.')

    if message.content.startswith('!getreviews'):
        album_id = int(message.content.split(' ', 1)[-1])
        lista = id_helper(album_id)
        if album_id > 999:
            album_id - 1000
        await message.channel.send(
            f'Reviews do **{db[lista][album_id]["artist"]} - {db[lista][album_id]["album"]}:\n**')
        counter = 0
        for review in db[lista][album_id]['reviews'].items():
            await message.channel.send(f'**{review[0]}** - *"{review[1]}"*\n')
            counter += 1
        if counter == 0:
            await message.channel.send(f'Nenhuma resenha atribuída para este álbum.')
        await message.channel.send(f'\n{divider}')

    ########################################################################

    if message.content.startswith('!getratings'):
        album_id = int(message.content.split(' ', 1)[-1])
        lista = id_helper(album_id)
        if album_id > 999:
            album_id - 1000
        await message.channel.send(f'Ratings do **{db[lista][album_id]["artist"]} - {db[lista][album_id]["album"]}**')
        average = []
        for rating in db[lista][album_id]['rating'].items():
            user_rating = rating[1]
            average.append(user_rating)

            await message.channel.send(f'{rating[0]}:  **{rating[1]}**\n')
        if len(average) > 0:
            await message.channel.send(
                f'{divider}Média do server: **{str(sum(average) / len(average))[:3]}**\n{divider}')
        else:
            await message.channel.send(f'Nenhuma nota atribuída para este álbum.\n{divider}')

    ########################################################################

    if message.content.startswith('!del_album'):
        id = int(message.content.split(' ', 1)[-1])
        user = str(message.author)
        album = del_last_album(id)
        if album:
            await message.channel.send(
                f'Álbum {album["id"]}. {album["artist"]} - {album["album"]} excluído da lista de lançamentos com sucesso!')
            add_points(user)
            await message.channel.send(
                f'\n{divider}**{str(message.author)}**, seu total de pontos atualizado é **{db["points"][str(message.author)]}** ponto(s).')
        else:

            await message.channel.send('ID incorreto. Verifique as informações novamente.')

    ########################################################################

    if message.content.startswith('!2022status'):
        # top_genres = top_genres()
        total_notas, total_reviews = list_status()
        await message.channel.send(
            f"-A lista de lançamentos de 2022 tem **{len(db['2022'])} álbuns** adicionados.\n-Já foram atribuídas **{total_notas}** notas e **{total_reviews}** reviews.\n{divider}"
        )
        # for genre in sorted_genres:
        #   await message.channel.send(
        #     f"***{genre[1]}** taggeados sob o gênero **{genre[0]}***")
    #######################################################################################

    if message.content.startswith('!mystatus'):
        total = len(db[(str(message.author))])
        list_2022 = []
        if total == 0:
            await message.channel.send(
                f'- Você ainda não tem dados suficientes disponíveis, mas, no momento, você tem o seguinte álbum do desafio para ouvir: **{db[str(message.author) + "_temp_list"]["id"]}**. {db[str(message.author) + "_temp_list"]["artist"]} - {db[str(message.author) + "_temp_list"]["album"]}. Seus status serão atualizados assim que você atualizar sua lista com o **!update**')
        else:
            list_2022, percentage_2022 = mystatus(list_2022, str(message.author))
            try:
                await message.channel.send(
                    f'**{message.author}**\n- Você ouviu um total de **{total} álbuns** do desafio:\n    - **{len(list_2022)} álbuns** da lista de lançamentos de 2022 - (progresso: **{round(percentage_2022, 1)}%**).\n'
                )
            except:
                await message.channel.send(
                    f'**{message.author}**\n- Você ouviu um total de **{total} álbuns** do desafio'
                )
            try:
                await message.channel.send(
                    f'- Seu último álbum adicionado à lista foi o **{db[str(message.author)][-1]["id"]}. {db[str(message.author)][-1]["artist"]} - {db[str(message.author)][-1]["album"]}**'
                )
            except:
                await message.channel.send(
                    f'- Seu último álbum adicionado à lista foi o **{db[str(message.author)][-1]}**'
                )
            try:
                if db[str(message.author) + '_temp_list']:
                    try:
                        await message.channel.send(
                            f'- No momento, você tem o seguinte álbum do desafio para ouvir: **{db[str(message.author) + "_temp_list"]["id"]}. {db[str(message.author) + "_temp_list"]["artist"]} - {db[str(message.author) + "_temp_list"]["album"]}**'
                        )
                    except:
                        await message.channel.send(
                            f'- No momento, você tem o seguinte álbum do desafio para ouvir: **{db[str(message.author) + "_temp_list"]}**'
                        )
            except:
                await message.channel.send(
                    f'- No momento, parece que você não tem nenhum álbum rollado para ouvir.'
                )
            await message.channel.send(
                f'- Você tem um total de **{db["points"][str(message.author)]}** ponto(s) para gastar.'
            )

        #######################################################################################

    if message.content.startswith('!top'):
        number = 0
        if len(message.content) > 4:
            try:
                number = int(message.content.split(' ')[-1])
            except:
                pass
        sorted_list = top_albums()
        await message.channel.send(f'Melhores lançamentos desde agosto de 2022 rankeados no server:\n{divider}')
        counter = 1
        if number != 0:
            for item in sorted_list:
                await message.channel.send(f'{counter}. {item["artist"]} - {item["album"]}  :  **{item["rating"]}**')
                counter += 1
                if counter > number:
                    break
        else:
            await message.channel.send(f'{counter}. {item["artist"]} - {item["album"]}  :  **{item["rating"]}**')
            counter += 1
        await message.channel.send(
            f'{divider}*Apenas álbuns com mais de uma nota recebida são contabilizados nessa lista*')

    #######################################################################################

    if message.content.startswith('!bottom'):
        number = 0
        if len(message.content) > 4:
            try:
                number = int(message.content.split(' ')[-1])
            except:
                pass
        sorted_list = top_albums()
        sorted_list = sorted(sorted_list, key=lambda d: d['rating'], reverse=False)
        await message.channel.send(
            f'Álbuns com as notas mais baixas desde agosto de 2022 rankeados no server:\n{divider}')
        counter = 0
        if number != 0:
            for item in sorted_list:
                await message.channel.send(
                    f'{len(sorted_list) - counter}. {item["artist"]} - {item["album"]}  :  **{item["rating"]}**')
                counter += 1
                if counter > number:
                    break
        else:
            await message.channel.send(f'{counter}. {item["artist"]} - {item["album"]}  :  **{item["rating"]}**')
            counter += 1
        await message.channel.send(
            f'{divider}*Apenas álbuns com mais de uma nota recebida são contabilizados nessa lista*')

    ########################################################################################

    if message.content.startswith('!myreviews'):
        sorted_list = myreviews(str(message.author))
        await message.channel.send(f'**{message.author}**, suas reviews foram enviadas no privado.\n{divider}')
        await message.author.send(f'**{message.author}**, seguem suas reviews para os lançamentos de 2022:\n{divider}')
        counter = 0
        for item in sorted_list:
            await message.author.send(f'**{item["artist"]} - {item["album"]}**  :  *{item["review"]}*\n{divider}')
            time.sleep(1)
            ########################################################################################

    if message.content.startswith('!myratings'):
        sorted_list = myratings(str(message.author))
        await message.channel.send(f'Álbuns avaliados por **{message.author}**:\n{divider}')
        counter = 1
        for item in sorted_list:
            await message.channel.send(f'{counter}. {item["artist"]} - {item["album"]}  :  **{item["rating"]}**')
            counter += 1
        await message.channel.send(f'{divider}')

    ########################################################################################

    # HELPER
    if message.content.startswith('!myalbums'):
        lista = myalbums(str(message.author))
        await message.channel.send(lista)

    #########################################################################################

    # HELPER
    if message.content.startswith('!missing'):
        missing_reviews, missing_ratings = missing(str(message.author))
        await message.channel.send(f'**{str(message.author)}**, seguem suas resenhas faltantes:\n{divider}')
        try:
            for id in missing_reviews:
                await message.channel.send(
                    f'**{db["2022"][id]["id"]}.** {db["2022"][id]["artist"]} - {db["2022"][id]["album"]}')
        except:
            pass
        await message.channel.send(f'{divider}')
        await message.channel.send(f'**{str(message.author)}**, seguem suas notas faltantes:\n{divider}')
        try:
            for id in missing_ratings:
                await message.channel.send(
                    f'**{db["2022"][id]["id"]}.** {db["2022"][id]["artist"]} - {db["2022"][id]["album"]}')
        except:
            pass
        await message.channel.send(f'{divider}')

        ########################################################################################

    if message.content.startswith('!lastadded'):
        counter = 1
        index = len(db['2022']) - counter
        await message.channel.send(f'Últimos 5 álbuns adicionados à lista de lançamentos de 2022:\n{divider}')
        for album in range(5):
            await message.channel.send(
                f'**{db["2022"][index]["id"]}.** {db["2022"][index]["artist"]} - {db["2022"][index]["album"]} ({db["2022"][index]["year"]})')
            index -= 1
        await message.channel.send(divider)

    ########################################################################################

    if message.content.startswith('!sc'):
        id = int(message.content.split(' ', 2)[1])
        c = message.content.split(' ', 2)[2:]
        country = ' '.join(c).title()
        db['2022'][id]['country'] = country
        await message.channel.send(f'{country} atribuido para o id {db["2022"][id]["id"]}')

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
        for user in db.keys():
            if '#' in user and '_temp_list' not in user:
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
            f'Comandos do bot:\n\n**!newalbum - ARTISTA - ALBUM - SPOTIFY**   Adiciona um álbum à lista de lançamentos de 2022.\n**!roll alltime**   Seleciona um álbum aleatório da lista de melhores álbuns rankeados de todos os tempos.\n**!roll 2022**   Seleciona um álbum aleatório da nossa lista de lançamentos de 2022.\n**!roll 2022 only GENRE**   Rola apenas álbuns taggeados com o gênero específico da lista de lançamentos de 2022.\n**!roll 2022 ignore GENRE**   Ignora o gênero específico ao rolar álbuns da lista de lançamentos de 2022.\n**!update**   Atualiza sua lista de álbuns ouvidos com o último álbum rollado.\n**!mystatus**   Exibe seus status no desafio.\n**!myratings**    Exibe seus álbuns ouvidos melhores avaliados.**\n**!myreviews**    Exibe, por mensagem direta (DM), todas as resenhas que você já realizou no desafio.\n!2022status**   Exibe a quantidade de álbuns da lista de lançamentos de 2022.\n**!list2022**   Exibe todos os álbuns já adicionados à lista de lançamentos de 2022.\n**!list LETRA**   Exibe todos os artistas adicionados na lista de lançamentos de 2022 que comecem com a LETRA escolhida.\n**!id NUMERO**    Exibe o álbum com o respectivo ID\n**!review ID TEXTO**    Salva o texto como a resenha para o álbum do respectivo ID\n**!rating ID NOTA**    Salva a nota para o álbum do respectivo ID\n**!getreviews ID**    Exibe todas as resenhas para o álbum do respectivo ID\n**!getratings ID**    Exibe todas as notas para o álbum do respectivo ID\n**!topalbums**    Exibe os álbuns mais bem avaliados do server\n**!users**   Exibe todos os usuários participantes do desafio.\n**!leaderboard**   Exibe a leaderboard do desafio.'
        )
    if message.content.startswith('!newalltime'):
        album_novo = message.content.split(' - ')
        artist = album_novo[1]
        album = album_novo[2]
        year = str(album_novo[3])
        spotify = album_novo[4]
        id = db['alltime'][-1]['id'] + 1
        reviews = {}
        rating = {}
        genre = ''
        tag = 'alltime'
        new = {'artist': artist, 'album': album, 'spotify': spotify, 'id': id, 'reviews': reviews, 'rating': rating,
               'genre': genre, 'year': year, 'tag': tag}
        if 'alltime' in db.keys():
            if new in db['alltime']:
                await message.channel.send(
                    f'Não foi possível adicionar esse álbum pois ele já está na lista.'
                )
            else:
                db['alltime'].append(new)
                await message.channel.send(
                    f'**{new["artist"]} - {new["album"]}** inserido à lista de alltime do RYM com sucesso! (id: **{new["id"]}**)'
                )
        else:
            db['alltime'] = [new]

    if message.content.startswith('!newalbum'):
        create_db()
        album_novo = message.content.split(' - ')
        artist = album_novo[1]
        album = album_novo[2]
        spotify = album_novo[3]
        id = db['2022'][-1]['id'] + 1
        reviews = {}
        rating = {}
        genre = ''
        year = '2022'
        country = '#'
        added_on_day = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%d/%m/%Y")
        added_on_time = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M:%S")
        added_by = str(message.author)
        new = {'artist': artist, 'album': album, 'spotify': spotify, 'id': id, 'reviews': reviews, 'rating': rating,
               'genre': genre, 'year': year, 'country': country, 'added_on_day': added_on_day,
               'added_on_time': added_on_time, 'added_by': added_by}
        album_list = [x['album'] for x in db['2022']]
        if db['points'][str(message.author)] > 0:
            if '2022' in db.keys():
                if new['album'] in album_list:
                    print('entrou já tem')
                    await message.channel.send(
                        f'Não foi possível adicionar esse álbum pois ele já está na lista.'
                    )
                else:
                    print('entrou NÃo tem')
                    db['2022'].append(new)
                    await message.channel.send(
                        f'**{new["artist"]} - {new["album"]}** inserido à lista de lançamentos de 2022 com sucesso! (id: **{new["id"]})**\n{divider}adicionado em **{new["added_on_day"]}** às **{new["added_on_time"]}** por **{new["added_by"]}**')
                    remove_points(str(message.author))
                    await message.channel.send(
                        f'\n{divider}**{str(message.author)}**, seu total de pontos atualizado é **{db["points"][str(message.author)]}** ponto(s).')
            else:
                db['2022'] = [new]
        else:
            await message.channel.send(
                f'**{str(message.author)}**, você não tem pontos suficientes para esta operação. Total de pontos: **{db["points"][str(message.author)]}**\nPara ganhar pontos, participe do desafio do #album-challenge ')

    if message.content.startswith('!teste'):
        await message.channel.send(f'bot funcionando normalmente.')

    if message.content.startswith('!listgenres'):
        genres = list(set([x['genre'] for x in db['2022'] if type(x) is not str]))
        print(genres)
        # await message.channel.send(f'Gêneros da lista de lançamentos de 2022')
        # await message.channel.send(', '.join(genres))

    if message.content.startswith('!list2022'):
        new_entries = [[v for v in d.values()][:-1] for d in db['2022']]
        new_entries2 = []
        counter = 0
        number = 0
        for item in new_entries:
            new_entries2.append(f'**{number}**. {item[0]} - {item[1]}')
            counter += 1
            number += 1
        await message.channel.send(
            'Álbuns já adicionados à lista de lançamentos de 2022:\n')
        for album in new_entries2:
            await message.channel.send(album)
        await message.channel.send(divider)

    if message.content.startswith('!listalltime'):

        await message.channel.send(
            f'Álbuns da lista de alltime álbuns do RYM:\n{divider}')
        for album in db['alltime']:
            await message.channel.send(
                f'**{album["id"]}**. {album["artist"]} - {album["album"]} - *{album["year"]}*')
        await message.channel.send(divider)

    if message.content.startswith('!list '):
        letter = message.content.split(' ')[-1][0]
        new_entries = [[v for v in d.values()] for d in db['2022']]
        new_entries2 = []
        for item in new_entries:
            new_entries2.append(f'{item[0]} - {item[1]} (id: **{item[3]}**)')
        await message.channel.send(
            f'Álbuns de artistas que começam com a letra **{letter.upper()}** já adicionados à lista de lançamentos de 2022:\n'
        )
        number = 0
        for album in new_entries2:
            if album[0].lower() == letter.lower():
                await message.channel.send(album)
                number += 1
        await message.channel.send(f'{divider}')
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

    if message.content.startswith('!id '):
        id = int(message.content.split(' ')[-1])
        lista = id_helper(id)
        if id > 999:
            id = id - 1000
        album = db[lista][id]
        await message.channel.send(
            f'**{album["artist"]} - {album["album"]} ({album["year"]})**\n*{album["genre"]}*\n**{album["country"]}**\n{divider}adicionado em **{album["added_on_day"]}** às **{album["added_on_time"]}** por **{album["added_by"]}**\n\n{album["spotify"]}')

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

my_secret = os.environ['TOKEN'] # Insert your discord bot token here

keep_alive()
try:
    client.run(my_secret)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')
    time.sleep(50)
