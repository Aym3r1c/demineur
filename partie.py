# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:45:02 2024

@author: Formation
"""


class partie:
    
    def __init__(self, difficulte):
        self.difficulte = difficulte
    
    def commencer_partie(self):
        if self.difficulte == 'facile':
            taille = 10
            bombe = 10
            create_grille(taille, bombe)
        if self.difficulte == 'moyen':
            taille = 20
            bombe = 20
            create_grille(taille, bombe)
        if self.difficulte == 'difficile':
            taille = 30
            bombe = 30
            create_grille(taille, bombe)


            