import requests
respons = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(respons)
# print(respons.status_code)
# print(respons.json())

#post request
data = {'userId': 1, 'id': 1, 'title':'for test'}
respons = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
# print(respons.status_code)
# print(respons.json())


#update request
data = {'userId': 1, 'id': 1, 'title':'for test(updated)'}
respons = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=data)
# print(respons.status_code)
# print(respons.json())

#deleted request
data = {'userId': 1, 'id': 1, 'title':'for test(updated)'}
respons = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(respons.status_code)
print(respons.json())