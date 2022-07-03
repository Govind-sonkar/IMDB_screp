# # import requests,json,os
# # from pprint import pprint
 
# # def group_by_year():
# #    c = {}
# #    a = open('all_movies.json','r')
# #    b= json.load(a)
# #    years = []
# #    for movie in b:
# #        if movie["year"] not in years:
# #            years.append(movie["year"])
# #    years.sort()
# #    # print(b)
  
# #    for i in years:
# #        movie_list=[]
# #        for movie in b:
# #            if i == movie["year"]:
# #                movie_list.append(movie)
# #        c[i]=movie_list
      
# #    return c
      
# # group_by_year()

# ###################################################   OR 

# import json
# from pprint import pprint

# with open("all_movies.json","r")as file:
#     movies=json.load(file)
#     # print(movies)

# def group_year(movies):
#     dict1={}
#     for i in movies:
#         years=(i["year"])
#         if years not in dict1:
#             dict1[years]=[]
#         else:
#              dict1[years].append(i)
#     # pprint(dict1)



# group_year(movies)