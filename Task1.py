
import json,requests
from pprint import pprint
from bs4 import BeautifulSoup

url="https://www.imdb.com/india/top-rated-indian-movies/"
page = requests.get(url)
# print(page.text)

soup = BeautifulSoup(page.text,'html.parser')

def scrape_top_list():
    
    #*************************************************************************main_div 
    main_div = soup.find('div',class_='lister')
    # print(main_div)

    #************************************************************************* tbody 
    tbody = main_div.find('tbody',class_='lister-list')
    # print(tbody)

    #************************************************************************* tbody 
    trs = tbody.find_all('tr')
    # print(trs)
    #...................OR.....................OR...................OR
    # return trs
# print(scrape_top_list())

    movies_ranks = []
    movies_name = []
    year_of_realease = []
    movie_urls = []
    movie_ratings = []

    for tr in trs:
        # position = tr.find('td', class_='titleColumn')         #  sabhi  td tag ka data dega .
        # print(position) 

        # position = tr.find('td', class_='titleColumn').get_text().strip()     # .strip() lgane par white space remove ho jata hai and .strip() nahi lahane par white space add ho jata hai .
        # print(position)
        
        position = tr.find('td', class_='titleColumn').get_text()        # get_text() lagane par sare tag hat jate hai and nahi lagane par data tag me milta hai .
        # print(position)

        rank = ''
        for i in position:
            if '.' not in i:
                rank = rank + i.strip()
            else:
                break
        movies_ranks.append(rank)
    # print(movies_ranks)       # all movies ranks acces

        title = tr.find('td',class_= 'titleColumn').a.get_text()
        movies_name.append(title)
    # print(movies_name)

        year = tr.find('td',class_ = 'titleColumn').span.get_text()
        year_of_realease.append(year)
    # print(year_of_realease)
   
        imdb_ratinkg = tr.find('td',class_= 'ratingColumn imdbRating').strong.get_text()
        movie_ratings.append(imdb_ratinkg)
    # print(movie_ratings)

    #............................................................................. <a></a> tag 
        # link = tr.find('td',class_ = 'titleColumn').a
        # print(link)
        #............................................................................. <a href=''></a> link 
        link = tr.find('td',class_ = 'titleColumn').a["href"]
        # print(link)

        movie_link = 'https://www.imdb.com' + link
        movie_urls.append(movie_link)
    # print(movie_link)

    Top_movies = []
    details ={"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movies_ranks)):
        details['position'] = int(movies_ranks[i])
        details['name'] = str(movies_name[i])
        year_of_realease[i] = year_of_realease[i][1:5]
        details['year'] = int(year_of_realease[i])
        details['rating'] = float(movie_ratings[i])
        details['url'] = movie_urls[i]
        Top_movies.append(details.copy())

    return Top_movies
    # a = open("all_movies.json",'w')
    # json.dump(Top_movies,a,indent=4)

# pprint(scrape_top_list())
