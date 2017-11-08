# -*- coding: utf-8 -*-
import requests
import matplotlib.pyplot as plt # import module
import numpy as np
from scipy import stats
#Sources :
#https://perso.esiee.fr/~courivad/Python/
#http://docs.python-requests.org/en/master/
#http://www.jaimegil.me/2012/12/26/a-python-restful-api-consumer.html
#https://docs.python.org/3/library/json.html
#https://git-scm.com/book/fr/v1/Les-bases-de-Git-Travailler-avec-des-d%C3%A9p%C3%B4ts-distants
#https://www.science-emergence.com/Articles/Statistiques-Descriptives-%C3%A0-1-variable-Python/


key = "75279893c9bfa89946178561b6ac75659dd7e997" #Info a mettre dans fichier config
contrat = "Paris" #Info a mettre dans fichier config
url = "https://api.jcdecaux.com/vls/v1/stations?contract="+contrat+"&apiKey="+key
#Récuperer des données
response = requests.get(url)
#https://api.jcdecaux.com/vls/v1/stations?contract=Paris&apiKey=75279893c9bfa89946178561b6ac75659dd7e997

#Analyse réponse serveur
#Condions à ameliorer => exporter dans un fichier config json avec dictionnaire
if(response.status_code == 200):#Si la requete est bien passée
    data = response.json() #Désérialiser/Décoder les données
elif(response.status_code == 301):
    print("redirection")
    exit
elif(response.status_code == 302):
    print("respectivement permanente et temporaire")
    exit
elif(response.status_code == 401):
    print("utilisateur non authentifié")
    exit
elif(response.status_code == 403):
    print("accès refusé")
    exit
elif(response.status_code == 404):
    print("page non trouvée")
    exit
elif(response.status_code == 500):
    print("erreur serveur")
    exit
elif(response.status_code == 503):
    print("erreur serveur")
    exit
else :
    print("erreur inconnue")
    exit



#print(type(data)) 
#<class 'list'>
#print("Nombre de stations : " + str(len(data))) 
#Nombre de stations : 772
#print(data)

#Il faut produire a minima un histogramme et une représentation géolocalisée:

#histogramme : vous devez extraire les paramètres statistiques essentiels
#(moyenne, médiane, écart type, variance, ...)
#Titre : nombre de vélo libre par station


freqEtVal = []
for station in data :
    if (station['status']=="OPEN") :
        freqEtVal.append(station['available_bikes'])
#print(freqEtVal)
print("Moyenne : " + str(np.mean(freqEtVal)))
print("Mediane : " + str(np.median(freqEtVal)))
print("Min : " + str(min(freqEtVal)))
print("Max : " + str(max(freqEtVal)))
print("Ecart type : " + str(np.std(freqEtVal)))
print('Q1: ', stats.scoreatpercentile(freqEtVal, 25))
print('Q2: ', stats.scoreatpercentile(freqEtVal, 50))
print('Q3: ', stats.scoreatpercentile(freqEtVal, 75))

valeurs = set(freqEtVal)


#représentation géolocalisée : selon l’étude, les données concerneront un pays,
#une ville, un quartier, etc... Il faudra organiser l’affichage de façon à ce 
#qu’il soit lisible, en particulier en limitant le nombre de données affichées.
