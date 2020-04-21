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

WORDLIST_FILENAME = "problemSets/ps2/words.txt"


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
def is_word_guessed(secret_word, letters_guessed): # Checks if Letters guessed complete the word
  '''is_word_guessed  Takes a set of guessed letters and checks aganst the secret word
  
  Args:
      secret_word (string): the word the user is guessing; assumes all letters are lowercase
      letters_guessed (list (of letters)): which letters have been guessed so far, assumes that all letters are lowercase
  Returns:
      boolean: True if all the letters of secret_word are in letters_guessed;
    False otherwise

  '''
  secret_word_list = list(secret_word)#makes a list of the letters in secret word
  letters_guessed = letters_guessed[:] # Takes a Copy of the letters_guessed list
  result = all(elem in letters_guessed for elem in secret_word_list)# Checks if all of the letters that have been guessed(elem in letters guessed) are in 
  return result
def get_guessed_word(secret_word, letters_guessed):
    '''get_guessed_word - Joins to a string the guessed letters and blanks in place of the missing ones 

    Args:
        secret_word (string): the word the user is guessing
        letters_guessed (list (of letters)): which letters have been guessed so far
    Returns:
         string :  comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = "".join([letter if letter in letters_guessed else " _ " for letter in secret_word])
    return guessed_word
def get_available_letters(letters_guessed):

  '''get_available_letters [summary]
  
  Args:
      letters_guessed (list (of letters)): which letters have been guessed so far
  
  Returns:
      string (of letters): comprised of letters that represents which letters have not yet been guessed.
  '''
  letters_guessed= letters_guessed[:]
  alphabet_list= list(string.ascii_lowercase)
  alphabet="".join([letter for letter in alphabet_list if letter not in letters_guessed ] )
  return alphabet    
def is_guess_valid(guess):
  if (len(guess) == 1 and str.isalpha(guess) and get_available_letters(guess)):
    return True
  else:
    return False

def game_start(secret_word, guess_threshold):
  '''is_word_guessed Prints the intro that includes 
  
  Args:
      guess_threshold ([type]): [description]
  '''
  print("Hello, and Welcome to Hangman" )
  print("The Word To Guess is",len(secret_word),"letters long" )
  print("You have",guess_threshold,"guesses")
def game_round(secret_word,guess_threshold,letters_guessed):
  '''game_round this takes in the starting parameters 
  '''
  guess_counter = 0 # set counter to starting value
  warning_counter = 0
  ##### Start Round ######
  while is_word_guessed(secret_word,letters_guessed)!= True: # Continue until the word is guessed 
    guess,guess_incr,warning_incr = user_guess(guess_threshold,guess_counter,warning_counter) # Takes user guess and validates
    guess_counter += guess_incr
    warning_counter += warning_incr
    letters_guessed.append(guess)
    print(letters_guessed)
    if guess_counter >= guess_threshold:
      print("You Have Lost the Round")
      break
  else :
    print("!!!!!!!!!!!!!!!!!!!!!!!!You Have Won The Round !!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!Good Job !!!!!!!!!!!!!!!!!!!)!!!!!")
def user_guess(guess_threshold,guess_counter,warning_counter):
  '''user_guess Takes in no argurments, User Supplies guess input, user_guess Validates Input and
  returns guess  and  a guess counter increment 

  Returns:
      tuple : (guess,  guess increment )
  '''
  #starting variables
  guess_incr = 0
  user_input = ""
  warning_incr = 0
  warning_threshold = 3 

  while is_guess_valid(user_input) != True:  
    user_input = input("Enter your Guess: ")
    if is_guess_valid (user_input) == False:
      if warning_incr < warning_threshold:
        warning_incr += 1
        print("Warning, Please enter a valid letter:", warning_incr ,"out of",warning_threshold)
      else:
        guess_incr += 1
        
    else:
      guess_incr += 1
      
    if guess_incr >= guess_threshold:
          user_input = None
          break     
  print ("Guess number:",guess_incr ) 

  return tuple((user_input,guess_incr,warning_incr))

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
  
    guess_threshold = 6
    letters_guessed = []
    game_start(secret_word,guess_threshold)
    game_round(secret_word,guess_threshold,letters_guessed)
    #print(is_guess_valid())

secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']
#letters_guessed = ['a','p','l','e']
#hangman(secret_word)
#print(is_word_guessed(secret_word,letters_guessed))
#print(get_guessed_word(secret_word,letters_guessed))
#print(get_available_letters(letters_guessed))
get_available_letters(letters_guessed)
# When you've completed your hangman function,  scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
