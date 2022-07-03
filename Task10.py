import json
from pprint import pprint
from Task9 import scrape_movie_json

def analyse_language_and_directors():
    movies_json = scrape_movie_json()
    Directors_dict = {}

    for i in movies_json:
        for dire in i['director']:
            Directors_dict[dire]= {}
            for lan in i['language']:
                if lan not in Directors_dict[dire].keys():
                    Directors_dict[dire][lan]=1
                else:
                    Directors_dict[dire][lan]=+1
    # pprint(Directors_dict)


# analyse_language_and_directors()