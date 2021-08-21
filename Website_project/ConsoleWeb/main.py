import requests
import json

url = "https://jkcremydjango.herokuapp.com/api/GetCremys"

data = requests.get(url)

#print(data.text)

cremys = json.loads(data.text)
#print(cremys)
#print(len(cremys))

print("Liste des cremys :")

for cremyModel in cremys:
    cremy = cremyModel['fields']
    print(cremy['nom'] + " : " + str(cremy['prix']) + "$" )
