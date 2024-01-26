from art import logo
from random import randint

# set difficulty to determine number of attempts
def set_difficulty():
  difficulty = ""
  while difficulty not in ["easy", "hard"]:
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  
# check user's guess with answer
def check_answer(guess, answer, attempts):
  is_correct = False
  if guess == answer:
    is_correct = True
    print(f"{guess} is correct! You win!")
  elif guess > answer:
    print(f"Too high, {attempts} attempts remaining.")
  else:
    print(f"Too low, {attempts} attempts remaining.")
  
  return is_correct

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  attempts = set_difficulty()
  print(f"You have {attempts} attempts remaining to guess the number.")

  continue_game = True
  while continue_game:
    guess = int(input("Make a guess: ")) 

    attempts -= 1

    # if user's guess is correct, end the game
    is_correct = check_answer(guess, answer, attempts)
    if is_correct:
      continue_game = False

    # if user runs out of attempts, end the game
    if attempts == 0 and continue_game == True:
      continue_game = False
      print(f"You've run out of attempts; the correct answer was {answer}. You lose.")

play_game()