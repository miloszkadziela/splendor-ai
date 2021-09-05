class Card:
    def __init__(self, colour, tier, points, cost={'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}):
        # possible_colours = ['white', 'blue', 'green', 'red', 'black']
        # Emerald  - GREEN
        # Sapphire - BLUE
        # Ruby     - RED
        # Diamond  - WHITE
        # Onyx     - BLACK
        # Gold     - YELLOW
        possible_colours = ['k', 'w', 'r', 'b', 'g']  # 'black', 'white', 'red', 'blue', 'green'
        self.colour = colour
        self.tier = tier  # 1, 2 or 3
        self.points = points
        self.cost = cost

        self.ID = 0  # Maybe give each card an ID, based on which a sprite will be displayed
        self.illustration = 0  # path to the sprite?

    def __repr__(self):
        return 'Card(points=' + str(self.points) + ', tier=' + str(self.tier) + ', colour=' + str(self.colour) + ', cost=' + str(self.cost)+ ')'