class Item:
    def __init__(self, content):
        self.content = content
        self.IRI = 1
        self.EF = 2.5
        self.intStep = 1

    def updateIRI(self):
        if intStep == 1:
            self.IRI = 1
        elif intStep == 2:
            self.IRI = 6
        else:
            self.IRI *= EF

    def updateEF(self, quality):
        self.EF += 0.1 - (5-q) * (0.08 + (5-q)*0.02)

        if self.EF < 1.3:
            self.EF = 1.3

    def update(self, quality):
        assert quality >= 0 and quality <= 5
        self.updateEF(quality)

        if quality < 3:
            self.intStep = 1
        else:
            self.intStep += 1

        self.updateIRI()


class Scheduler:
    def __init__(self, items, intervals):
        self.items = items

