from urllib import request, parse
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')
json_list = r.json()
# for post in json_list:
    # print (post["title"])



def get_post():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    json_list = r.json()
    for post in json_list:
        print (post["title"])


def create_post():
    r = requests.post('https://jsonplaceholder.typicode.com/posts')
    title = input("Enter Post Title\n:")
    body = input("Write Post Body\n:")
    req = {'tittle':title, 'body':body}
    data = parse.urlencode(req).encode()
    request_ = requests.Request(r, data=data)
    return request_

print("Select operation.")
print("1.View Posts")
print("2.Create Posts")

choice = int(input("Enter choice(1/2): "))
if choice == 1:
    get_post()
elif choice == 2:
    print (create_post())
else:
    print("Invalid choice")


