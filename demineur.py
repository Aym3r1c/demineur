# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:50:04 2024

@author: Formation
"""

import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from caseMine import CaseMine
from caseNumerote import CaseNumerote
from caseVide import CaseVide
from grille import Grille


class JeuDemineur(QtWidgets.QWidget):
    def __init__(self, mode):
        super().__init__()
        self.difficulté = None
        self.grille = None
        self.partie_terminée = False
        self.mode_drapeau = False
        self.mode = mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Démineur")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.boutons = []
        self.difficultyButton = QtWidgets.QPushButton("Choisir la difficulté")
        self.difficultyButton.clicked.connect(self.choisir_difficulte)
        self.layout.addWidget(self.difficultyButton)

        self.modeDrapeauButton = QtWidgets.QPushButton("Activer le mode Drapeau")
        self.modeDrapeauButton.clicked.connect(self.switch_mode_drapeau)
        self.layout.addWidget(self.modeDrapeauButton)

        self.gridLayout = QtWidgets.QGridLayout()
        self.layout.addLayout(self.gridLayout)

    def switch_mode_drapeau(self):
        self.mode_drapeau = not self.mode_drapeau
        if self.mode_drapeau:
            self.modeDrapeauButton.setText("Désactiver le mode Drapeau")
        else:
            self.modeDrapeauButton.setText("Activer le mode Drapeau")

    def choisir_difficulte(self):
        if self.mode == "ui":
            choix, ok = QtWidgets.QInputDialog.getItem(
                self,
                "Choisissez la difficulté",
                "Difficulté:",
                ["FACILE", "MOYEN", "DIFFICILE"],
                0,
                False,
            )
            if ok and choix:
                self.difficulté = choix
                self.demarrer()
        else:
            print("Choisissez la difficulté : ")
            print("1. Facile (8x8, 10 mines)")
            print("2. Moyen (16x16, 40 mines)")
            print("3. Difficile (24x24, 99 mines)")
            choix = input("Entrez le numéro correspondant à la difficulté : ")
            if choix == "1":
                self.difficulté = "FACILE"
            elif choix == "2":
                self.difficulté = "MOYEN"
            elif choix == "3":
                self.difficulté = "DIFFICILE"
            else:
                print("Choix invalide. Sélection de la difficulté par défaut : FACILE.")
                self.difficulté = "FACILE"

    def demarrerVC(self):
        self.choisir_difficulte()
        self.grille = Grille(self.difficulté)
        while not self.partie_terminée:
            self.grille.afficher_grille()
            x, y = map(int, input("Entrez les coordonnées (x, y) : ").split())
            action = input("Révéler (r) ou Marquer (m) ? ")
            if action == "r":
                self.reveler_case(x, y)
            elif action == "m":
                self.marquer_case(x, y)
            self.winOrLose()

    def demarrer(self):
        self.grille = Grille(self.difficulté)
        self.partie_terminée = False
        self.afficher_grille()

    def afficher_grille(self):
        self.clear_buttons()
        for x in range(self.grille.taille):
            row = []
            for y in range(self.grille.taille):
                button = QtWidgets.QPushButton()
                button.setFixedSize(40, 40)
                button.setStyleSheet("font-size: 18px;")
                button.clicked.connect(lambda checked, x=x, y=y: self.clic_case(x, y))

                self.gridLayout.addWidget(button, x, y)
                row.append(button)
            self.boutons.append(row)

    def clear_buttons(self):
        for button in self.boutons:
            for b in button:
                self.gridLayout.removeWidget(b)
                b.deleteLater()
        self.boutons = []

    def clic_case(self, x, y):
        if not self.mode_drapeau:
            self.reveler_case(x, y)
        if self.mode_drapeau:
            self.placer_drapeau(x, y)

    def placer_drapeau(self, x, y):
        case = self.grille.cases[x][y]
        if not case.revelee:
            case.marquer()
            self.update_buttons()

    def reveler_case(self, x, y):
        case = self.grille.cases[x][y]
        if case.marquee:
            return
        if not case.marquee:
            case.reveler()
            self.grille.cases_a_revelees -= 1
            print(self.grille.cases_a_revelees)
        if isinstance(case, CaseMine):
            self.partie_terminée = True
            # self.show_message("Vous avez perdu!")
        elif isinstance(case, CaseVide):
            self.revelation_case_vide(case, x, y)
        if self.mode == "ui":
            self.update_buttons()

    def revelation_case_vide(self, case, x, y):
        compteur = 0
        voisins, coords = self.grille.obtenir_voisins(x, y)
        # print(len(voisins))
        if voisins == []:
            return
        for ca in voisins:
            if ca.revelee:
                compteur += 1
                continue
            if not ca.revelee:
                ca.reveler()
                self.grille.cases_a_revelees -= 1
                print(self.grille.cases_a_revelees)
        if compteur == len(voisins):
            return

        for c in range(len(voisins)):
            voisin = voisins[c]
            if isinstance(voisin, CaseVide):
                new_x, new_y = coords[c]
                self.revelation_case_vide(
                    voisin, new_x, new_y
                )  # Réappelle la fonction récursivement

    def update_buttons(self):
        for x in range(
            self.grille.taille
        ):  # parcourir toutes les cases qui ont été découverts
            for y in range(self.grille.taille):
                case = self.grille.cases[x][y]
                button = self.boutons[x][y]
                if case.revelee:
                    if isinstance(case, CaseVide):
                        button.setText("")
                    elif isinstance(case, CaseNumerote):
                        button.setText(str(case.mines_voisines))
                    else:
                        button.setText(str("*"))
                    button.setEnabled(False)
                elif case.marquee:  # Vérifie si la case est marquée
                    button.setText("F")  # Affiche le drapeau
                else:
                    button.setText("")  # Case non révélée

        self.winOrLose()
        """
        if self.grille.cases_a_revelees == 0:
            self.partie_terminée = True
            self.show_message("Félicitations, vous avez gagné!")
        """

    def winOrLose(self):
        if self.grille.cases_a_revelees == 0:
            self.partie_terminée = True
            self.show_message("Félicitations, vous avez gagné!")

        elif self.partie_terminée:
            self.show_message("Dommage, vous avez perdu.")

    def show_message(self, message):
        if self.mode == "console":
            print(message)
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(message)
            msg.setWindowTitle("Démineur")
            msg.exec_()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    demineur = JeuDemineur("ui")
    demineur.show()
    sys.exit(app.exec_())

    ####### mode console
    # demineur = JeuDemineur("console")
    # demineur.demarrerVC()
