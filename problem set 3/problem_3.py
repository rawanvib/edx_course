def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters=list(string.ascii_lowercase)
    
    for i in lettersGuessed:
      if i in letters:
        a=letters.index(i)
        del letters[a]

    return "".join(letters)

