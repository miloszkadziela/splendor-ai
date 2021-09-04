class Player:
    def __init__(self):
        self.coins = {'k': 0, 'w': 0, 'r': 0, 'b': 0, 'g': 0}  # Max Total = 10
        self.nobles = list()  # Receive them automatically
        self.cards = list()
        self.reserved_cards = list()  # Max 3

    def take_three_gem_tokens(self):
        pass

    def take_two_gem_tokens(self):
        pass

    def reserve_a_card(self):
        '''
        Take one gold token and reserve one development card.
        The maximum total number of reserved cards is three.
        If there is no gold token left, the player can reserve a card without the token.
        '''
        pass

    def purchase_card(self):
        pass

    def purchase_reserved_card(self):
        pass
