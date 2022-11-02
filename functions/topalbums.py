from replit import db

def top_albums():
  unsorted_list = []
  for item in db['2022']:
    if len(item['rating']) > 0:
       try:
          if len(item['rating'].values()) > 1:
            score = sum(item['rating'].values())
            final_score = round(score/len(item['rating'].values()), 2)
            new_entry = {
                'artist': item['artist'],
                'album': item['album'],
                'rating': final_score
            }
            unsorted_list.append(new_entry)
       except:
          continue  
  sorted_list = sorted(unsorted_list, key=lambda d: d['rating'], reverse=True)
  return sorted_list


def bottom_albums():
  pass
  