def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    tempHand = hand.copy()
    for char in word:
        if char in hand.keys():
            #this condition checks occuruences of letter in word <= occ. in hand
            if tempHand[char]>0:
                tempHand[char] -= 1
            else:
                return False
        else:
            return False
    if word in wordList:
        return True
    else:
        return False

