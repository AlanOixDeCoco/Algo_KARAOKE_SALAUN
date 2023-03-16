from os import system
import random

# import de la classe Player
from Player import Player

# ============== PROGRAMME ==============

# reset de la console pour plus de lisibilité
system("cls")

# les scores NE SONT PAS dépendants de l'existence d'un tableau des musiques,
# ce tableau est là pour rendre compte de ce qui peut être fait avec la classe Player
songs: list[str] = {
    "Musique 1",
    "Musique 2",
    "Musique 3",
    "Musique 4",
    "Musique 5",
}

# creation de 4 joueurs
players: list[Player] = [
    Player("Jean"),
    Player("Jacques"),
    Player("Joaquim"),
    Player("John")
]

# assignation de 50 scores aléatoires à chaque joueur (pour s'assurer du fonctionnement)
for player in players:
    for i in range(10):
        player.SetScore(random.randint(0, songs.__len__()), random.randint(0, 100))

for player in players:
    player.DisplayAllScores()
    player.DisplayBestScore()
    player.DisplayWorseScore()
    print("==========================")