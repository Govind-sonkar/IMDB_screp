import json,requests
from pprint import pprint
from bs4 import BeautifulSoup

def scrape_movie_details(link):
    
    dict1 = {}
    get_movie_list_details = []

#................................ movies name ?
    page  = requests.get(link)
    soup = BeautifulSoup(page.text,"html.parser")
    movie_name = soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.text
    # print(movie_name)
#................................... Director ?

    Director = soup.find('li',class_="ipc-metadata-list__item")
    # print(Director)

    Dir_name = Director.find_all('a')
    Director_names = []
    for i in Dir_name:
        b= (i.text)
        Director_names.append(b)
    # print(Director_names)

#.......................................... counrty name ?

    co =soup.find('li',attrs={"data-testid":"title-details-origin"})
    counrty_name = co.find('a').text
    # print(counrty_name)

#............................................... language ?

    movies_language = []
    lan = soup.find('li',attrs={"data-testid":"title-details-languages"})
    language = lan.find('a').text
    # print(language.text)
    movies_language.append(language)
    # print(movies_language)

#........................................... poster image /

    poster_image = soup.find('img',class_="ipc-image")["src"]
    # print(poster_image)

#......................................... Bio ?

    Bio_div = soup.find('span',class_="GenresAndPlot__TextContainerBreakpointXL-sc-cum89p-2 eqbKRZ").text
    # print(Bio_div)

#................................... .................................run time ?

    RunTime = soup.find("li",attrs={"data-testid":"title-techspec_runtime"})
    # print(RunTime)

    run_time = RunTime.find('div',class_="ipc-metadata-list-item__content-container").text
    ran = run_time.replace(' hours', '').replace(' minutes', '').replace(' hour', '').replace(' minute', '').replace(' h', '').replace(' m', '')
    sp = ran.split(' ')
    t_time = 0
    if len(sp)==2:
        t_time += int(sp[0])*60
        t_time += int(sp[1])
    elif len(sp)==1:
        if 'h' in run_time:
            t_time += int(sp[0])*60
        else:
            t_time += int(sp[0])
        
    # print(t_time)
    
#..................................................................... genre ?

    genre_movies = []
    genre1 = soup.find('li',attrs={'data-testid':"storyline-genres"})
    g = genre1.find('a').text
    # print(g)
    genre_movies.append(g)
    # print(genre_movies)
#...................................... movies_details ?


    dict1['name']= movie_name
    dict1['director']= Director_names
    dict1['country']= counrty_name
    dict1['language']= movies_language
    dict1['poster_image_url']= poster_image
    dict1['bio']= Bio_div
    dict1['runtime']= t_time
    dict1['genre']= genre_movies

    return dict1

    get_movie_list_details.append( dict1)
        
        # a = open('task4.json','w')
        # json.dump(get_movie_list_details,a, indent=4)


# pprint(scrape_movie_details("https://www.imdb.com/title/tt8176054/"))