import random
from art import logo

print(logo)
number=random.choice(range(100))


def start_the_game(difficulty_range):
  tries=difficulty_range
  print(f"You have {tries}:")
  guessed_number=int(input("Make a guess\n"))
  for i in range(difficulty_range+1):
    tries-=1
    if tries > 0:
      if guessed_number==number:
        print(f"You got it! The answer was {number}.")
        game_over=True
        return game_over
      elif guessed_number > number:
        print("Too high.")
        print(f"You have {tries} attempts remaining to guess the number.")
        guessed_number=int(input("Guess again.\n"))
      elif guessed_number < number:
        print("Too low.")
        print(f"You have {tries} attempts remaining to guess the number.")
        guessed_number=int(input("Guess again.\n"))
    else:
      print(f"You've run out of guesses. The correct answer was {number} you lose..")
      game_over=True
      return game_over



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
valid_choice=True

while valid_choice:
  if difficulty_choice == "easy":
    difficulty=10
    valid_choice=False
  elif difficulty_choice == "hard":
    difficulty=5
    valid_choice=False
  else:
    difficulty_choice=input("Invalid entery! Please type 'easy' or 'hard' for difficulty level: ").lower()

game_over=False

while not game_over:
  start_the_game(difficulty)
  game_over=start_the_game
