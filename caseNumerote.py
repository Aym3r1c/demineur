# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:24:47 2024

@author: Formation
"""

from case import Case


class CaseNumerote(Case):

    def __init__(self, mines_voisines):
        super().__init__()
        self.mines_voisines = mines_voisines

    def reveler(self):
        if self.revelee or self.marquee:
            return
        self.revelee = True

    def __str__(self):
        if self.revelee:
            return str(self.mines_voisines)
        return super().__str__()
