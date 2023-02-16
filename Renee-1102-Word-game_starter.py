import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
  
  #secret_word = random(word_list)
  #letters_guessed = input(range(list))
  #list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#      


    for letter in secret_word:
        if letter not in letters_guessed:
          return False

    return True

### Testcases
#secret_word = 'renee'
#letters_guessed = ['e', 'f', 'r', 'n', 'o']
#print(is_word_guessed(secret_word, letters_guessed))

#print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
  
    output_string = ''
    for letter in secret_word:
       if letter in letters_guessed:
         output_string += letter  
       else:
        output_string += '_ '
    
    return output_string 


    
    
      
#Testcases
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
#print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...   
  
    import string
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters




#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game.
    * At the start of the game, let the user know how many 
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    letters_guessed = []
    times_to_guess = 8
    print("Welcome to the word guessing game")
    print("Guess a word with a length of " + str(len(secret_word)) + " letters")
    while times_to_guess > 0:
      guess = input("Enter a lower case letter to start guessing: ")
      print("You have " + str(times_to_guess) + " more guesses")
      print("Available letters: " + get_available_letters(letters_guessed))
      if guess in letters_guessed:
        print("You've gussed this letter already, try again")
        continue
      letters_guessed.append(guess)
      print(str(times_to_guess) + " more times to guess")
      print(get_guessed_word(secret_word, letters_guessed))
      print("Here's your available letters: " + get_available_letters(letters_guessed))
      if guess in secret_word:
        print("Correct, this letter is found in your secret word")
      else:
        times_to_guess -= 1
        print("Guess again, this letter is not found in secret word")
      if is_word_guessed(secret_word, letters_guessed):
        print("YOU WON")
        break

    
    if times_to_guess == 0:
      print("TRY AGAIN, YOU LOSE")
      print("The secret word was " + secret_word + ".")







def main():
    secret_word = choose_word(word_list)
    game_loop('book')

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()
