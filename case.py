# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:44:12 2024

@author: Formation
"""


class Case:
    def __init__(self):
        self.revelee = False
        self.marquee = False

    def reveler(self):
        pass

    def marquer(self):
        self.marquee = not self.marquee

    def __str__(self):
        if self.marquee:
            return "F"
        elif not self.revelee:
            return "."
        return " "
