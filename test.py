import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "tutorial", "views": "100"},
        {"likes": 20, "name": "rando", "views": "900"},
        {"likes": 50, "name": "zelda", "views": "1500"}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "video/2")
print(response.json())

input()

response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json)

input()

response = requests.get(BASE + "video/2")
print(response.json())