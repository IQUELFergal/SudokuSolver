# Travail Pratique #2 - CSP – Résolution de Sudoku
# 
## _8INF846 – Intelligence Artificielle – Hiver 2022_
#
# Membres du groupe

Ce travail a été réalisé par quatre étudiants de l'UQAC :

- CLAVIER Thomas
- CRENN Damien
- CUILLANDRE Tony
- IQUEL Fergal

## Description

Dans le cadre du cours 8INF846 - Intelligence Artificielle, nous avons développé un solveur de Sudoku en utilisant le modèle CSP. L’utilisateur peut soumettre n’importe quelle grille de Sudoku dans un fichier texte. Le programme va ensuite le résoudre selon l’algorithme indiqué par l’utilisateur.


## Lancement et Utilisation

Il est nécessaire de spécifier un fichier texte contenant la grille de Sudoku initiale. Il est donc possible d'utiliser n'importe quelle grille en la modifiant au préalable. Il faut passer le path vers le fichier.txt en paramètre pour executer le programme. 

Le programme s'exécute avec la commande suivante :

```sh
python main.py True True Path
```
 
Il est possible de désactiver l'utilisation de l'algorithme AC-3 de cette manière :

```sh
python main.py False True Path
```

De la même manière on peut exécuter le code en désactivant la dégrée heuristique :

```sh
python main.py True False Path
```
