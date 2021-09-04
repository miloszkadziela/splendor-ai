from data.coin import Coin
from data.card import Card
from data.noble import Noble

class Game:
    def __init__(self, n):
        self.number_of_players = n
        self.coins = self.init_coins()
        self.deck = self.deck()  # Deck
        self.nobles = self.init_nobles()

    def init_coins(self):
        # (self, quantity, colour):
        # white', 'blue', 'green', 'red', 'black', 'yellow'
        if self.number_of_players == 4:
            self.coins = [Coin(7, 'w'), Coin(7, 'b'), Coin(7, 'g'), Coin(7, 'r'), Coin(7, 'k'), Coin(5, 'y')]
        elif self.number_of_players == 3:
            self.coins = [Coin(5, 'w'), Coin(5, 'b'), Coin(5, 'g'), Coin(5, 'r'), Coin(5, 'k'), Coin(5, 'y')]
        elif self.number_of_players == 2:
            self.coins = [Coin(4, 'w'), Coin(4, 'b'), Coin(4, 'g'), Coin(4, 'r'), Coin(4, 'k'), Coin(5, 'y')]

    def init_deck(self):
        # TODO:
        # - Move the card definitions to a .txt file so that the deck can be easily extended/modified
        # - Add sprite/illustration name for each card
        self.deck = [
            # TIER 1 TIER 1 TIER 1 TIER 1 TIER 1 TIER 1 TIER 1 TIER 1
            # White TIER 1
            Card('w', 1, 0, {'w': 0, 'b': 3, 'g': 0, 'r': 0, 'k': 0}),
            Card('w', 1, 0, {'w': 0, 'b': 0, 'g': 0, 'r': 2, 'k': 1}),
            Card('w', 1, 0, {'w': 0, 'b': 2, 'g': 0, 'r': 0, 'k': 2}),
            Card('w', 1, 0, {'w': 0, 'b': 2, 'g': 2, 'r': 0, 'k': 1}),
            Card('w', 1, 0, {'w': 3, 'b': 1, 'g': 0, 'r': 0, 'k': 1}),
            Card('w', 1, 0, {'w': 0, 'b': 1, 'g': 1, 'r': 1, 'k': 1}),
            Card('w', 1, 0, {'w': 0, 'b': 1, 'g': 2, 'r': 1, 'k': 1}),
            Card('w', 1, 1, {'w': 0, 'b': 0, 'g': 4, 'r': 0, 'k': 0}),

            # Blue TIER 1
            Card('b', 1, 0, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 3}),
            Card('b', 1, 0, {'w': 1, 'b': 0, 'g': 0, 'r': 0, 'k': 2}),
            Card('b', 1, 0, {'w': 0, 'b': 0, 'g': 2, 'r': 0, 'k': 2}),
            Card('b', 1, 0, {'w': 1, 'b': 0, 'g': 2, 'r': 2, 'k': 0}),
            Card('b', 1, 0, {'w': 0, 'b': 1, 'g': 3, 'r': 1, 'k': 0}),
            Card('b', 1, 0, {'w': 1, 'b': 0, 'g': 1, 'r': 1, 'k': 1}),
            Card('b', 1, 0, {'w': 1, 'b': 0, 'g': 1, 'r': 2, 'k': 1}),
            Card('b', 1, 1, {'w': 0, 'b': 0, 'g': 0, 'r': 4, 'k': 0}),

            # Green TIER 1
            Card('g', 1, 0, {'w': 0, 'b': 0, 'g': 0, 'r': 3, 'k': 0}),
            Card('g', 1, 0, {'w': 2, 'b': 1, 'g': 0, 'r': 0, 'k': 0}),
            Card('g', 1, 0, {'w': 0, 'b': 2, 'g': 0, 'r': 2, 'k': 0}),
            Card('g', 1, 0, {'w': 0, 'b': 1, 'g': 0, 'r': 2, 'k': 2}),
            Card('g', 1, 0, {'w': 1, 'b': 3, 'g': 1, 'r': 0, 'k': 0}),
            Card('g', 1, 0, {'w': 1, 'b': 1, 'g': 0, 'r': 1, 'k': 1}),
            Card('g', 1, 0, {'w': 1, 'b': 1, 'g': 0, 'r': 1, 'k': 2}),
            Card('g', 1, 1, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 4}),

            # Red TIER 1
            Card('r', 1, 0, {'w': 3, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),
            Card('r', 1, 0, {'w': 0, 'b': 2, 'g': 1, 'r': 0, 'k': 0}),
            Card('r', 1, 0, {'w': 2, 'b': 0, 'g': 0, 'r': 2, 'k': 0}),
            Card('r', 1, 0, {'w': 2, 'b': 0, 'g': 1, 'r': 0, 'k': 2}),
            Card('r', 1, 0, {'w': 1, 'b': 0, 'g': 0, 'r': 1, 'k': 3}),
            Card('r', 1, 0, {'w': 1, 'b': 1, 'g': 1, 'r': 0, 'k': 1}),
            Card('r', 1, 0, {'w': 2, 'b': 1, 'g': 1, 'r': 0, 'k': 1}),
            Card('r', 1, 1, {'w': 4, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),

            # Black TIER 1
            Card('k', 1, 0, {'w': 0, 'b': 0, 'g': 3, 'r': 0, 'k': 0}),
            Card('k', 1, 0, {'w': 0, 'b': 0, 'g': 2, 'r': 1, 'k': 0}),
            Card('k', 1, 0, {'w': 2, 'b': 0, 'g': 2, 'r': 0, 'k': 0}),
            Card('k', 1, 0, {'w': 2, 'b': 2, 'g': 0, 'r': 1, 'k': 0}),
            Card('k', 1, 0, {'w': 0, 'b': 0, 'g': 1, 'r': 3, 'k': 1}),
            Card('k', 1, 0, {'w': 1, 'b': 1, 'g': 1, 'r': 1, 'k': 0}),
            Card('k', 1, 0, {'w': 1, 'b': 2, 'g': 1, 'r': 1, 'k': 0}),
            Card('k', 1, 1, {'w': 0, 'b': 4, 'g': 0, 'r': 0, 'k': 0}),

            # TIER 2 TIER 2 TIER 2 TIER 2 TIER 2 TIER 2 TIER 2 TIER 2
            # White TIER 2
            Card('w', 2, 1, {'w': 0, 'b': 0, 'g': 3, 'r': 2, 'k': 2}),
            Card('w', 2, 1, {'w': 2, 'b': 3, 'g': 0, 'r': 3, 'k': 0}),
            Card('w', 2, 2, {'w': 0, 'b': 0, 'g': 0, 'r': 5, 'k': 0}),
            Card('w', 2, 2, {'w': 0, 'b': 0, 'g': 0, 'r': 5, 'k': 3}),
            Card('w', 2, 2, {'w': 0, 'b': 0, 'g': 1, 'r': 4, 'k': 2}),
            Card('w', 2, 3, {'w': 6, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),

            # Blue TIER 2
            Card('b', 2, 1, {'w': 0, 'b': 2, 'g': 2, 'r': 3, 'k': 0}),
            Card('b', 2, 1, {'w': 0, 'b': 2, 'g': 3, 'r': 0, 'k': 3}),
            Card('b', 2, 2, {'w': 0, 'b': 5, 'g': 0, 'r': 0, 'k': 0}),
            Card('b', 2, 2, {'w': 5, 'b': 3, 'g': 0, 'r': 0, 'k': 0}),
            Card('b', 2, 2, {'w': 2, 'b': 0, 'g': 0, 'r': 1, 'k': 4}),
            Card('b', 2, 3, {'w': 0, 'b': 6, 'g': 0, 'r': 0, 'k': 0}),

            # Green TIER 2
            Card('g', 2, 1, {'w': 2, 'b': 3, 'g': 0, 'r': 0, 'k': 2}),
            Card('g', 2, 1, {'w': 3, 'b': 0, 'g': 2, 'r': 3, 'k': 0}),
            Card('g', 2, 2, {'w': 0, 'b': 0, 'g': 5, 'r': 0, 'k': 0}),
            Card('g', 2, 2, {'w': 0, 'b': 5, 'g': 3, 'r': 0, 'k': 0}),
            Card('g', 2, 2, {'w': 4, 'b': 2, 'g': 0, 'r': 0, 'k': 1}),
            Card('g', 2, 3, {'w': 0, 'b': 0, 'g': 6, 'r': 0, 'k': 0}),

            # Red TIER 2
            Card('r', 2, 1, {'w': 2, 'b': 0, 'g': 0, 'r': 2, 'k': 3}),
            Card('r', 2, 1, {'w': 0, 'b': 3, 'g': 0, 'r': 2, 'k': 3}),
            Card('r', 2, 2, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 5}),
            Card('r', 2, 2, {'w': 3, 'b': 0, 'g': 0, 'r': 0, 'k': 5}),
            Card('r', 2, 2, {'w': 1, 'b': 4, 'g': 2, 'r': 0, 'k': 0}),
            Card('r', 2, 3, {'w': 0, 'b': 0, 'g': 0, 'r': 6, 'k': 0}),

            # Black TIER 2
            Card('k', 2, 1, {'w': 3, 'b': 2, 'g': 2, 'r': 0, 'k': 0}),
            Card('k', 2, 1, {'w': 3, 'b': 0, 'g': 3, 'r': 0, 'k': 2}),
            Card('k', 2, 2, {'w': 5, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),
            Card('k', 2, 2, {'w': 0, 'b': 0, 'g': 5, 'r': 3, 'k': 0}),
            Card('k', 2, 2, {'w': 0, 'b': 1, 'g': 4, 'r': 2, 'k': 0}),
            Card('k', 2, 3, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 6}),

            # TIER 3 TIER 3 TIER 3 TIER 3 TIER 3 TIER 3 TIER 3 TIER 3
            # White TIER 3
            Card('w', 3, 3, {'w': 0, 'b': 3, 'g': 3, 'r': 5, 'k': 3}),
            Card('w', 3, 4, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 7}),
            Card('w', 3, 4, {'w': 3, 'b': 0, 'g': 0, 'r': 3, 'k': 6}),
            Card('w', 3, 5, {'w': 3, 'b': 0, 'g': 0, 'r': 0, 'k': 7}),

            # Blue TIER 3
            Card('b', 3, 3, {'w': 3, 'b': 0, 'g': 3, 'r': 3, 'k': 5}),
            Card('b', 3, 4, {'w': 7, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),
            Card('b', 3, 4, {'w': 6, 'b': 3, 'g': 0, 'r': 0, 'k': 3}),
            Card('b', 3, 5, {'w': 7, 'b': 3, 'g': 0, 'r': 0, 'k': 0}),

            # Green TIER 3
            Card('g', 3, 3, {'w': 5, 'b': 3, 'g': 0, 'r': 3, 'k': 3}),
            Card('g', 3, 4, {'w': 0, 'b': 7, 'g': 0, 'r': 0, 'k': 0}),
            Card('g', 3, 4, {'w': 3, 'b': 6, 'g': 3, 'r': 0, 'k': 0}),
            Card('g', 3, 5, {'w': 0, 'b': 7, 'g': 3, 'r': 0, 'k': 0}),

            # Red TIER 3
            Card('r', 3, 3, {'w': 3, 'b': 5, 'g': 3, 'r': 0, 'k': 3}),
            Card('r', 3, 4, {'w': 0, 'b': 0, 'g': 7, 'r': 0, 'k': 0}),
            Card('r', 3, 4, {'w': 0, 'b': 3, 'g': 6, 'r': 3, 'k': 0}),
            Card('r', 3, 5, {'w': 0, 'b': 0, 'g': 7, 'r': 3, 'k': 0}),

            # Black TIER 3
            Card('k', 3, 3, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),
            Card('k', 3, 4, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),
            Card('k', 3, 4, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}),
            Card('k', 3, 5, {'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0})
        ]

    def init_nobles(self):
        # TODO:
        # - Move the noble definitions to a .txt file so that the nobles can be easily extended/modified
        # - Add sprite/illustration name for each noble

        # (self, points=3, cost={'w': 0, 'b': 0, 'g': 0, 'r': 0, 'k': 0}):
        self.nobles = [
            # 4/4 Nobles
            Noble(3, {'w': 0, 'b': 0, 'g': 4, 'r': 4, 'k': 0}),
            Noble(3, {'w': 0, 'b': 0, 'g': 0, 'r': 4, 'k': 4}),
            Noble(3, {'w': 0, 'b': 4, 'g': 4, 'r': 0, 'k': 0}),
            Noble(3, {'w': 4, 'b': 0, 'g': 0, 'r': 0, 'k': 4}),
            Noble(3, {'w': 4, 'b': 4, 'g': 0, 'r': 0, 'k': 0}),

            # 3/3/3 Nobles
            Noble(3, {'w': 3, 'b': 0, 'g': 0, 'r': 3, 'k': 3}),
            Noble(3, {'w': 3, 'b': 3, 'g': 3, 'r': 0, 'k': 0}),
            Noble(3, {'w': 0, 'b': 0, 'g': 3, 'r': 3, 'k': 3}),
            Noble(3, {'w': 0, 'b': 3, 'g': 3, 'r': 3, 'k': 0}),
            Noble(3, {'w': 3, 'b': 3, 'g': 0, 'r': 0, 'k': 3})
        ]

    def choose_nobles(self):
        '''
        Randomly choose N+1 nobles
        '''

    def update_nobles(self):
        '''
        After each turn check if any player is eligible for a Noble.
        If multiple are available, let the player choose which one they want.
        Maybe move this function to Player instead

        If the player has earned enough development card gems to trigger a Noble points bonus,
        that player is "visited" by the Noble, and takes that Noble tile.

        - If player is eligible for visit by more than one Noble, player can choose the Noble.
        - Noble tile is not replaced by a new one.
        - Player gets to keep the Noble until the end of the game.
        '''
        pass

    def update_cards(self):
        '''
        If a development card is purchased, it is replaced from the top card on the respective deck.
        When the deck runs out, there are no more cards of that rank available.
        '''
        pass

    def draw_board(self):
        pass

print("Test Game")