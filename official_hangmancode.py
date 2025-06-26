"""
Practical Lab 1, HANGMAN PROJECT
Yunior Azcona
6/14/2025
License: MIT
hangman_game.py
Description: This is a hangman game that prompts a player one to choose a word he would like the other person to guess.
Player Two will try to figure out the word with 6 attempts
"""

# To index a list of the hangman based on the amount of attempts
def for_attempts(attempts, all_attempts):
      print(all_attempts[attempts])
      return


# Lets the user know how many letters are in the word when they first start
def attempt_0(user_word, guesses):
      if len(guesses) == 0:
            print(f"_" * len(user_word) + "\n")
      return


# Lets the user know if their guess is in the word. If not, gives them wrong attempt
def letters(attempts, guessed, user_word):
      if guessed in user_word:
            print("That letter is in the word!\n")
      else:
            attempts += 1
      # Return attempts so that it can be increased
      return attempts


# Allows the game to check if the guessed letters in the word and option to win game once it is filled
def letters2(game, guesses, user_word, attempts, all_attempts):
      for letter in user_word:
            if letter in guesses:
                  game += letter
            else:
                  game += "_"
      if game == user_word:
            print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word.upper()}\n")
            for_attempts(attempts, all_attempts)
            exit()
      # Return the game function so it can be saved within a string to use
      return game


# Call back function for the main game code
def main():
      # Welcomes the Players
      print("Welcome to my Hangman Project")

      # This is wrong attempts printed out with body
      attempt0 = ("      |-----|\n" + "            |\n" + "            |\n" + "            |\n" + "-------------\n")
      attempt1 = ("      |-----|\n" + "      O     |\n" + "            |\n" + "            |\n" + "-------------\n")
      attempt2 = ("      |-----|\n" + "      O     |\n" + "      |     |\n" + "            |\n" + "-------------\n")
      attempt3 = ("      |-----|\n" + "      O     |\n" + "     /|     |\n" + "            |\n" + "-------------\n")
      attempt4 = ("      |-----|\n" + "      O     |\n" + "     /|\\    |\n" + "            |\n" + "-------------\n")
      attempt5 = ("      |-----|\n" + "      O     |\n" + "     /|\\    |\n" + "     /      |\n" + "-------------\n")
      attempt6 = ("      |-----|\n" + "      O     |\n" + "     /|\\    |\n" + "     / \\    |\n" + "-------------\n")

      # Print the hangman to show how many attempts they have at the start
      print(attempt0)
      # Prompt the user 1 to pick a word, added .lower to make it lower case, prevents wrong attempts for uppercase
      user_word = input("What would you like the word to be? \n").lower()
      # This is to hide the first players word
      print("\n" * 40)
      # Allows guesses to start at 0
      attempts = 0
      # List to allow guessed letters to go
      guesses = []
      # List so we can index the hangman based on attempts
      all_attempts = [attempt0, attempt1, attempt2, attempt3, attempt4, attempt5, attempt6]

      # While attempts doesn't equal 6, starts game and keeps in loop until they hit 6
      while attempts < 6:
            game = ""
            # Prints hangman based on incorrect attempts
            for_attempts(attempts, all_attempts)
            # Start to allow user to see how many letters in the word
            attempt_0(user_word, guesses)
            # Asks user what letter they want to guess
            guessed = input("What letter would you like to guess? \n")
            # Brings the guessed letter into guess_guess so it can be added to a list
            guess_guess = guessed
            guesses.append(guess_guess)
            # Allows the attempts to increase within the function so it doesn't stay at 0
            attempts = letters(attempts, guessed, user_word)
            letters(attempts, guessed, user_word)
            # Print the guesses made to help player 2
            print(guesses)
            letters2(game, guesses, user_word, attempts, all_attempts)
            # Makes game set to the letters correctly guessed and missed so it can be printed out
            game = letters2(game, guesses, user_word, attempts, all_attempts)
            print(game)
      # This is for when attempts hits 6 attempts aka the max attempts/body parts
      if attempts == 6:
            print(guesses)
            #New indicator for game to show letters correct and missed
            game = ""
            # Prints hangman to allow them to see where they finished off
            for_attempts(attempts, all_attempts)
            letters2(game, guesses, user_word, attempts, all_attempts)
            # Makes game set to the letters correctly guessed and missed so it can be printed out
            game = letters2(game, guesses, user_word, attempts, all_attempts)
            print(game)
            # Sorry you have lost prompt
            print(f"I am sorry, you have run out of attempts, the word was {user_word.upper()}\n")
            # Exits game when they have lost
            exit()
      return

main()
