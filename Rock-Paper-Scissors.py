"""
Program to play Rock Paper Scissors game

simple rules: rock beats scissors, paper beats rock, and scissors beat paper.
It a tie happens then you should play again
"""

import random
print("Welcome to Rock Paper Scissors game")
elem = ['rock','paper','scissors']
choice = random.choice(elem)
# print("Computer choice is", choice)
print("Enter your choice among - rock,paper,scissors")
player = input()

if player == choice:
    print("Game is a Tie; Play again")

if player == "rock":
    if choice == "paper":
        print("Computer Wins")
    else:
        print("Player Wins")

if player == "scissors":
    if choice == "paper":
        print("Player Wins")
    else:
        print("Computer Wins")

if player == "paper":
    if choice == "rock":
        print("Player Wins")
    else:
        print("Computer Wins")
