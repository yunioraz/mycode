"""
Practical Lab 1, HANGMAN PROJECT
Yunior Azcona
6/14/2025
License: MIT
hangman_game.py
Description: This is a hangman game that prompts a player one to choose a word he would like the other person to guess.
Player Two will try to figure out the word with 6 attempts
"""

#Welcomes the Players
print("Welcome to my Hangman Project")

#This is zero wrong attempts
attempt0 = ("      |-----|\n"
      "            |\n"
      "            |\n"
      "            |\n"
      "-------------\n")
#This is one wrong attempt
attempt1 = ("      |-----|\n"
      "      O     |\n"
      "            |\n"
      "            |\n"
      "-------------\n")
#This is two wrong attempts
attempt2 = ("      |-----|\n"
      "      O     |\n"
      "      |     |\n"
      "            |\n"
      "-------------\n")
#This is three wrong attempts
attempt3 = ("      |-----|\n"
      "      O     |\n"
      "     /|     |\n"
      "            |\n"
      "-------------\n")
#This is four wrong attempts
attempt4 = ("      |-----|\n"
      "      O     |\n"
      "     /|\\    |\n"
      "            |\n"
      "-------------\n")
#This is five wrong attempts
attempt5 = ("      |-----|\n"
      "      O     |\n"
      "     /|\\    |\n"
      "     /     |\n"
      "-------------\n")
#This is six wrong attempts
attempt6 = ("      |-----|\n"
      "      O     |\n"
      "     /|\\    |\n"
      "     / \\    |\n"
      "-------------\n")

