# import de la classe Player
from Player import Player

class Karaoke:
    def __init__(self, firstPlayer: Player) -> None:
        self.__players: list[Player] = []
        self.__players.append(firstPlayer)

        self.__songs: list[str] = {
            "Musique 1",
            "Musique 2",
            "Musique 3",
            "Musique 4",
            "Musique 5",
        }

    def AddPlayer(self, newPlayer: Player):
        if(self.__players.__contains__(newPlayer)):
            return
        self.__players.append(newPlayer)
    
    def RemovePlayer(self, playerIndex: int):
        if(playerIndex > self.__players.__len__() - 1):
            print("L'index de joueur spécifié n'existe pas !")
            return

        if(self.__players.__len__() < 2):
            print("Il n'y a qu'un joueur dans le karaoke !")
            return

        self.__players.pop(playerIndex)

    def BestTotal(self) -> Player:
        bestPlayer: Player = self.__players[0]
        for player in self.__players:
            if(player.GetScoresTotal() > bestPlayer.GetScoresTotal()):
                bestPlayer = player

        return bestPlayer
    
    def BestAverage(self) -> Player:
        bestPlayer: Player = self.__players[0]
        for player in self.__players:
            if(player.GetScoresAverage() > bestPlayer.GetScoresAverage()):
                bestPlayer = player

        return bestPlayer
    
    def BestScore(self) -> Player:
        bestPlayer: Player = self.__players[0]
        for player in self.__players:
            if(player.GetBestScore() > bestPlayer.GetBestScore()):
                bestPlayer = player

        return bestPlayer
    
    def BestScoreFor(self, song: str) -> Player:
        bestPlayer: Player = self.__players[0]
        for player in self.__players:
            if(player.GetScoreFor(song) > bestPlayer.GetScoreFor(song)):
                bestPlayer = player

        return bestPlayer