# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:24:35 2024

@author: Formation
"""

from case import Case

class CaseMine(Case):
    
    def __init__(self):
        super().__init__()
    
    def reveler(self):
        if self.revelee or self.marquee:
            return
        self.revelee = True
        #print("BOOM! Vous avez perdu.")
    
    def __str__(self):
        if self.revelee:
            return '*'
        return super().__str__()