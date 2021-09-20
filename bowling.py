class Bowling: 
    def __init__(self):   
        self._frames = [[]]

    def score(self):
        score = 0
        for index, frame in enumerate(self._frames):
            score += sum(frame, 0)
            #first roll of frame bonuses
            if index > 1 and self.isStrike(self._frames[index-1]) or self.isSpare(self._frames[index-1]):
                score += frame[0]
            if index > 2 and self.isStrike(self._frames[index-1]) and self.isStrike(self._frames[index-2]):    
                score += frame[0]

            #second roll of frame bonuses
            if index > 1 and self.isStrike(self._frames[index-1]) and len(frame) == 2:
                score += frame[1]
        return score

    def isNotComplete(self, frame):
        return len(frame) == 1 and frame[0] < 10
    
    def isStrike(self, frame):
        return len(frame) == 1 and frame[0] == 10

    def isSpare(self, frame):
        return len(frame) == 2 and sum(frame, 0) == 10

    def roll(self, pinesThrown):
        lastFrame = self._frames[-1]
        if self.amountOfPinesMustBeInteger(pinesThrown) or pinesThrown > 10 or pinesThrown < 0: 
            raise Exception('Cannot throw this many pines')

        if self.isNotComplete(lastFrame) and lastFrame[0] + pinesThrown > 10:
            raise Exception('Cannot throw this many pines')
        
        if self.isNotComplete(lastFrame):
            lastFrame.append(pinesThrown)
        else:
            self._frames.append([pinesThrown])
        

    def amountOfPinesMustBeInteger(self, pinesThrown):
        return type(pinesThrown) is not int