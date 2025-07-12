import random
from art import logo
from art import vs
from game_data import data
def compare(result, a, b):
    if result == "a":
        return a["follower_count"] > b["follower_count"]
    elif result == "b":
        return b["follower_count"] > a["follower_count"]
    else:
        return False
game_starter = random.choice(data)
score = 0
is_game_on = True 
while is_game_on:
    game_starter_2 = random.choice(data)
    while game_starter == game_starter_2:
        game_starter_2 = random.choice(data)
    print(logo)
    print(f"a: {game_starter["name"]} from {game_starter["country"]} a {game_starter["description"]}")   
    print(vs)
    print(f"b: {game_starter_2["name"]} from {game_starter_2["country"]} a {game_starter_2["description"]}") 
    result = input("Make a Guess a or b: ").lower()
    if compare(result, game_starter, game_starter_2):
        score += 1
        print("You win")
        print(f"Your new score is {score}")
        game_starter = game_starter_2
    else:
        print("You lose")
        print(f"Your final score is {score}")
        is_game_on = False


    