from data.coin import Coin
from data.card import Card
from data.noble import Noble
from data.game import Game
import numpy as np

# Maybe change name from Coins to GemTokens
# https://en.wikipedia.org/wiki/Splendor_(game)
# https://startyourmeeples.com/2017/06/18/splendor-tactical-analysis-gem-distribution/
# Cards: http://danielsolisblog.blogspot.com/2014/05/the-time-to-point-ratio-in-splendor.html

game = Game(3)

print(game.deck)
print(game.nobles)
print(game.coins)