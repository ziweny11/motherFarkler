from game import farkleGame
from players import Player, HumanPlayer
from calcscore import parse_rules, create_dp_table

rules = parse_rules('rules.txt')
dp_table = create_dp_table(rules)

P1 = HumanPlayer()
P2 = HumanPlayer()
Game = farkleGame(dp_table, P1, P2)

Game.run()