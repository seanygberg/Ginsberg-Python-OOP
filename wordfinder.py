import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("testwords.txt")
    3 words read

    >>> wf.random() in ["Abbie", "abbot", "abbotcy"]
    True
    
    >>> wf.random() in ["Abbie", "abbot", "abbotcy"]
    True
    
    >>> wf.random() in ["Abbie", "abbot", "abbotcy"]
    True
    """
    def __init__(self, filename):
        """Initialize WordFinder with words"""
        file = open(filename, "r")
        self.words = file.read().splitlines()
        print(len(self.words), "words read")
    
    def random(self):
        """Return a random word from the dictionary."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> wf = SpecialWordFinder("complexwords.txt")
    4 words read

    >>> wf.random() in ["Abbie", "abbot", "abbotcy"]
    True
    
    >>> wf.random() in ["Abbie", "abbot", "abbotcy"]
    True

    >>> wf.random() in ["Abbie", "abbot", "abbotcy"]
    True
    """
    def __init__(self, filename):
        """Initialize SpecialWordFinder with words"""
        super().__init__(filename)
        for word in self.words:
            if word.strip().startswith("#"):
                self.words.remove(word)

    def random(self):
        """Return a random word from the dictionary."""
        return random.choice(self.words)