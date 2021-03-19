class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)
        Message.get_valid_words(self)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        max_words = 0
        best_shift = 0
        
        for i in range(26):
            to_decrypt = (self.apply_shift(i)).split(" ")
            words_num = 0
            for word in to_decrypt:
                if is_word(self.valid_words, word):
                    words_num += 1
            if words_num > max_words:
                max_words = words_num
                best_shift = i
        
        decrypted = "".join(self.apply_shift(best_shift))
        
        return best_shift, decrypted

