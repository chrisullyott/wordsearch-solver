from .file import read_file_upper

class Solver:
    """
    Solver for a wordsearch puzzle.

    Variables:
        directions {list} -- Two-digit permutations of [-1, 0, 1], excluding [0, 0].
    """

    directions = [
        [ 0,  -1],
        [-1,   0],
        [ 0,   1],
        [ 1,   0],
        [-1,  -1],
        [-1,   1],
        [ 1,  -1],
        [ 1,   1]
    ]

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def find_candidates(self, char):
        candidates = []
        for row_key, row in enumerate(self.puzzle.grid):
            for col_key, cell in enumerate(row):
                if char == cell:
                    candidates.append([row_key, col_key])
        return candidates

    def find_word(self, word):
        word_chars = list(word.replace(' ', '').strip().upper())
        for candidate in self.find_candidates(word_chars[0]):
            for direction in self.directions:
                coords = []
                for char_key, char in enumerate(word_chars):
                    row_key = candidate[0] + (direction[0] * char_key)
                    col_key = candidate[1] + (direction[1] * char_key)
                    if self.puzzle.coord_matches(row_key, col_key, char):
                        coords.append([row_key, col_key])
                    else:
                        break
                if len(coords) == len(word_chars):
                    return coords
        return []

    def find_words(self, words):
        coords = []
        for word in words:
            coords = coords + self.find_word(word)
        return coords

    def find_from_wordlist(self, wordlist):
        words = read_file_upper(wordlist).splitlines()
        return self.find_words(words)
