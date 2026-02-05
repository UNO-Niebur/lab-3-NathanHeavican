#RPS.py
#Name: Nathan Heavican
#Date: 2-4-26
#Assignment: Lab 3
#Purpose: Create a playable Rock, Paper, Scissors game where the user selects Rock, Paper, or Scissors, the computer randomly selects a choice, the program determines the outcome, the user can choose to play again, and the program tracks wins, losses, and ties.
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  play = "yes"
  while play == "yes":
    #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  computer = random.choice(["R", "P", "S"])
  #Prompt the user for their RPS selection
  player = input("Choose your weapon (R, P, S): ")
  #Determine winner and state what happened to the user
  if computer == "R":
    print("The computer chose Rock.")
  elif computer == "P":
    print("The computer chose Paper.")
  else computer == "S":
    print("The computer chose Scissors.")

  if player == "R":
    print("You chose Rock.")
  elif player == "P":
    print("You chose Paper.")
  else player == "S":
    print("You chose Scissors.")
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
