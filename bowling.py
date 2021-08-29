class Bowling: 
    def __init__(self):   
        self._score = 0
        self._frameScore = 0
        self._frameStage = 0
        self._spareBonusPending = False
        self._strikeBonusPending = False

    def score(self):
        return self._score

    def roll(self, pinesThrown):
        if self.amountOfPinesMustBeInteger(pinesThrown) or pinesThrown > 10 or pinesThrown < 0: 
            raise Exception('Cannot throw this many pines')

        if self._frameScore + pinesThrown > 10:
            raise Exception('Cannot throw this many pines')
        

        self._score += pinesThrown
        if self._spareBonusPending:
            self._spareBonusPending = False
            self._score += pinesThrown

        self._frameScore += pinesThrown
        self._frameStage += 1

        if self._frameStage == 2 and self._frameScore == 10:
            self._spareBonusPending = True

        if self._frameStage == 1 and self._frameScore == 10:
            self._strikeBonusPending = True

        if self._frameStage == 2 and self._strikeBonusPending:
            self._strikeBonusPending = False
            self._score += self._frameScore

        if self._frameScore == 10 or self._frameStage == 2:
            self._frameScore = 0
            self._frameStage = 0

    def amountOfPinesMustBeInteger(self, pinesThrown):
        return type(pinesThrown) is not int