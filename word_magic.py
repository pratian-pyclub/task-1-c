import re
WILDCARD = '?'
WILDCARD_PATTERN = '\\' + WILDCARD

class WordMagic():
    def __init__(self, tile, word):
        """Initialize WordMagic object with tile and word values"""
        self.tile = tile
        self.word = word

    def can_create(self):
        """Return a boolean value if given tile can create the word or not"""

        # If length of word is greater than the tile, 
        # word can never be formed
        if len(self.word) > len(self.tile):
            return False

        tile = self.tile

        for letter in self.word:
            # At each pass remove the matched letter, 
            # else regex will match for repeating letters

            # Eg, without removal a tile with a single 'e' 
            # will return True for a word with double 'e'
            if re.search(letter, tile) is not None:
                tile = tile.replace(letter, "")
            elif re.search(WILDCARD_PATTERN, tile) is not None:
                tile = tile.replace(WILDCARD, "")
            else:
                # If neither of the conditions match,
                # function can return False immediately
                
                # This prevents logic running for the length of the word
                # when a letter at the beginning itself did not match
                return False

        return True
