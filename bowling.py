class Bowling: 
    def __init__(self):   
        self._score = 0

    def score(self):
        return self._score

    def roll(self, pinesThrown):
        if type(pinesThrown) is not int or pinesThrown > 10 or pinesThrown < 0:
            raise Exception('Cannot throw this many pines')

        self._score += pinesThrown