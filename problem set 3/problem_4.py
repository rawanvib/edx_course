def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +" letters long")
    print("-----------")
    lettersGuessed = []
    guesses = 8
    # while all the letters of secretWord are not yet in lettersGuessed and guesses left is more than 0
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        # print first line
        print("You have " + str(guesses) +" guesses left")
        # print second line
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        # print third line
        # if user input a letter that has already been entered, reprompt for letter
        while True:
            guessLetter = input("Please guess a letter: ").lower()
            if guessLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                print("    You have " + str(guesses) +" guesses left")
                print("Available Letters: " + getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += guessLetter
        # print last line
        # if correctly guessed secret word
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("Congratulations, you won!")
            break
        # else if the guess letter is in secret word
        elif guessLetter in secretWord:
             print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
             print("-----------")
        # else the guess letter is not in secret word
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            guesses -= 1
        # if ran out of guesses
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            
            



