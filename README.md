# demineur
## Comment jouer?
Après avoir cloner le projet sur votre ordinateur, ouvrez le fichier "demineur.py"
### Via la console
Assurer vous de decommenter les deux dernières lignes dans if __name__ == "__main__": et de commenter les quatres lignes suivantes 
- app = QtWidgets.QApplication(sys.argv)
- demineur = JeuDemineur("ui")
- demineur.show()
- sys.exit(app.exec_())

Exécutez le script. Les inputs et la grille s'affichent dans la console
### Via l'interface graphique
- Exécutez le script
- choisissez la difficulté (tant que ce n'est pas fait ça ne sert à rien d'appuyer sur le bouton "activer mode drapeau")
- La grille se crée.
- Un clic gauche sur une case la révéle. Pour placer un drapeau, il faut appuyer sur le bouton "activer mode drapeau" et cliquer sur la case. Pour pouvoir révéler des cases de nouveau, il suffit de réappuyer sur le bouton "déactiver mode drapeau"
- lorsqu'une partie se termine (victoire ou défaite), vous pouvez relancer une partie en appuyant sur "choisir la difficulté".
