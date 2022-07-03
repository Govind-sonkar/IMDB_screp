import json 
from Task4 import scrape_movie_details
from pprint import pprint

a = open('all_movies.json', 'r')
b = json . load(a)
# b.close()

def  get_movie_list_details ():
    mai_list = []
    for i in b[:10]:
        mai_list.append(scrape_movie_details(i['url']))
    # pprint(mai_list)

    return  mai_list

# pprint(get_movie_developerlist_details ())