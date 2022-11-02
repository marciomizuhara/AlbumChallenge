from replit import db
from functions.helpers import *


def check_user(user):
  if not db[user]:
    print('user novo')
    db[user] = []
    db['points'][user] = 1    
  else:
    print('user existente')


def add_points(user):    
    db['points'][user] += 1 


def update_album(user, album):
  del album['spotify']
  del album['reviews']
  del album['rating']
  del album['genre']
  del album['added_by']
  del album['added_on_time']    
  if str(user) in db.keys():
      lista1 = db[str(user)]
      lista1.append(album)
      db[str(user)] = lista1
  else:
      db[str(user)] = [album]        
  add_points(user)