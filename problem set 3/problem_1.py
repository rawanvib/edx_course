def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    wordLen=len(secretWord)
    
    for i in secretWord:
      if i in lettersGuessed:
         wordLen-=1

    if wordLen==0:
      return True
    else:
      return False
        
