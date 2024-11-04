# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:44:12 2024

@author: Formation
"""


class Case:
    def __init__(self):
        '''
        constructeur d'une case

        Returns
        -------
        None.

        '''
        self.revelee = False
        self.marquee = False

    def reveler(self):
        '''
        fonction révéler redéfini dans les sous-classe

        Returns
        -------
        None.

        '''        
        pass

    def marquer(self):
        '''
        place un drapeau sur la case

        Returns
        -------
        None.

        '''
        self.marquee = not self.marquee

    def __str__(self):
        '''
        constructeur de l'aperçu d'une case

        Returns
        -------
        None.

        '''
        if self.marquee:
            return "F"
        elif not self.revelee:
            return "."
        return " "
