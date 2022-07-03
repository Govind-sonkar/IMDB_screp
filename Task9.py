import json,os
import random, time
from pprint import pprint
from Task4 import scrape_movie_details
# print(scrape_movie_details)

a = open('all_movies.json' , 'r')
url = json.load(a)

# def scrape_movie_json():
#     all = []
#     time.sleep(random.randint(1,10))
#     for i in url[:10]:
#         # print(i)
#         url_name = i["url"]
#         file_name ="movies/"+url_name[27:36]+".json"
#         file_name =url_name[27:36]+".json"
#         if (os.path.exists(file_name)):
#             all_movies = scrape_movie_details(url_name)
#         else:
#             all_movies = scrape_movie_details(url_name)
#             a = open(file_name,'w')
#             json.dump(all_movies,a,indent=4)
#         all.append(all_movies)
#     return all

# pprint (scrape_movie_json())
