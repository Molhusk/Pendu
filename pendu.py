import os
import pickle
import random
from donnees import *
from fct import *

os.chdir('C:/Users/jason/Desktop/Python/Pendu')

scores = recupScore()

user = recupPlayerName()

print('Bonjour',user,'et bienvenue sur ce jeu du pendu !')

if user not in scores.keys():
    scores[user] = 0

continuerPartie = 'o'

while continuerPartie != 'n' :
    motMystere = choixMot()
    lettreTrouve = []
    motDecouvert = motMasque(motMystere, lettreTrouve)
    chances = vies
    while motMystere != motDecouvert and chances > 0 :
        print('Il vous reste {} chances, votre mot est :'.format(chances))
        print(motDecouvert)
        lettre = recupLettre()
        if lettre in lettreTrouve :
            print('Vous avez deja joue cette lettre')
        elif lettre in motMystere :
            lettreTrouve.append(lettre)
            print('bien joue')
        elif lettre not in motMystere :
            chances -= 1
            print('Cette lettre ne fait pas partie du mot')
        motDecouvert = motMasque(motMystere, lettreTrouve)
    if motMystere == motDecouvert :
        print('Bravo, bien joué ! Vous avez marqué {0} points'.format(chances))
        scores[user] += chances
    else :
        print('PENDU !! Dommage pour vous ;)')
    
    continuerPartie = input('Voulez vous rejouer une partie ? (O/N)')
    continuerPartie = continuerPartie.lower()

    saveScores(scores)

print('{0} quitte la partie avec un total de {1}'.format(user,scores))
        
        
        
