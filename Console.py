# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 2020

@author: Este
"""

j1 = input("Quel est ton nom ? ")
chances = 8
score = 0
import random
liste_mots = open('mots.txt','r')
liste = liste_mots.readlines()
mot = (liste[random.randint(0,11)])
liste_mots.close()
longueur = len(mot)
barre = "_ "
resultat = mot[0] + " " + barre*(longueur-1)
print(resultat)
restant = longueur
citees=[]

while chances != 0 and restant != 0 :
    lettre = input("Choisir une lettre : ")
    if lettre in citees :
        print("Déjà donnée")
        print(resultat)
    elif lettre in mot :
        print("Oui")
        nombre = mot.count(lettre)
        resultat = resultat.split(" ")
        position = 0
        while nombre != 0 :
            position = int(mot.index(lettre,position + 1))
            resultat.pop(position)
            resultat.insert(position,lettre)
            nombre += -1
        resultat=" ".join(resultat)
        citees.append(lettre)
        restant += -1
        print(resultat)
    else :
        print("Non")
        citees.append(lettre)
        chances += -1
        print("Vie(s) restante(s) : ",chances)
        print(resultat)
        
if chances == 0 :
    print("Perdu")
elif restant == 0 :
    print("Gagné")
    score += 1
