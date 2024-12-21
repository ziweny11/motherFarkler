import pickle
import os
from tqdm import tqdm
import itertools

# parse rules from rules.txt
def parse_rules(filename):
    rules = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = list(map(int, line.strip().split()))
            score = parts.pop()
            rule_key = [0]*6
            for die in parts:
                rule_key[die-1] += 1
            rule_key = tuple(rule_key) 
            rules[rule_key] = max(rules.get(rule_key, 0), score)
    return rules

def create_dp_table(rules, filename='dp_table.pkl'):
    # Check if the DP table already exists
    if os.path.exists(filename):
        print("Loading existing DP table from file...")
        with open(filename, 'rb') as file:
            dp = pickle.load(file)
        return dp

    dp = {}
    max_dice = 6
    total_combinations = [c for c in itertools.product(range(max_dice + 1), repeat=6) if sum(c) <= max_dice]
    print(len(total_combinations))
    total_combinations.sort(key=sum) 
    for counts in tqdm(total_combinations, desc="Calculating DP Table"):
        dp[counts] = 0
        for i in range(1, sum(counts)+1):
            for sub_counts in itertools.combinations_with_replacement(range(6), i):
                action = [0]*6
                for idx in sub_counts:
                    action[idx] += 1
                action_tuple = tuple(action)
                if action_tuple in rules:
                    remaining_counts = tuple(x - y for x, y in zip(counts, action_tuple))
                    if all(x >= 0 for x in remaining_counts):  # Valid remaining counts
                        dp[counts] = max(dp[counts], dp[remaining_counts] + rules[action_tuple])

    with open(filename, 'wb') as file:
        pickle.dump(dp, file)
        print(f"DP table computed and saved to {filename}")

    return dp

def check_if_any_action(action, dp):
    action_tuple = tuple(action)
    if action_tuple in dp:
        return True, dp[action_tuple]
    return False, 0

def generate_valid_actions(rules, filename='valid_actions.pkl'):
    """
    Generate all valid actions and their corresponding scores based on given rules,
    and store the result in a .pkl file if not already computed.
    """
    # Check if the valid actions file already exists
    if os.path.exists(filename):
        print("Loading valid actions from file...")
        with open(filename, 'rb') as f:
            return pickle.load(f)
    
    valid_actions = {}  # Dictionary to store actions and their corresponding scores
    
    # Get the scoring combinations (keys) from the rules
    scoring_combinations = list(rules.keys())
    
    # Generate all possible combinations of scoring sets
    for num_combinations in range(1, 7):  # Up to 6 combinations
        for combo in itertools.combinations_with_replacement(scoring_combinations, num_combinations):
            # Calculate the total dice counts by summing the individual counts from the combination
            total_counts = [0] * 6
            total_score = 0
            for action in combo:
                for i in range(6):
                    total_counts[i] += action[i]  # Sum the counts for each die face
                total_score += rules[action]  # Add the score for this combination
            
            # Ensure that we have a valid action (total dice <= 6)
            if sum(total_counts) <= 6:
                # Convert the total_counts into a tuple so it can be a dictionary key
                action_tuple = tuple(total_counts)
                
                # Store the action and its corresponding score (keep the max score if there are multiple ways to form it)
                if action_tuple not in valid_actions:
                    valid_actions[action_tuple] = total_score
                else:
                    valid_actions[action_tuple] = max(valid_actions[action_tuple], total_score)
    
    # Save the computed valid actions to a .pkl file for future use
    print(f"Saving valid actions to {filename}...")
    with open(filename, 'wb') as f:
        pickle.dump(valid_actions, f)
    
    return valid_actions


rules = parse_rules('rules.txt')

valid_actions = generate_valid_actions(rules)


dp_table = create_dp_table(rules)

action = [3, 1, 0, 0, 1, 0]
valid, score = check_if_any_action(action, dp_table)
print(f"Valid: {valid}, Score: {score}")