#Print the hangman to show how many attempts they have
print(attempt0)
#Prompt the user 1 to pick a word, added .lower to make it lower case, prevents wrong attempts for making a letter uppercase or lower
user_word = input("What would you like the word to be? \n").lower()
#This is to hide the first players word
print("\n" * 40)
#User starts off with 0 attempts
attempts = 0
#Max attempts at 6,because of 6 limbs
max_attempts = 6
#Allows guesses to start at 0
guesses = []
#While attempts doesnt equal 6, start game
while attempts != max_attempts:
      #Starts game at 0 attempts
      if attempts == 0:
            #Gives us a starting point for game to add to
            game = ""
            #Prints the hangman bar
            print(attempt0)
            #Allows us to see how long the word given is
            if len(guesses) == 0:
                  print(f"_" * len(user_word) + "\n")
            #Lets user guess
            guess = input("What letter would you like to guess? \n").lower()
            #Every letter guessed will be added to guesses
            guesses += guess
            #If the letter is inside the word, print that it is
            if guess in user_word:
                  print("That letter is in the word!\n")
            #If not in the word, give them a wrong attempt
            else:
                  attempts += 1
            print(guesses)
            #Got help from chatgpt, for every letter in the word, shows user their attempt or tells them they're wrong with underscores
            for letter in user_word:
                  if letter in guesses:
                        game += letter
                        #This allows user to attempt to guess full word
                        if game == user_word:
                              #Because an error I noticed, I added this to prevent extra letters from giving the player an instant win
                              if len(guess) > len(user_word):
                                    print("Seems you added one too many letters\n")
                              #If they guess full word in one go
                              else:
                                    print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word}\n")
                                    #Exit the game if they completed it
                                    exit()
                  #This shows them the missing letters they have
                  else:
                        game += "_"
            #Prints the guessed letters and missed letters
            print(game)
      #When the amount of attempts hits 1, start this loop
      if attempts == 1:
            #New indicator for guessed letters and unguessed so it does not double onto the first loop (got this tip from Chat GPT)
            game = ""
            #Prints head for hangman
            print(attempt1)
            guess = input("What letter would you like to guess? \n")
            #Adds the guess to guess to be saved
            guesses += guess
            #Let's player 2 know they got a letter correct
            if guess in user_word:
                  print("That letter is in the word!\n")
            #If incorrect, adds one to the attempts and shows them their guesses
            else:
                  attempts += 1
            print(guesses)
            #Got help from chatgpt, for every letter in the word, shows user their attempt or tells letter they're missing
            for letter in user_word:
                  if letter in guesses:
                        #For the letters in user_word, if it shows up in guesses, add it to game
                        game += letter
                        #Chance to guess full word or let them win when finished
                        if game == user_word:
                              #Due to error when you guess full word and add letter, to prevent them from winning.
                              if len(guess) > len(user_word):
                                    print("Seems you added one too many letters\n")
                              #If they win
                              else:
                                    print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word}\n")
                                    #Ends game
                                    exit()
                  else:
                        game += "_"
            print(game)
      #Due to the fact this is just a replica off of If attempts == 1, they'll be fewer comments explaining
      if attempts == 2:
            game = ""
            print(attempt2)
            guess = input("What letter would you like to guess? \n").lower()
            guesses += guess
            if guess in user_word:
                  print("That letter is in the word!\n")
            else:
                  attempts += 1
            print(guesses)
            #got help from chatgpt, for every letter in the word, shows user their attempt or tells them they're wrong
            for letter in user_word:
                  if letter in guesses:
                        game += letter
                        if game == user_word:
                              if len(guess) > len(user_word):
                                    print("Seems you added one too many letters\n")
                              else:
                                    print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word}\n")
                                    exit()
                  else:
                        game += "_"
            print(game)
      # Due to the fact this is just a replica off of If attempts == 1, they'll be fewer comments explaining
      if attempts == 3:
            game = ""
            print(attempt3)
            guess = input("What letter would you like to guess? \n").lower()
            guesses += guess
            if guess in user_word:
                  print("That letter is in the word!\n")
            else:
                  attempts += 1
            print(guesses)
            #got help from chatgpt, for every letter in the word, shows user their attempt or tells them they're wrong
            for letter in user_word:
                  if letter in guesses:
                        game += letter
                        if game == user_word:
                              if len(guess) > len(user_word):
                                    print("Seems you added one too many letters\n")
                              else:
                                    print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word}\n")
                                    exit()
                  else:
                        game += "_"
            print(game)
      # Due to the fact this is just a replica off of If attempts == 1, they'll be fewer comments explaining
      if attempts == 4:
            game = ""
            print(attempt4)
            guess = input("What letter would you like to guess? \n").lower()
            guesses += guess
            if guess in user_word:
                  print("That letter is in the word!\n")
            else:
                  attempts += 1
            print(guesses)
            #Got help from chatgpt, for every letter in the word, shows user their attempt or tells them they're missing a letter
            for letter in user_word:
                  if letter in guesses:
                        game += letter
                        if game == user_word:
                              if len(guess) > len(user_word):
                                    print("Seems you added one too many letters\n")
                              else:
                                    print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word}\n")
                                    exit()
                  else:
                        game += "_"
            print(game)
      #Due to the fact this is just a replica off of ff attempts == 1, they'll be fewer comments explaining
      if attempts == 5:
            game = ""
            print(attempt5)
            guess = input("What letter would you like to guess? \n").lower()
            guesses += guess
            if guess in user_word:
                  print("That letter is in the word!\n")
            else:
                  attempts += 1
            print(guesses)
            #Got help from chatgpt, for every letter in the word, shows user their attempt or tells them they're missing a letter
            for letter in user_word:
                  if letter in guesses:
                        game += letter
                        if game == user_word:
                              if len(guess) > len(user_word):
                                    print("Seems you added one too many letters\n")
                              else:
                                    print(f"CONGRATS! YOU WON THE GAME! THE WORD IS {user_word}\n")
                                    exit()
                  else:
                        game += "_"
            print(game)
#This is for when attempts hits 6 attempts aka the max attempts
if attempts == max_attempts:
      #New indicator for game to show letters correct and missed
      game = ""
      for letter in user_word:
            if letter in guesses:
                  game += letter
            else:
                  game += "_"
      #Prints the full hangman
      print(attempt6)
      print(game)
      #Sorry you have lost
      print(f"I am sorry, you have run out of attempts, the word was {user_word}\n")
      #Exits game when they have lost
      exit()
