# -*- coding: utf-8 -*-
import requests
#Sources :
#http://docs.python-requests.org/en/master/
#http://www.jaimegil.me/2012/12/26/a-python-restful-api-consumer.html
#https://docs.python.org/3/library/json.html

#Récuperer des données
key = "75279893c9bfa89946178561b6ac75659dd7e997"
contrat = "Paris"
response = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract="+contrat+"&apiKey="+key)
data = ""
if( response.status_code == 200) :#Si la requete est bien passée
    data = response.json() #Désérialiser/Décoder les données
    print(data[0]['position'])
    print(len(data))
    #print(data)