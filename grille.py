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
        '''
        constructeur de la grille

        Parameters
        ----------
        difficulté : string
            difficulté choisie par le joueur.

        Returns
        -------
        None.

        '''
        self.taille, self.nb_mines = self.definir_difficulte(difficulté)
        self.cases = [[None for _ in range(self.taille)] for _ in range(self.taille)]
        self.générer_grille()
        self.cases_a_revelees = self.taille**2 - self.nb_mines

    def definir_difficulte(self, difficulté):
        '''
        donne les dimensions de la grille et le nombre de mines en fonction de la difficulté choisie

        Parameters
        ----------
        difficulté : string
            difficulté choisie par le joueur

        Returns
        -------
        tuple of int
            nombre de ligne/colonne et nombre de mines.

        '''
        if difficulté == "FACILE":
            return 8, 10  # taille, nb_mines
        elif difficulté == "MOYEN":
            return 16, 40
        elif difficulté == "DIFFICILE":
            return 24, 99

    def générer_grille(self):
        '''
        place les mines aléatoirement puis les cases vide et numérotée en fonction

        Returns
        -------
        None.

        '''
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
        '''
        compte le nombre de cases minées autour de la case sélectionnée

        Returns
        -------
        int
            nombre de mines voisines/numéro écrit sur la case

        '''      
        voisins, coords = self.obtenir_voisins(x, y)
        return sum(1 for voisin in voisins if isinstance(voisin, CaseMine))

    def obtenir_voisins(self, x, y):
        '''
        parcours tous les voisins (8) de la case choisie et les renvoie

        Parameters
        ----------
        x : int
            numéro de ligne de la case.
        y : int
            numéro de colonne de la case

        Returns
        -------
        voisins : list of Case
            liste des cases voisines.
        coords : list of tuple of int
            liste des coordonnées des cases voisines.

        '''
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
        '''
        mode console: affiche la grille sous forme de points

        Returns
        -------
        None.

        '''
        for row in self.cases:
            print(" ".join(str(c) for c in row))
