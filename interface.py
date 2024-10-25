# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:46:01 2024

@author: Formation
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
    
class Interface:
    
    
    def __init__():
        self.rien = None
    
    
    
if __name__ == "__main__":
    
    app = QApplication.instance() 
    if not app: # sinon on crée une instance de QApplication
        app = QApplication(sys.argv)
    
    # création d'une fenêtre avec QWidget dont on place la référence dans fen
    fen = QWidget()
    
    # on donne un titre à la fenêtre
    fen.setWindowTitle("Premiere fenetre")
    
    # on fixe la taille de la fenêtre
    fen.resize(500,250)
    
    # on fixe la position de la fenêtre
    fen.move(300,50)
    
    # la fenêtre est rendue visible
    fen.show()
    
    # exécution de l'application, l'exécution permet de gérer les événements
    app.exec_()