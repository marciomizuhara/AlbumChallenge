from replit import db

divider = '---------------------------------------------------------------------------\n'

def create_db():
  if '2022' in db.keys():
    pass
  else:
    db['2022'] = []


def id_helper(id):
  lista = ''
  if id < 1000:
    lista = '2022'
  else:
    lista = 'alltime'
  return lista
  

def myalbums(user):
  lista = []
  for album in db[user]:
    texto = f'{album["artist"]} - {album["album"]}'
    lista.append(texto)
  return lista


def missing(user):
  user_list = [x for x in db[user]]
  review_list = []
  rating_list = []
  print('user', user,'\ntipo:', type(user))
  for album in db['2022']:    
    try:
      if user in album['reviews']:
        review_list.append(album['id'])
    except:
      pass
    try:
      if user in album['rating']:
        rating_list.append(album['id'])
    except:
      pass      
  missing_reviews = []
  missing_ratings = []  
  if len(review_list) > 0:
    missing_reviews = [x['id'] for x in user_list if x['id'] not in review_list]
  if len(rating_list) > 0:
    missing_ratings = [x['id'] for x in user_list if x['id'] not in rating_list]
  return missing_reviews, missing_ratings


def del_last_album(id):
  if id == db['2022'][-1]['id']: 
    print('entrou ID igual')
    album = db['2022'][-1]
    del db['2022'][-1]
    return album
  else:
    return None
    