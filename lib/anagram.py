# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # initializing an empty list and checking match words
        matches = []

        #  iterating throuh the word_list and checking match
        for word in word_list:
            if sorted(self.word) == sorted(word):
                matches.append(word)

        return matches