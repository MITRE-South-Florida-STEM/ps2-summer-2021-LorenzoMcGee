# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"







def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
  letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
  returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
  '''
  for char1 in secret_word:
    charInGuessed = False
    for char2 in letters_guessed:
      if(char1 == char2):
        charInGuessed = True
    if(not charInGuessed):
      return False
  return True



def get_guessed_word(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
  '''
  workerString = ""
  for char1 in secret_word:
    charInGuessed = False
    for char2 in letters_guessed:
      if(char1 == char2):
        charInGuessed = True
    if(charInGuessed):
      workerString += char1 + " "
    else:
      workerString += "_ "
  return workerString
    
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    tempString = string.ascii_lowercase
    workerString = ""
    for char1 in tempString:
      isInGuessed = False
      for char2 in letters_guessed:
        if(char1 == char2):
          isInGuessed = True
      if(not isInGuessed):
        workerString += char1
    return workerString
    
warnings = 3
guesses = 6
def getUserGuess(guessed_letters,secret_word):
  global warnings
  global guesses
  isValidGuess = False
  currentGuess = ""  
  while(not isValidGuess):
    currentGuess = input("Please input your one letter guess: ");
    if(len(currentGuess) != 1):
      print("Restrict your guess to one character please.")
    else:
      for char in string.ascii_letters:
        if char == currentGuess:
          isValidGuess = True
          isAlreadyGuessed = False
          for char2 in guessed_letters:
            if char == char2:
              isAlreadyGuessed = True
              break
          if(isAlreadyGuessed):
            if(warnings > 0):
              warnings -= 1
              print("This character is already guessed. You've lost a warning. Remaining:",warnings)
            else:
              print("This character is already guessed. You've lost a guess.")
              guesses -= 1
            return ""
          break
      if(warnings > 0 and (not isValidGuess)):
        warnings -= 1
        print("That was not a valid guess mate. Warnings left:", warnings)
      elif (warnings == 0) and (not isValidGuess):
        isValidGuess = True
  currentGuess = currentGuess.lower()
  isInWord = False
  for char in secret_word:
    if(char == currentGuess):
      isInWord = True
      break
  isVowel = False
  if(not isInWord):
    tempString = "aeiou"
    for char in tempString:
      if(char == currentGuess):
        isVowel = True
        break
  if(not isInWord and isVowel):
    guesses -= 2
  elif(not isInWord):
    guesses -= 1

  if(isInWord):
    print("Correct. This is in the word.")
  else:
    print("This character is not in the word.")
  return currentGuess

def getUserGuessWithHints(guessed_letters,secret_word):
  global warnings
  global guesses
  isValidGuess = False
  currentGuess = ""  
  while(not isValidGuess):
    currentGuess = input("Please input your one letter guess: ");
    if(len(currentGuess) != 1):
      print("Restrict your guess to one character please.")
    else:
      for char in (string.ascii_letters+"*"):
        if char == currentGuess:
          isValidGuess = True
          isAlreadyGuessed = False
          for char2 in guessed_letters:
            if char == char2:
              isAlreadyGuessed = True
              break
          if(isAlreadyGuessed):
            if(warnings > 0):
              warnings -= 1
              print("This character is already guessed. You've lost a warning. Remaining:",warnings)
            else:
              print("This character is already guessed. You've lost a guess.")
              guesses -= 1
            return ""
          break
      if(warnings > 0 and (not isValidGuess)):
        warnings -= 1
        print("That was not a valid guess mate. Warnings left:", warnings)
      elif (warnings == 0) and (not isValidGuess):
        isValidGuess = True
  currentGuess = currentGuess.lower()
  if(currentGuess == "*"):
    show_possible_matches(get_guessed_word(secret_word,guessed_letters))
    return ""
  isInWord = False
  for char in secret_word:
    if(char == currentGuess):
      isInWord = True
      break
  isVowel = False
  if(not isInWord):
    tempString = "aeiou"
    for char in tempString:
      if(char == currentGuess):
        isVowel = True
        break
  if(not isInWord and isVowel):
    guesses -= 2
  elif(not isInWord):
    guesses -= 1

  if(isInWord):
    print("Correct. This is in the word.")
  else:
    print("This character is not in the word.")
  return currentGuess

def uniqueCharacters(secret_word):
  worker = ""
  for char1 in secret_word:
    isInWorker = False
    for char2 in worker:
      if(char2 == char1):
        isInWorker = True
    if(not isInWorker):
      worker += char1
  return len(worker)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''
    global guesses
    print("Welcome to hangman. You have",guesses,"guesses to guess the length",len(secret_word),"word. Good luck!")
    guessedLetters = ""
    while(guesses > 0 and (not(is_word_guessed(secret_word,guessedLetters)))):
      print("Remaining Warnings:", warnings)
      print("Remaining Guesses:",guesses)
      print("Remaining Letters: " + get_available_letters(guessedLetters))
      print(get_guessed_word(secret_word,guessedLetters))
      guess = getUserGuess(guessedLetters,secret_word)
      guessedLetters += guess
    if(is_word_guessed(secret_word,guessedLetters)):
      print(get_guessed_word(secret_word,guessedLetters))
      print("Congratulations. You won. Score:",guesses*uniqueCharacters(secret_word))
    else:
      print("Sorry, you lost. The word was:",secret_word)
      



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

#I don't know enough python where this isn't the simplest solution to finding out if a string is is valid

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    
    my_word = my_word.replace(" ","")
    uniqueCharsInMyWord = ""
    for char in my_word:
      alreadyInIt = False
      for char2 in uniqueCharsInMyWord:
        if char2 == char:
          alreadyInIt = True
          break
      if(not alreadyInIt):
        uniqueCharsInMyWord += char
    
    if(len(my_word)!=len(other_word)):
      return False
    
    for i in range (len(my_word)):
      char1 = my_word[i:i+1]
      char2 = other_word[i:i+1]
      if(char1 != char2):
        if(not char1.isalpha()):
          Invalid = False
          for char in uniqueCharsInMyWord:
            if(char == char2):
              Invalid = True
              break
          if(Invalid):
            return False
        else:
          return False
    return True
    




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    builderString = ""
    for elm in wordlist:
      if(match_with_gaps(my_word,elm)):
        builderString +=  elm + " "
    if(builderString == ""):
      print("No Matches Found")
    else:
      print(builderString)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global guesses
    print("Welcome to hangman with hints. You have",guesses,"guesses to guess the length",len(secret_word),"word. Good luck!")
    guessedLetters = ""
    while(guesses > 0 and (not(is_word_guessed(secret_word,guessedLetters)))):
      print("Remaining Warnings:", warnings)
      print("Remaining Guesses:",guesses)
      print("Remaining Letters: " + get_available_letters(guessedLetters))
      print(get_guessed_word(secret_word,guessedLetters))
      guess = getUserGuessWithHints(guessedLetters,secret_word)
      guessedLetters += guess
    if(is_word_guessed(secret_word,guessedLetters)):
      print(get_guessed_word(secret_word,guessedLetters))
      print("Congratulations. You won. Score:",guesses*uniqueCharacters(secret_word))
    else:
      print("Sorry, you lost. The word was:",secret_word)
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
