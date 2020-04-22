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
  return result # Returns result

def get_guessed_word(secret_word, letters_guessed): # Returns Secret word with blanks for unguessed letters
    '''get_guessed_word - Joins to a string the guessed letters and blanks in place of the missing ones 
      (needs to be called and stored before guess_warning)
    Args:
        secret_word (string): the word the user is guessing
        letters_guessed (list (of letters)): which letters have been guessed so far
    Returns:
         string :  comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = "".join([letter if letter in letters_guessed else " _ " for letter in secret_word]) #If letter guessed is in secret word , join letter , else join blank
    return guessed_word #Returns Guessed Word

def get_available_letters(letters_guessed): # Returns a String of unguessed letters

  '''get_available_letters [summary]
  
  Args:
      letters_guessed (list (of letters)): which letters have been guessed so far
  
  Returns:
      string (of letters): comprised of letters that represents which letters have not yet been guessed.
  '''
  letters_guessed= letters_guessed[:] # Make a copy of letters guessed 
  alphabet_list= list(string.ascii_lowercase)# Make a list of lowercase letters in alphabet
  alphabet="".join([letter for letter in alphabet_list if letter not in letters_guessed ] ) # Adds letters in the alphabet to a string that are not in the letters guessed list
  return alphabet #Returns String    

def is_guess_valid(guess,letters_guessed): # Checks if the guess is valid 
  '''
  is_guess_valid - takes in user inputted guess and checks if it is valid

  Args:
      guess (str): Users Guess

  Returns:
      Bool : If the guess is a valid lowercase letter guess return true
  '''  
  if (len(guess) == 1 and str.isalpha(guess) and get_available_letters(letters_guessed)): #checks the validity of guess returns #TODO: is this the best way to do this ?
    return True
  elif not (len(guess) == 1 and str.isalpha(guess)):
    return 'incorrect_type'
  else:
    return 'already_guessed'

def guess_warning(is_guess_valid, warning_counter,warning_threshold,guess,guessed_word):
  '''
  guess_warning - takes in a is_guess_valid response  and prints a warning and returns warning increment if needed 
  '''

  #TODO: Print Warning if already guessed or is wrong(two different prints)
  #TODO: (Possible) 
  if is_guess_valid != True:
    warning_counter += 1
    if is_guess_valid == 'incorrect_type':
      print("Oops !! ", guess, ",is not a valid letter. You have",(warning_threshold - warning_counter),"guesses left")#TODO:This is going 
    elif is_guess_valid == 'already_guessed':
      print("Oops !! You Already Guessed ",guess,".")
    else:
      raise Exception("Somehow you entered an invalid char that is undefined, char was:",is_guess_valid)
    
    return warning_counter
  

def game_start(secret_word, guess_threshold): # Introduction Text
  '''is_word_guessed - Prints the intro that includes the length of guess and the guess threshold
  
  Args:
      guess_threshold ([type]): [description]
  '''
  print("Hello, and Welcome to Hangman" )
  print("The Word To Guess is",len(secret_word),"letters long" )
  print("You have",guess_threshold,"guesses")

def game_round(secret_word,guess_threshold,letters_guessed): #Runs the game round 
  '''game_round this takes in the starting parameters 
  '''
  #TODO: Change round logic to make more sense  (possible gamestate condition function)
  # Something like  is_guess_valid(input("Enter your Guess: "))
  guess_counter = 0 # Set counter to starting value (0)
  warning_counter = 0 # Set the warning counter to the starting value (0)
  ##### Start Round ######
  while is_word_guessed(secret_word,letters_guessed)!= True: # Continue until the word is guessed 
    guess,guess_incr,warning_incr = user_guess(guess_threshold,guess_counter,warning_counter) # Takes user guess and validates
    guess_counter += guess_incr # Increments guess counter  
    warning_counter += warning_incr # Increments warning counter 
    letters_guessed.append(guess) # Appends the guess to the guessed letters list
    
    print(letters_guessed)
    
    if guess_counter >= guess_threshold: # Checks if guess threshold has been met if so print losing statement then break
      print("You Have Lost the Round")
      break
  else : 
    print("!!!!!!!!!!!!!!!!!!!!!!!!You Have Won The Round !!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!Good Job !!!!!!!!!!!!!!!!!!!)!!!!!")

def user_guess(guess_threshold,guess_counter,warning_counter): # Takes user guess (possbly not needed)
  '''user_guess Takes in no argurments, User Supplies guess input, user_guess Validates Input and
  returns guess  and  a guess counter increment 

  Returns:
      tuple : (guess,  guess increment )
  '''
  #starting variables
  guess_incr = 0 # sets the increment to zero 
  user_input = "" # resets user input variable 
  warning_incr = 0 # resets warning_increment
  warning_threshold = 3 # sets warning threshold 

  while is_guess_valid(user_input) != True:  # take user input until it is a valid guess 
    user_input = input("Enter your Guess: ")# takes user input

    ### (possible) warnining function / increment function

    if is_guess_valid (user_input) == False: #checks if guess is not valid  
      if warning_incr < warning_threshold: #checks if warning has not been met 
        warning_incr += 1 # increment warning counter 
        print("Warning, Please enter a valid letter:", warning_incr ,"out of",warning_threshold) #print warning statement 
      else: #if warnings have been used up increase guess count 
        guess_incr += 1 
        
    else: #if correct increment guess counter 
      guess_incr += 1
    #####(possible) this will probably end up in gamestate after refactor
    if guess_incr >= guess_threshold: # if the guessing has already hit the threshold break out of gettig input
          user_input = None # Remove any user input
          break # break out of guessing     
  #dont need #print ("Guess number:",guess_incr ) #print guess number

  return tuple((user_input,guess_incr,warning_incr)) #Return the input and increments 

def hangman(secret_word): #Main Function
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
  
    guess_threshold = 6 # sets guess threshold
    letters_guessed = [] # makes a empty list for the letter to be stored
    game_start(secret_word,guess_threshold)# runs the game intro script
    game_round(secret_word,guess_threshold,letters_guessed)# Starts a game round
    #print(is_guess_valid())

secret_word = 'apple' # takes in secret word for testing
#hangman(secret_word) # start the program
letters_guessed = ['e','i','k','p','r','s']
#letters_guessed = ['a','p','l','e']
warning_counter  = 0
guess_incr = 0 # sets the increment to zero 
guess = input("Enter your Guess: ") # resets user input variable 
warning_incr = 0 # resets warning_increment
warning_threshold = 3 # sets warning threshold

#print(is_word_guessed(secret_word,letters_guessed))
#print(get_guessed_word(secret_word,letters_guessed))
#print(get_available_letters(letters_guessed))
#get_available_letters(letters_guessed)
print(guess_warning(is_guess_valid(guess,letters_guessed),warning_counter,warning_threshold,guess,get_guessed_word(secret_word,letters_guessed)))
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
