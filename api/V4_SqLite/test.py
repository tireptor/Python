import requests 

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/1",{"views":21,"likes":20})
#response = requests.patch(BASE + "video/1") Display sans mettre à jour
print(response.json())