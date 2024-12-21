import random
from collections import Counter
import pickle

class farkleGame():
    def __init__(self, dp_table, Player1, Player2):
        self.scores = {1: 0, 2: 0}
        self.whoseturn = 1
        self.maxscore = 10000
        self.dp_table = dp_table
        self.Player1 = Player1
        self.Player2 = Player2
        with open('valid_actions.pkl', 'rb') as file:  # Replace 'data.pkl' with your actual pickle file name
            valid_actions = pickle.load(file)
        self.valid_actions = valid_actions
    def roll_dice(self, num_dice):
        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        # Count the results
        roll_counts = Counter(rolls)
        return [roll_counts[i] for i in range(1, 7)]
    def score_turn(self):
        score_turn = 0
        num_dice = 6
        while num_dice > 0:
            throws = self.roll_dice(num_dice)

            #TODO: write a if check if farkle each time rolling a dice
            if self.dp_table[tuple(throws)] == 0:
                print("farkle!")
                score_turn = 0
                break
            pick, cont = self.Player1.decide_action(throws) if self.whoseturn == 1 else self.Player2.decide_action(throws)
            score_turn += self.valid_actions[tuple(pick)]
            if not cont:
                break
            num_dice -= sum(pick)
        return score_turn
    def run(self):
        while True:
            print(f"current score are {self.scores[1]} and {self.scores[2]}")
            leading_player = max(self.scores, key=self.scores.get)
            if self.scores[leading_player] >= self.maxscore:
                print(f"{leading_player} wins")
                break
            self.scores[self.whoseturn] += self.score_turn()
            self.whoseturn = 2 if self.whoseturn == 1 else 1





            

    
