import requests

response = requests.get('https://raw.githubusercontent.com/SCUACM/h4h-fullstack-workshop/main/data.json')

print(response.json())

dictionary = {
  "year": 2023, 
  "name": "Hack for Humanity 2023!", 
  "data": [1, 2, 3, 4, 5]
}

print(dictionary)