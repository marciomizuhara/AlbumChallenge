from replit import db


def myreviews(user):
  unsorted_list = []      
  for item in db['2022']:
    for review in item['reviews']:
      if review == user:            
        try:
          new_entry = {
                'artist': item['artist'],
                'album': item['album'],
                'review': item['reviews'][review]
            }
          unsorted_list.append(new_entry)              
        except:              
          continue
  sorted_list = sorted(unsorted_list, key=lambda d: d['artist'])
  return sorted_list


def update_album_review(user, id, review):    
    if str(user) in db.keys():
        if str(user) not in db['2022'][id]['reviews'].keys():
          db['2022'][id]['reviews'][str(user)] = {}
        db['2022'][id]['reviews'][str(user)] = review
    else:
        pass