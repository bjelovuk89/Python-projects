import random
import art
from game_data import data

print(art.logo)
first_name = random.choice(data)
second_name = random.choice(data)
if first_name == second_name:
    second_name = random.choice(data)["name"]

def comparison (a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
    a_or_b_def = input("Who has more followers? Type 'A' or 'B': ")
    return a_or_b_def

a_or_b = comparison(first_name, second_name)

current_score = 0
while True:
    if a_or_b.lower() == "a" and first_name['follower_count'] > second_name['follower_count']:
        # right choice option where "a" option is right one
        current_score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score {current_score}")
        first_name = first_name
        second_name = random.choice(data)
        if first_name == second_name:
            second_name = random.choice(data)["name"]
        a_or_b = comparison(first_name, second_name)
    elif a_or_b.lower() == "b" and first_name['follower_count'] < second_name['follower_count']:
        # right choice option where "b" option is right one, so "b" option becomes "a" option
        current_score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score {current_score}")
        first_name = second_name
        second_name = random.choice(data)
        if first_name == second_name:
            second_name = random.choice(data)["name"]
        a_or_b = comparison(first_name, second_name)
    else:
        #wrong option
        print(f"Sorry, that's wrong. Final score: {current_score}.")
        break