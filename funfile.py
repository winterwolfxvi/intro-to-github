# This is the code created by your imaginary partner. It can be run in the terminal by typing 'python funfile.py'

import random

# Variables

triesLeft = 11
hint = ''
secretWord = ''
randomIndex = 0
userOption = ''
guessedCorrectly = False
repeatedGuess = False

wordGuess = ''
letterGuess = ''

# Procedures - CheckWord, CheckLetter, Create Hint/Indicator
# the method 'upper' is used to account for user inputs using different capitalization. ex) if the user puts in 'a' or 'A', the program should account for both values, making the user input case insensitive. 

def createIndicator(word):
  hintAsList = list(hint)
  wordAsList = list(word)
  #print(wordAsList)
  
  for char in wordAsList:
    if char == ('_'):
      hintAsList.append(' ')
    else:
      hintAsList.append('_')
    
  #print(hintAsList)
  output = ''.join(hintAsList)
  return(output)

def checkLetter(letter, word):
  index = 0
  letterProcessed = letter.upper()
  wordAsList = list(word)
  hintAsList = list(hint)
  #print(wordAsList)

  for i in range (len(wordAsList)):
    if letterProcessed == wordAsList[index]:
      hintAsList.pop(index)
      hintAsList.insert(index, letterProcessed)
    index = index+1
  #print(hintAsList)
  output = ''.join(hintAsList)
  #print(output)
  return(output)

def checkWord(guess, word):
  guessProcessed = guess.upper()
  guessAsList = list(guess)
  if " " in guessAsList:
    guessProcessed = guessProcessed.replace(" ", "_")
  #print(guessProcessed)

  if guessProcessed == word:
    return(True)
  else:
    return(False)

def addRecord(guess):
  guessProcessed = guess.upper()
  if guessProcessed not in guessRecord:
    guessRecord.append(guessProcessed)
    print("Your previous guesses: ", guessRecord)
    return(False)
  else:
    print("You have already guessed ", guess, ". Pick another letter/word to guess")
    return(True)

# Lists
dictionary = ["WATER_GAME", "DRIVEBASE", "CRESCENDO", "SWERVE_DRIVE", "TANK_DRIVE", "SCOUTING", "ALLIANCE", "ELEVATOR", "REGIONAL", "DRIVE_TEAM", "HARMONY", "COOPERTITION", "WORLDS", "CYBERLIONS", "NOTE", "INTAKE", "SHOOTER", "AMP", "SPEAKER", "GO_LIONS", "HUMAN_PLAYER", "TEAM_SPIRIT", "DEFENSE_ROBOT", "TRAP", "ROMMEUS_SERAPH", "WORLDS"]
guessRecord = [] # keeps track of what the user guesses so the user doesnt accidently repeat a guess
hangman = [
  """
  -----
  |   
  |
  |
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |
  |
  |
  |
  |
  |
  |
  --------
  """, 
  """
  -----
  |   |
  |   0
  |
  |
  |
  |
  |
  |
  --------
  """, 
  """
  -----
  |   |
  |   0
  |  -+-
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | 
  |  | 
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | | 
  |  | 
  |
  --------
  """,
  """
  -----
  |   |
  |   0 GAME OVER :P
  | /-+-\ 
  |   | 
  |   | 
  |  | | 
  |  | | 
  |
  --------
  """
] # hangman visuals created by user acardnell24 on StackExchange: https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman

# Main Code
# - startup code (before the game actually starts)
randomIndex = random.randint(0, (len(dictionary)-1))
#print(randomIndex)
secretWord = dictionary[randomIndex]
#print(secretWord)
hint = createIndicator(secretWord)
print(hint)
print(hangman[0])
print("Welcome to hangman! Try to guess the secret word by guessing a letter or the word itself.")
# game starts
while triesLeft != 0:
  # if the user guesses correctly or guesses all the letters to form a complete word, the program will display a win message and the loop will break
  if guessedCorrectly or '_' not in hint:
    if '_' not in hint:
      guessedCorrectly = True
    print("Congratulations! The word was ", secretWord)
    break

  # displayed every time a user guesses incorrectly but still has tries left
  if guessedCorrectly == False and triesLeft != 11:
    print("Not there yet - you have ", triesLeft, "tries left.")
    print(hangman[(11-triesLeft)])
  # choice menu
  userOption = input("Pick an option: \n1. Guess letter \n2. Guess word")
  if userOption == '1': #Guess letter
    letterGuess = input("Provide a letter to guess")
    if len(letterGuess) != 1 or letterGuess == ' ': 
      print("Invalid letter input. Please provide a single letter and make sure there are no extra characters in your input. To guess a word, select '2' in the menu.")
      repeatedGuess = True
    else:
      repeatedGuess = addRecord(letterGuess)
      hint = checkLetter(letterGuess, secretWord)
      print(hint)
  elif userOption == '2': #Guess word
    wordGuess = input("Provide a word to guess. Note: This will account for the entire phrase if there are multiple words: ")
    guessedCorrectly = checkWord(wordGuess, secretWord)
    repeatedGuess = addRecord(wordGuess)
  elif userOption != '1' or userOption != '2':
    print("Invalid user input: Make sure you select 1 or 2 before guessing.")
    repeatedGuess = True

  if repeatedGuess == False: # if the user repeats a guess by accident has an invalid input, it should not take away the amount of tries they get.
    triesLeft = triesLeft - 1

# end of game
if guessedCorrectly == False:
  print("You ran out of guesses :( . The word was ", secretWord)
  print(hangman[11])
  
if guessedCorrectly == True and triesLeft == 0: # added in case the user correctly guesses on the last try 
  print("Congratulations! The word was ", secretWord)