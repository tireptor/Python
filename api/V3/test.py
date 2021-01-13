import requests 

BASE = "http://127.0.0.1:5000/"

data = [{"likes":100,"name":"Vincent","views": 10000},{"likes":200,"name":"Tireptor","views": 15000},{"likes":300,"name":"Jean","views": 10055},
        {"likes":400,"name":"Paul","views": 25}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print (response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())