class Coin:
    def __init__(self, quantity, colour):
        possible_colours = ['w', 'b', 'g', 'r', 'k', 'y']  # white', 'blue', 'green', 'red', 'black', 'yellow'
        self.illustration = 0
        self.quantity = quantity
        self.colour = colour

    def __repr__(self):
        return 'Coin(quantity=' + str(self.quantity) + ', colour=' + str(self.colour) + ')'