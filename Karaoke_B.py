from os import system
import random

# import de la classe Player*
from Player import Player
from Karaoke import Karaoke

# ============== PROGRAMME ==============

# reset de la console pour plus de lisibilité
system("cls")

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
        player.SetScore(random.randint(0, 10), random.randint(0, 100))

karaoke = Karaoke(players[0])
for player in players:
    karaoke.AddPlayer(player)

karaoke.AddPlayer(Player("Jean"))

karaoke.RemovePlayer(1)
karaoke.RemovePlayer(1)

print("Joueur avec le meilleur total :")
karaoke.BestTotal().DisplayAllScores()