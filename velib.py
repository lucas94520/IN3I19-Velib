# -*- coding: utf-8 -*-
import requests
import matplotlib.pyplot as plt # import module
import numpy as np
from scipy import stats
import json
import sys
import math

#Sources :
#https://perso.esiee.fr/~courivad/Python/
#http://docs.python-requests.org/en/master/
#http://www.jaimegil.me/2012/12/26/a-python-restful-api-consumer.html
#https://docs.python.org/3/library/json.html
#https://git-scm.com/book/fr/v1/Les-bases-de-Git-Travailler-avec-des-d%C3%A9p%C3%B4ts-distants
#https://www.science-emergence.com/Articles/Statistiques-Descriptives-%C3%A0-1-variable-Python/
#https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python



#Récuperation configuration
jsonConfig = "config.json"
with open(jsonConfig, mode="r", encoding="utf-8") as data_file:    
    config = json.load(data_file)

key = config['key']
contrat = config['contrat']
errors = config['errors']
url = "https://api.jcdecaux.com/vls/v1/stations?contract="+contrat+"&apiKey="+key

#Lancement de la requête au serveur
#https://api.jcdecaux.com/vls/v1/stations?contract=Paris&apiKey=75279893c9bfa89946178561b6ac75659dd7e997
response = requests.get(url)
#Analyse réponse serveur
code = str(response.status_code)
if (code in errors.keys()):
    print("Un probléme a été rencontré lors de la récupération des données : " + errors[code]);
    sys.exit()
if code != "200":
    print("Un probléme inconnu a été rencontré lors de la récupération des données.");
    sys.exit()
    
#Récuperation des données
data = response.json()
#Il faut produire a minima un histogramme et une représentation géolocalisée:
#histogramme : vous devez extraire les paramètres statistiques essentiels
#(moyenne, médiane, écart type, variance, ...)

freqEtVal = []
for station in data :
    if (station['status']=="OPEN") :
        freqEtVal.append(station['available_bikes'])
vmin = min(freqEtVal)
vmax = max(freqEtVal)
print("Moyenne : " + str(np.mean(freqEtVal)))
print("Mediane : " + str(np.median(freqEtVal)))
print("Min : " + str(vmin))
print("Max : " + str(vmax))
print("Ecart type : " + str(np.std(freqEtVal)))
print('Q1: ', stats.scoreatpercentile(freqEtVal, 25))
print('Q2: ', stats.scoreatpercentile(freqEtVal, 50))
print('Q3: ', stats.scoreatpercentile(freqEtVal, 75))

#Titre Histogram : nombre de vélo libre par station
pas = math.ceil((vmax-vmin)/9)
b = list(range(vmin,pas*10,pas))
print(b)



#représentation géolocalisée : selon l’étude, les données concerneront un pays,
#une ville, un quartier, etc... Il faudra organiser l’affichage de façon à ce 
#qu’il soit lisible, en particulier en limitant le nombre de données affichées.
