# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 2020

@author: Este
"""

# Le jeu du pendu (Version Console) #

# Menu

import random
import tkinter as Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Tk
from tkinter import GROOVE
from tkinter import LEFT
from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import NW

import os
from random import randint

def Regle():
    print ("\n\t\t-- Règles du jeu --")
    print ("Vous avez 8 chances \n")

def CreationListeMots() : # Créer une liste de mots à partir du fichier .txt
    FichierMots = open("mots.txt","r")
    T = FichierMots.read().split("\r\n") # Transforme le fichier .txt  en liste de mots séparés par \n
    FichierMots.close()
    return T

def MotRandom() : # Donne un mot aléatoire parmis la liste de mots
    T = CreationListeMots()
    longueur = len(T)
    return T[randint(0,longueur-1)]

def Afficher_(mot) : # Fonction qui affiche la première lettre du mot et des underscores pour les autres lettres différentes 
    PremiereLettre = mot[0]
    AfficherLettresMot = PremiereLettre
    longueur = len(mot)
    m = 1
    for k in range(1,longueur) :
        if mot[k] == PremiereLettre :
            AfficherLettresMot += PremiereLettre
            m += 1
        else :
            AfficherLettresMot += " _"
    return (AfficherLettresMot,m)  

def TransfoListeChaine(liste) :
    n = len(liste)
    string = ""
    for k in range(n):
        string += str(liste[k])
    return string

def Pendu() :    
    mot = MotRandom()
    score = Afficher_(mot)[1]
    chances = 8
    longueur = len(mot)
    MotAffiche = list(Afficher_(mot)[0])
    LettresConnues =[mot[0]]
    print (TransfoListeChaine(MotAffiche))
    print ("Nombre de vies restantes :" + str(chances))
    while score != longueur and chances > 0 :
        c = 0
        x = input("Quelle lettre ?")
        for lettre in LettresConnues :
            if lettre == x :
                c += 1
        if c == 0 :
           LettresConnues.append(x)
           m = 0
           for k in range(1,longueur) :
              if x == mot[k] :
                  m += 1
                  MotAffiche.pop(2*k)
                  MotAffiche.insert(2*k,x)
           if m == 0 :
               chances += -1
           else :
               score += m
           print (TransfoListeChaine(MotAffiche))
           print ("Nombre de vies restantes : " + str(chances))
        else :
            print ("La lettre choisie a déjà été demandée")
            print (TransfoListeChaine(MotAffiche))
            
NewFenetre=Tk()
NewFenetre.title('Le Pendu')
NewFenetre.geometry('400x400+400+400')
BoutonLancer=Button(NewFenetre, text = 'Jouer', command = lambda: Afficher_(MotRandom()))
BoutonLancer.pack(side = LEFT,padx = 4, pady = 4)
NewFenetre.mainloop()

BoutonInstruction=Button(NewFenetre, text = 'Instructions', command = Regle)
BoutonInstruction.pack(side = LEFT, padx = 4, pady = 4)
BoutonQuitter=Button(NewFenetre, text = 'Quitter', command = NewFenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 4, pady = 4)

BoutonRejouer=Button(NewFenetre, text = 'Rejouer', command = Regle)
BoutonRejouer.pack(side = LEFT, padx = 4, pady = 4)

NewFenetre.mainloop()
   
Frame1=Frame(NewFenetre,relief=GROOVE)
Frame1.pack(side=LEFT,padx=40,pady=40)

NewFenetre=Tk()
NewFenetre.title('Le Pendu')
   
w=200
h=200
k=8

while k!=0:    
    can = Canvas(NewFenetre, width = w, height = h)
    Dessin=PhotoImage(file='pendu'+ str(k) +'.png')
    item = can.create_image(0,0,anchor=NW, image=Dessin)
    can.pack()
    print (item)
    k-=1

NewFenetre.mainloop()
