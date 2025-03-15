data = {'userId': 1, 'id': 1, 'title':'for test(updated)'}
respons = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(respons.status_code)
print(respons.json())