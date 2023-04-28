import random

def roll_the_dice(dice_num:int):
    dice = [1,2,3,4,5,6]
    results = []
    result_sum = 0
    for x in range(dice_num):
        roll = random.choice(dice)
        results.append(roll)
    for result in results:
        result_sum = result_sum + result
    return results, result_sum
        
