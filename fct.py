import os
import pickle
from random import choice
from donnees import *


def recupScore() :
    if os.path.exists(saveFile):  #Récupération de dict de scores si fichier existe
        scoreFile = open(saveFile,'rb')
        scorePeek = pickle.Unpickler(scoreFile)
        scores = scorePeek.load()
        scoreFile.close()

    else:
        scores = {}
    return scores

def saveScores(scores) :
    scoreFile = open(saveFile,'wb')
    scorePeek = pickle.Pickler(scoreFile)
    score = scorePeek.dump(scores)
    scoreFile.close()

def recupPlayerName() :
    playerName = input('Quel est votre nom de Joueur ?')
    playerName = playerName.capitalize()
    if playerName.isalnum == False or len(playerName)>5:
        print('Ce nom est invalide')
        return recupPlayerName() #appelle a nouveau la fct, agit comme continue
    else :
        return playerName

def recupLettre() :
    lettre = input('Quelle lettre jouez vous ?')
    lettre = lettre.lower()
    if lettre.isalpha() == False or len(lettre) > 1:
        print('La valeur saisie est invalide')
        return recupLettre()
    else :
        return lettre
    
def choixMot() :
    return choice(listeMots)


def motMasque(motcomplet, lettresTrouves):
    motMasque = ''
    for lettre in motcomplet :
        if lettre in lettresTrouves :
            motMasque += lettre
        else :
            motMasque += '*'
    return motMasque

