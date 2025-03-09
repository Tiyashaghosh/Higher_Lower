from art import logo,vs
from game_data import data
import random

def compare(ch,c1,c2,):
    if ch == 'a':
        if c1 > c2:
            return True
        elif c1 < c2:
            return False
    elif ch == 'b':
        if c1 < c2:
            return True
        elif c1 > c2:
            return False

game_over = False
# Set score to 0
score = 0
# Randomly choose two values from the dictionary
compare1 = random.choice(data)
compare2 = random.choice(data)
if compare1 == compare2:
    compare2 = random.choice(data)
while game_over is False :
    # Print the logo
    print(logo)
    #Print score
    if score != 0 :
        print(f"You are right! Correct score : {score}")
    # Print the first data
    print(f"Compare A: {compare1['name']}, a {compare1['description']}, from {compare1['country']}")
    print(vs)
    # Print the second data
    print(f"Against B : {compare2['name']}, a {compare2['description']}, from {compare2['country']}")
    # Ask the user to guess who has more followers
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    result = compare(choice,compare1['follower_count'],compare2['follower_count'])
    if result is True :
        compare1 = compare2
        score += 1
        compare2 = random.choice(data)
        game_over = False

    elif result is False:
        game_over = True

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")

# import os
# import random
# from art import logo, vs
# from game_data import data
#
# def clear_screen():
#     """Clears the console screen."""
#     os.system('cls' if os.name == 'nt' else 'clear')
#
# def format_data(account):
#     """Takes an account dictionary and returns the formatted string."""
#     return f"{account['name']}, a {account['description']}, from {account['country']}"
#
# def compare(choice, c1, c2):
#     """Compares follower counts based on the user's choice."""
#     return (choice == 'a' and c1 > c2) or (choice == 'b' and c1 < c2)
#
# def get_random_account(exclude=None):
#     """Gets a random account, ensuring it's not the excluded one."""
#     account = random.choice(data)
#     while account == exclude:
#         account = random.choice(data)
#     return account
#
# def play_game():
#     """Main game logic."""
#     clear_screen()
#     print(logo)
#
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#
#     while game_should_continue:
#         account_b = get_random_account(exclude=account_a)
#
#         clear_screen()
#         print(logo)
#         print(f"Compare A: {format_data(account_a)}")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}")
#
#         # Get user's choice and validate it
#         choice = input("Who has more followers? Type 'A' or 'B': ").lower()
#         while choice not in ['a', 'b']:
#             choice = input("Invalid input. Please type 'A' or 'B': ").lower()
#
#         is_correct = compare(choice, account_a['follower_count'], account_b['follower_count'])
#
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}")
#             account_a = account_b
#         else:
#             print(f"Sorry, that's wrong. Final score: {score}")
#             game_should_continue = False
#
# # Game loop with replay option
# while True:
#     play_game()
#     replay = input("Do you want to play again? Type 'yes' or 'no': ").lower()
#     if replay != 'yes':
#         print("Thanks for playing!")
#         break
