from urllib import request, parse
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')
json_list = r.json()
for post in json_list:
    print (post["title"])



# def get_post(json_list):
#     for post in json_list:
#      return post["title"]
# print (get_post(json_list))

