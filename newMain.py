import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime

noms = []
adresses = []
villes = []
tels = []


print('entrer un profession ou tapper + pour rechercher tous les metiers')
nomFamille = input()
print('tapper une ville, une region :')
ville = input()

# Ouverture de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')

# Lien de la page formulaire
driver.get('https://www.infoannuaire.fr/res/search?q='+nomFamille+'&w='+ville)
time.sleep(2)

# Test recup un element
j=1

driver.find_element_by_xpath('/html/body/div[7]').click()
try:
    # trouver le nombre de page
    nbPage=driver.find_element_by_xpath('/html/body/section/div[3]/section/section[2]/ul/li[1]').text
    nbPage = (nbPage[-2]+ nbPage[-1])
    print("page : " + nbPage)
    # driver.find_element_by_xpath('//*[@id="lastP"]').click()
    time.sleep(1)
except:
    nbPage=1
    pass
page=1
while(page<=int(nbPage)):
    # Test recup un element
    ligne = 1
    print('page en cour : '+str(page))
    while (ligne <11):
        try:
            print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .nom-prenom__response").text)
            nom = driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .nom-prenom__response").text
            print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .phonenumber").text)
            tel = driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .phonenumber").text
            print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .adresse__response div:nth-child(1)").text)
            print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .adresse__response div:nth-child(2)").text)
            adresse = driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .adresse__response div:nth-child(1)").text
            ville = driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(ligne)+") .adresse__response div:nth-child(2)").text


            time.sleep(2)
            noms.append(nom)
            tels.append(tel)
            adresses.append(adresse)
            villes.append(ville)
        except:
            pass
        ligne+=1
    try:
        driver.find_element_by_xpath('//*[@id="nextP"]').click()
        time.sleep(1)
    except:
        pass
    page+=1

test = pd.DataFrame({
    'Nom ': noms,
    'Adresse': adresses,
    'ville': villes,
    'Telephone': tels
})

test.to_csv('particulier'+ville+'.csv',sep="|", encoding='utf-8-sig')