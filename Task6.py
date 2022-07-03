import json 
from Task5 import get_movie_list_details
from pprint import pprint

a = get_movie_list_details()
# pprint(a)

def analyse_movies_language ():
    language_dict = {}
    for i in  a:
        for l in i['language']:
            if l in  language_dict:
                language_dict[l] += 1
            else:
                 language_dict[l] = 1
    pprint(language_dict)          
analyse_movies_language ()