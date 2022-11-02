from replit import db
from functions.helpers import *


def myratings(user):
  unsorted_list = []
  for item in db['2022']:
    for nota in item['rating']:                        
        if nota == str(user):                            
          try:              
            new_entry = {
                'artist': item['artist'],
                'album': item['album'],
                'rating': item['rating'][nota]
            }
            unsorted_list.append(new_entry)                
          except:                
            continue      
  sorted_list = sorted(unsorted_list, key=lambda d: d['rating'], reverse=True)
  return sorted_list


def getratings(lista, album_id):
  pass


def update_album_rating(user, id, rating):    
    lista = id_helper(id)
    if id > 999:
          id = id - 1000
    if str(user) in db.keys():
        if str(user) not in db['2022'][id]['rating'].keys():
          db[lista][id]['rating'][str(user)] = {}
        db[lista][id]['rating'][str(user)] = rating
    else:
        pass