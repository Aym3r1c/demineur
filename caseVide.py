# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:25:00 2024

@author: Formation
"""

from case import Case


class CaseVide(Case):
    def __init__(self):
        super().__init__()

    def reveler(self):
        if self.revelee or self.marquee:
            return
        self.revelee = True
