import json 
from Task5 import get_movie_list_details
from pprint import pprint

a = get_movie_list_details()
# pprint(a)

def analyse_movies_directors ():
    directors_dict = {}
    for i in  a:
        for l in i['director']:
            if l in  directors_dict:
                directors_dict[l] += 1
            else:
                 directors_dict[l] = 1
    pprint(directors_dict)          
# analyse_movies_directors ()