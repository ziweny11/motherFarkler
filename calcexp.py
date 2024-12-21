# #calculate the expected score for throwing 0-6 dices
# import pickle
# import os
# from tqdm import tqdm
# import itertools

# def expected_score_given_num(num_dice, dp_table, max_dice_face=6):
#     if num_dice < 1 or num_dice > 6:
#         raise ValueError("Number of dice must be between 1 and 6")
    
#     # Generate all combinations of dice counts that sum to num_dice
#     combinations = [c for c in itertools.product(range(num_dice + 1), repeat=max_dice_face) if sum(c) == num_dice]
    
#     # Calculate the total score for these combinations
#     total_score = 0
#     for combo in combinations:
#         if combo in dp_table:
#             total_score += dp_table[combo]
#         else:
#             total_score += 0  # Assume a score of 0 if the combination is not in the table (unusual)
    
#     # Calculate the expected score as the average of the scores
#     if len(combinations) > 0:
#         return total_score / len(combinations)
#     return 0

# def gen_exp_list(dp_table):
#     res = []
#     for i in range(1, 7):
#         res.append(expected_score_given_num(i, dp_table)) 
#     return res

# with open("dp_table.pkl", 'rb') as file:
#     dp_table = pickle.load(file)

# print(gen_exp_list(dp_table))