class Noble:
    def __init__(self, points=3, cost={'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}):
        self.illustration = 0
        # self.cards_required = {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}
        self.cost = cost  # Number of cards required to be eligible for the Noble's visit
        self.points = points

    def __repr__(self):
        return 'Noble(points=' + str(self.points) + ', cost=' + str(self.cost) + ')'