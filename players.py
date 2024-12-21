
class Player():
    def __init__(self):
        pass
    def decide_action(self, cur_score, tar_score, throws):
        raise NotImplementedError("This method should be overridden by subclasses")


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def decide_action(self, cur_score, tar_score, throws):
        # Prompt the player to pick the dice they want to keep (size 6 list for dice 1-6)
        print(f"Throws: {throws}")
        
        # Ask the player to input the number of dice they want to keep in the format "3 0 0 0 0 0"
        while True:
            try:
                pick_input = input("Enter how many dice you want to keep for each number (1-6) as 'x x x x x x': ")
                pick = list(map(int, pick_input.split()))
                
                # Ensure the input is a list of six integers
                if len(pick) != 6:
                    print("Please enter exactly six values (one for each dice number from 1 to 6).")
                    continue
                
                # Validate that the pick values are within the allowable range (0 to throws[i])
                if all(0 <= pick[i] <= throws[i] for i in range(6)):
                    break
                else:
                    print("Please make sure your picks are within the range of dice rolled.")
            except ValueError:
                print("Invalid input. Please enter six integers separated by spaces.")

        # Ask whether to continue or stop (bank the score)
        while True:
            cont_input = input("Do you want to continue rolling? (y/n): ").lower()
            if cont_input == 'y':
                cont = True
                break
            elif cont_input == 'n':
                cont = False
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

        return pick, cont



class 