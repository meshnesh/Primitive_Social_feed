from urllib import request, parse
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')
json_list = r.json()
# for post in json_list:
    # print (post["title"])



# def get_post(json_list):
#     for post in json_list:
#      return post["title"]
# print (get_post(json_list))

def create_post():
    r = requests.post('https://jsonplaceholder.typicode.com/posts')
    title = input("Enter Post Title\n:")
    body = input("Write Post Body\n:")
    req = {'tittle':title, 'body':body}
    data = parse.urlencode(req).encode()
    request_ = requests.Request(r, data=data)
    return request_
    # resp = request.urlopen(request_)
    # return resp
print (create_post())

# print (json_list)
