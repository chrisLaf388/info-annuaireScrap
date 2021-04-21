import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime

noms = []
adresses = []
tels = []
professions = []

# nom = ''
#Variable Boolean pour les boucles de pages et de lignes
# boutonPageSuivante = True
# finPage = True

#  Affiche la date / Pour nommer fichiers et dossier
# date = datetime.now()
# dateFichier = date.strftime('%Y-%m-%d %H-%M-%S')
# dateDossier = date.strftime('%Y-%m-%d')

# print ('Veuillez entrer le mot de recherche à scraper sans Caractères Spéciaux. Par exemple : "garagiste bouche du rhone"')
# #EXEMPLE
# # rechercheGoogle = "cbd+bouche+du+rhone"
# #input pour saisir la recherche
# rechercheGoogle = input()

# #replace ' ' par '+'
# rechercheGoogle = rechercheGoogle.replace(' ', '+')
# print(rechercheGoogle)

# Ouverture de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')

# Lien de la page formulaire
driver.get('https://www.infoannuaire.fr/pro/search?q=+&w=marseille&searchMode=pro')
time.sleep(2)

# Test recup un element
i=0
# while (i <11):
#     print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(i)+") .nom-prenom__response").text)
#     print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(i)+") .phonenumber").text)
#     print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(i)+") .adresse__response ").text)
#     print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child("+ str(i)+") .activite__response").text)
#     time.sleep(2)
i+=1
driver.find_element_by_xpath('/html/body/div[7]').click()

# trouver le nombre de page
nbPage=driver.find_element_by_xpath('/html/body/section/div[3]/section/section[2]/ul/li[1]').text
nbPage = (nbPage[-2]+ nbPage[-1])
print(nbPage)
driver.find_element_by_xpath('//*[@id="lastP"]').click()
time.sleep(1)
while(i<4):
    print('hello'+str(i))
    driver.find_element_by_xpath('//*[@id="nextP"]').click()

    time.sleep(1)
    print(driver.find_element(By.CSS_SELECTOR, ".response-aproche:nth-child(1) .nom-prenom__response").text)
    i+=1
#Si Cookies
# driver.find_element_by_xpath('//*[contains(text(), "J\'accepte")]').click()

# #Boucle continue tant qu'il existe le bouton Suivant
# while (boutonPageSuivante):
#     i = 1
#     finPage = True
#     #Boucle continue tant que nom n'a pas deux fois la même valeur
#     while(finPage):
#         try:
#             driver.find_element(By.CSS_SELECTOR, "div:nth-child("+str(i)+") > div > .uMdZh .rllt__details > div:nth-child(1)").click()
#             time.sleep(2)
#         except:
#             pass
#         try:
#             if (nom == driver.find_element(By.CSS_SELECTOR, ".qrShPb > span").text):
#                 finPage = False
#         except:
#             finPage = False
#
#         try:
#             print(driver.find_element(By.CSS_SELECTOR, ".qrShPb > span").text)
#             nom = driver.find_element(By.CSS_SELECTOR, ".qrShPb > span").text
#             time.sleep(1)
#             # adresse
#             adresse = driver.find_element(By.CSS_SELECTOR, ".Z1hOCe .LrzXr").text
#             print(driver.find_element(By.CSS_SELECTOR, ".Z1hOCe .LrzXr").text)
#             time.sleep(1)
#             # tel
#             tel = driver.find_element(By.CSS_SELECTOR, ".LrzXr span").text
#             print(driver.find_element(By.CSS_SELECTOR, ".LrzXr span").text)
#
#             if (tel != adresse) :
#                 noms.append(nom)
#                 adresses.append(adresse)
#                 tels.append(tel)
#             else :
#                 nomsBis.append(nom)
#                 telsBis.append(tel)
#
#         except:
#             print('null')
#
#         i +=1
#     time.sleep(2)
#     try :
#         driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
#         time.sleep(2)
#     except:
#         boutonPageSuivante = False
#
#
# # affichage en tableau avec adresse
# test = pd.DataFrame({
#     'Nom entreprise': noms,
#     'Adresse': adresses,
#     'Telephone': tels
# })
# # affichage en tableau sans adresse
# testBis = pd.DataFrame({
#     'Nom entreprise': nomsBis,
#     'Telephone': telsBis
# })
#
#
#
# #Chemin d'acces au donnée
# # username = os.environ['username']
# path = 'scraping/'+dateDossier+'/'
# #Création du dossier Scraping s'il n existe pas
# if not os.path.exists('scraping/'):
#     os.mkdir('scraping/')
#
# #Créer dossier date du jour s il n'existe pas
# if not os.path.exists(path):
#     os.mkdir(path)
#
# # creation de fichier csv
# test.to_csv(path+'scrap-'+rechercheGoogle+dateFichier+'.csv',sep="|", encoding='cp1252')
#
# # creation de fichier csv sans adresse
# testBis.to_csv(path+'scrap-'+rechercheGoogle+'PasAdresse'+dateFichier+'.csv',sep="|", encoding='cp1252')

#Fermer fenetre driver Chrome
# driver.quit();

# # Ouvrir un dossier
# path = os.path.realpath(path)
# os.startfile(path)

#fermer le programme
# sys.quit()
