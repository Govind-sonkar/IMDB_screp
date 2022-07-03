import json
from pprint import pprint
from Task4 import scrape_movie_details
# print(scrape_movie_details)

a = open('all_movies.json' , 'r')
url = json.load(a)

def scrape_movie_json():
    for i in url[:10]:
        # print(i)
        url_name = i["url"]
        file_name ="movies/"+url_name[27:36]+".json"
        file_name =url_name[27:36]+".json"
        all_movies = scrape_movie_details(url_name)
        with open(file_name,"w+")as file:
            json.dump(all_movies,file,indent=6)

# scrape_movie_json()