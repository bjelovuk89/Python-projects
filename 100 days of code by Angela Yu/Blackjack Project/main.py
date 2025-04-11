import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def the_score(hand):
    score = 0
    for i in hand:
        score += i
    return score

def ace_check(hand, score):
    new_hand = []
    for i in hand:
        if i == 11 and score > 21:
            i = 1
        new_hand.append(i)
    return new_hand


while True:
    the_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if the_choice == "y":
        print(art.logo)
        player_hand = [random.choice(cards), random.choice(cards)]
        player_score = the_score(player_hand)
        player_hand = ace_check(player_hand, player_score)
        player_score = the_score(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")

        dealer_hand = [random.choice(cards), random.choice(cards)]
        dealer_score = the_score(dealer_hand)
        dealer_hand = ace_check(dealer_hand, dealer_score)
        dealer_score = the_score(dealer_hand)
        while dealer_score > 17:
            dealer_hand += [random.choice(cards)]
            dealer_score = the_score(dealer_hand)
            dealer_hand = ace_check(dealer_hand, dealer_score)
            dealer_score = the_score(dealer_hand)

        print(f"Comuter's first hand: {dealer_hand[0]}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        while another_card == "y" and player_score <= 21:
            player_hand.append(random.choice(cards))
            player_score += cards[-1]
            ace_check(player_hand, player_score)
            player_score = the_score(player_hand)
            print(f"Your cards: {player_hand}, current score: {player_score}")
            if player_score > 21 or another_card == "n":
                break
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_score > 21:
            print("You went over. You lose!")
            break
        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
        if player_score == dealer_score:
            print("It's a draw!")
        elif dealer_score > player_score and player_score <= 21:
            print("You lose!")
        else:
            print("You win!")

    if the_choice == "n":
        break
    else:
        print("Please use 'y' or 'n'!")