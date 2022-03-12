scores = {}
highScores = {}

class scoreKeeping:
    def __init__(self, playerName, playerScore):
        self.playerName = playerName
        self.playerScore = playerScore
  
    def sortScores():
        global scores
        #global highScores
        with open("scores.txt") as f:
            for line in f:
                (k, v) = line.split()
                scores[k] = int(v)
        valueList = list(scores.values())
        keyList = list(scores.keys())
        topScores = 5
        sortedList = sorted(valueList, reverse=True)
        sortedList = sortedList[:topScores]
        for score in sortedList:
            sortedList.index(score)
            i = valueList.index(score)
            highScores.update({keyList[i]: valueList[i]})
        print(highScores)
        

    def loadScores():
        pass
        #global scores
        #with open("scores.txt") as f:
           # for line in f:
          #      (k, v) = line.split()
           #     scores[k] = int(v)
        #print("loadScores ", scores)
    
    
    def addScore(playerName, playerScore):
        global scores
        scores.update({playerName: playerScore})

    def saveScores():
        with open ("scores.txt", 'w') as f:
            for key, value in scores.items():
                f.write('%s %s\n' % (key, value))

scoreKeeping.sortScores()
#scoreKeeping.addScore("Bill", 14)
scoreKeeping.saveScores()


