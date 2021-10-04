import requests
# API_key = '91590cb0-22fe-4950-9779-55834eee93ad'
# res = requests.get(f'https://api.thecatapi.com/v1/images/0XYvRd7oD?api_key={API_key}')
# open('cat.csv', 'wb').write(res.content)

# res1 = requests.get('https://api.thecatapi.com/v1/breeds')
# search_results = res1.json()   #Note can combine this into line above as shown in responses below
# #print(search_results)
# for item in search_results:
#     print(item['id'])

# res2 = requests.get('https://api.thecatapi.com/v1/images/search?breed_ids=abys').json()
# print(res2)
res3 = requests.get('https://cdn2.thecatapi.com/images/Kq8__jmkT.jpg')
open('cat.jpg', 'wb').write(res3.content)

import requests

TOKEN = 'MtiWtbxgWJBuDckpY2EOpp64g6QOVzwg7pk0zqPFNsFkdBIcqe3jD8bXk5EM8oVM97OUT5PQLeGlguVe'
url = 'https://www.nytimes.com/'
endpoint = 'https://api.opengraphr.com/api/og'
response = requests.get(endpoint, params={'api_token': TOKEN, 'url': url }).json()
#OR
#response = requests.get(https://api.opengraphr.com/v1/og?api_token={TOKEN}&url={url}).json()

print(response)