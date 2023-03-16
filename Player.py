class Player:
    # constructeur de la classe
    def __init__(self, pseudo) -> None:
        self.__pseudo: str = pseudo
        self.__scores: dict[int, int] = {}
        self.__sortedScores: list[int] = []

    def __SortScores(self) -> None:
        if(self.__scores.__len__() == 0):
            return 0
        
        #stocke les scores par ordre croissant
        self.__sortedScores = sorted(self.__scores.values())

    def SetScore(self, songID: int, score: int) -> None:
        # don't add scores < 50
        if(score < 50):
            return
        
        # edit score if already in the list
        if(self.__scores.get(songID)):
            # don't save on last try if new score < last one
            if(self.__scores[songID] > score):
                return
            
            else:
                self.__scores[songID] = score

        # or create a new one if not
        else:
            self.__scores[songID] = score

        # on reclasse les scores après l'ajout
        self.__SortScores()

    def GetScoresTotal(self) -> int:
        if(self.__scores.__len__() == 0):
            return 0
        total: int = 0
        for score in self.__scores.values():
            total += score

        return total

    def GetScoresAverage(self) -> float:
        if(self.__scores.__len__() == 0):
            return 0
        return self.GetScoresTotal() / self.__scores.__len__()
    
    def DisplayBestScore(self) -> None:
        if(self.__scores.__len__() == 0):
            print("Il n'existe actuellement aucun score pour", self.__pseudo, "!")
            return 0
        
        # le premier score de la liste (classée préalablement)*
        bestScore: int = self.__sortedScores[self.__sortedScores.__len__() - 1]
        print("Meilleur score de", self.__pseudo, ":", bestScore)

    def DisplayWorseScore(self) -> None:
        if(self.__scores.__len__() == 0):
            print("Il n'existe actuellement aucun score pour", self.__pseudo, "!")
            return 0
        
        # le premier score de la liste (classée préalablement)*
        bestScore: int = self.__sortedScores[0]
        print("Plus mauvais score de", self.__pseudo, ":", bestScore)

    def DisplayAllScores(self) -> None:
        if(self.__scores.__len__() == 0):
            print("Il n'existe actuellement aucun score pour", self.__pseudo, "!")
            return 0
        
        # pour chaque musique on affiche l'ID de la musique et son score
        print("Scores de", self.__pseudo, "par musique :")
        for songID in self.__scores.keys():
            print("Musique", songID, ":", self.__scores[songID])