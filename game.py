#imports
import random

#variables
dice = [1, 2, 3, 4, 5, 6]

#rolls the dice once and returns a number 
def get_roll(dice, player):
    roll = dice[random.randint(0, len(dice)-1)]
    print(f"{player} rolled a {roll}")
    return roll

#adds 2 rolls together
def add_roll(roll):
    total_roll = roll + roll
    return total_roll

#checks if the total_roll is even
def check_even(total_roll):
    if total_roll % 2 == 0:
        return True
    else:
        return False

#checks if the player rolled the same 2 numbers
def check_double(roll1, roll2):
    if roll1 == roll2:
        return True

#adds the scores
def add_scores(scores):
    total = 0
    for i in range(len(scores)):
        total = total + scores[i]
    return total

#the game
def game(player1, player2, rounds, p1_score, p2_score, p1_scores, p2_scores):
    rounds = rounds - 1
    player1_roll1 = get_roll(dice, player1)
    player1_roll2 = get_roll(dice, player1)
    player2_roll1 = get_roll(dice, player2)
    player2_roll2 = get_roll(dice, player2)
    
    player1_total_roll = player1_roll1 + player1_roll2
    player2_total_roll = player2_roll1 + player2_roll2
    
    p1_score = p1_score + player1_total_roll
    p2_score = p2_score + player2_total_roll
    
    p1_even = check_even(player1_total_roll)
    p2_even = check_even(player2_total_roll)
    
    p1_double = check_double(player1_roll1, player1_roll2)
    p2_double = check_double(player2_roll1, player2_roll2)
    
    #player1
    if p1_even == True:
        p1_score +=10
    else:
        p1_score -=5
    
    if p1_double == True:
        p1_roll3 = get_roll(dice, player1)
        p1_score = p1_score + p1_roll3
    
    p1_scores.append(p1_score)
    
    #player2
    if p2_even == True:
        p2_score +=10
    else:
        p2_score -=5
    
    if p2_double == True:
        p2_roll3 = get_roll(dice, player2)
        p2_score = p2_score + p2_roll3
    
    p2_scores.append(p2_score)
    
    print(f"This round {player1} scored: {p1_score}")
    print(f"This round {player2} scored: {p2_score}")
    

#runs the game
def main():
    p1_score = 0
    p2_score = 0
    p1_scores = []
    p2_scores = []
    
    rounds = 5
    
    player1 = input("Please enter player1's name: ")
    player2 = input("Please enter player2's name: ")
    
    for _ in range(rounds):
        roll_ = input("Press enter to roll or q to quit: ")
        if roll_ == 'q':
            break
        
        game(player1, player2, rounds, p1_score, p2_score, p1_scores, p2_scores)
    
    print("Rounds Finished.")
    p1_total = add_scores(p1_scores)
    p2_total = add_scores(p2_scores)
    
    while p1_total == p2_total:
        p1_roll_again = get_roll(dice, player1)
        p2_roll_again = get_roll(dice, player2)
        p1_total += p1_roll_again
        p2_total += p2_roll_again
        return p1_total, p2_total
    print(f"{player1} scored {p1_total}.")
    print(f"{player2} scored {p2_total}.")
    
    if p1_total > p2_total:
        print(f"{player1} won the game.")
    else:
        print(f"{player2} won the game")


main()