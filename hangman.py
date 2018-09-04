# -*- coding: utf-8 -*-
"""
Created on Tue Aug  24 14:05:53 2018

@author: EMEKA AND OLUWABAMISE
"""

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

# -----------------------------------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()
letters_guessed = []
letters_guessed = input("Enter your guessed word:").lower() 
def is_word_guessed(secret_word, letters_guessed):
    
    #secret_word: string, the word the user is guessing; assumes all letters are
    #lowercase
    #letters_guessed: list (of letters), which letters have been guessed so far;
    #assumes that all letters are lowercase
    #returns: boolean, True if all the letters of secret_word are in letters_guessed;
    #False otherwise
    
    for letters in secret_word:  
        if letters in letters_guessed:
                return True
        else:
                return False 
#print(is_word_guessed("sweskills", letters_guessed))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
#-----------------------------------------------------------------    

    

#-----------------------------------------------------------------    
wordlist = load_words()
letters_guessed = input("Enter your guessed word:").lower() 
def get_guessed_word(secret_word, letters_guessed):
    
  #  secret_word: string, the word the user is guessing
   # letters_guessed: list (of letters), which letters have been guessed so far
    #returns: string, comprised of letters, underscores (_), and spaces that represents
     # which letters in secret_word have been guessed so far.
    
    incomplete_guessed_word = " "
    for letters in secret_word:  
        if letters in letters_guessed:
            incomplete_guessed_word += letters   
        else:
            incomplete_guessed_word += "_"
    return incomplete_guessed_word
#print(get_guessed_word("sweskills", letters_guessed))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
#-----------------------------------------------------------------   

    

#-----------------------------------------------------------------   
wordlist = load_words()
letters_guessed = input("Enter your guessed word:").lower()
def get_available_letters(letters_guessed):
    
    #letters_guessed: list (of letters), which letters have been guessed so far
    #returns: string (of letters), comprised of letters that represents which letters have not
    #yet been guessed.
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    letters = string.ascii_lowercase
    unguessed = " "
    #for each item in letters, check if it's been guessed; if not, added to unguessed variable
    for i in letters:
      if i not in letters_guessed:
        unguessed += i
    return unguessed
#print(get_available_letters(letters_guessed))

#------------------------------------------------------------------



#FUNCTION TO TEST THE USER'S INPUT IN THE HANGMAN GAME
#--------------------------------------------------------------------
    
def user_input_requirements():

    warning = 3
    
    #users_guess_history = []
    
    while warning >= 0:
        
        users_guess = input("Make a guess. Put in a letter: ").lower()
        
        if users_guess not in "abcdefghijklmnopqrstuvwxyz":
            
            print("You can only put in an alphabet")
            
            print("You have lost a warning")
           
            warning -= 1
            
        elif users_guess == "":
            
            print("You must guess an alphabet")
            
            print("You have just lost a warning")
            
            warning -= 1
            
            
           
        else:
        
            return (users_guess, warning)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#FUNCTION TO RETURN THE COUNT OF UNIQUE LETTERS IN THE SECRET WORD
def count_unique_letters(secret_word):
     
    return len(set(secret_word))

#------------------------------------------------------------------------------
  #FUNCTION TO REDUCE GUESSING CHANCES IF WRONG GUESS IS A VOWEL OR CONSONANT       
def reduce_guess(users_guess, num_of_guesses_left):
    
    if users_guess in "aeiou":
        
        num_of_guesses_left -= 2
        
    else:
        
        num_of_guesses_left -= 1
        
    return num_of_guesses_left

#----------------------------------------------------------------------------
    
wordlist = load_words()
letters_guessed = input("Enter your guessed word:").lower()
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print("Welcome to the Hangman game!")
    
    #Variable conatining the random word chosen by the computer. For testing
    secret_word = choose_word(wordlist)
    
    #For testing
    print(secret_word)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    
    print("I am thinking of a word that is", str(len(secret_word)), "letters long")
    
   # print(guessed_words)
    
    #Initializing the list containing all the guessed letters
    letters_guessed = []
    
    print("                                                  ")
    #print("You have", str(num_of_guesses_left), "guesses left")
    
    print("Available Letters:", get_available_letters(letters_guessed))
    
    num_of_guesses_left = 6
    
    while num_of_guesses_left >= 0:
    
        #Take in the user's guess with the user_input_requirement function
        (users_guess, warning) = user_input_requirements()
        
        letters_guessed.append(users_guess)
        
        #guess_non_repeat(users_guess, letters_guessed)
        
        
        #Check if the guessed letter is in the computer's chosen word
        if users_guess in secret_word:
            
            #letters_guessed.append(users_guess)
            
            #guess_non_repeat(users_guess, letters_guessed)
            
            print("You have", str(num_of_guesses_left), "guesses left")
            
            print("Warning:", str(warning))
            
            print(letters_guessed)
            
            print("Available Letters:", get_available_letters(letters_guessed))
            
            print("Good Guess:", get_guessed_word(secret_word, letters_guessed ))         
                     
            print("__________________________________________")
            
            if get_guessed_word(secret_word, letters_guessed ) == secret_word:
                
                print("                                          ")
                
                total_score = num_of_guesses_left * count_unique_letters(secret_word)
                
                print("Your total score is:", str(total_score))
                
                print("                                          ")
                
                print("Congratulations!!!")
                
                break
            
        else:
            
            #guess_non_repeat(users_guess, letters_guessed)
            
            print(letters_guessed)
            
            num_of_guesses_left = reduce_guess(users_guess, num_of_guesses_left)
            
            print("Warning:", str(warning))
            
            print("Available Letters:", get_available_letters(letters_guessed))
            
            #print("You have", str(num_of_guesses_left), "guess(es) left")
            
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed ) )
            
            print("__________________________________________")
            
            #To stop the printing of '-1 guess(es)' when vowel guess 
            #reduction takes num_of_guesses_left to below 0
            if num_of_guesses_left != -1:
                
                print("You have", str(num_of_guesses_left), "guess(es) left")
            
            if num_of_guesses_left <= 0:
                
                print("                                          ")
                
                print("Ooops!!!, you are out of guesses!!")
                
                print("                                          ")
                
                print("The Word is:", secret_word.upper())
                
                print("                                          ")
                
                print("Game Over!!!")
                
                break
            



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)



# When you've completed your hangman function, scroll down to the bottom
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
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)