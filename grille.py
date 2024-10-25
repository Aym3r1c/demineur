# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:44:35 2024

@author: Formation
"""

import random as rd

from case import Case
from caseMine import CaseMine
from caseNumerote import CaseNumerote
from caseVide import CaseVide


class Grille:
    def __init__(self, difficulté):
        self.taille, self.nb_mines = self.definir_difficulte(difficulté)
        self.cases = [[None for _ in range(self.taille)] for _ in range(self.taille)]
        self.générer_grille()
        self.cases_a_revelees = self.taille**2 - self.nb_mines

    def definir_difficulte(self, difficulté):
        if difficulté == "FACILE":
            return 8, 1  # taille, nb_mines    10 EN REALITE ET PAS 1
        elif difficulté == "MOYEN":
            return 16, 40
        elif difficulté == "DIFFICILE":
            return 24, 99

    def générer_grille(self):
        # Placer les mines
        mines = rd.sample(range(self.taille * self.taille), self.nb_mines)
        for index in mines:
            x, y = divmod(index, self.taille)
            self.cases[x][y] = CaseMine()

        # Placer les autres cases
        for i in range(self.taille):
            for j in range(self.taille):
                if self.cases[i][j] is None:
                    mines_voisines = self.compter_mines_voisines(i, j)
                    if mines_voisines == 0:
                        self.cases[i][j] = CaseVide()
                    else:
                        self.cases[i][j] = CaseNumerote(mines_voisines)

    def compter_mines_voisines(self, x, y):
        voisins, coords = self.obtenir_voisins(x, y)
        return sum(1 for voisin in voisins if isinstance(voisin, CaseMine))

    def obtenir_voisins(self, x, y):
        voisins = []
        coords = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.taille and 0 <= ny < self.taille:
                    voisins.append(self.cases[nx][ny])
                    coords.append([nx, ny])
        return voisins, coords

    def afficher_grille(self):
        for row in self.cases:
            print(" ".join(str(c) for c in row))


"""
class grille:
    
    def __init__(self):
        self.cases = [[Case() for _ in range(self.taille)] for _ in range(self.taille)]
    
    def creer_grille(self):
        # Placer mines aléatoirement
        mines = rd.sample(range(self.taille * self.taille), self.nb_mines)
        for index in mines:
            x, y = divmod(index, self.taille)
            self.cases[x][y].contient_mine = True
            
    def victoire(self):
        for row in self.cases:
            for case in row:
                if not case.contient_mine and not case.est_revelée:
                    return False
        return True
"""
