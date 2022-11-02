from replit import db

def list_status():
  total_notas = 0
  total_reviews = 0
  for item in db['2022']:
    if len(item['rating']) > 0:
      for nota in item['rating']:
        if len(nota) > 0:
          total_notas += 1
    if len(item['reviews']) > 0:
      for review in item['reviews']:
        if len(review) > 0:
          total_reviews += 1
  return total_notas, total_reviews



def mystatus(list_2022, user):
  for album in db[user]:
    if album['year'] == '2022':
      list_2022.append(album)        
  percentage_2022 = (len(list_2022) / len(db['2022'])) * 100
  return list_2022, percentage_2022
                