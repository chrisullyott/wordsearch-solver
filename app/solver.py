from .file import *

class Solver:
    directions = [
        [0, -1], [-1, 0], [0, 1], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]
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
        found_coords = []
        word = word.strip().upper()
        word_chars = list(word)
        dim = self.puzzle.dim
        for candidate in self.find_candidates(word_chars[0]):
            for direction in self.directions:
                test_coords = []
                for char_key, char in enumerate(word_chars):
                    row_key = candidate[0] + (direction[0] * char_key)
                    col_key = candidate[1] + (direction[1] * char_key)
                    coord_exists = row_key < dim[0] and col_key < dim[1]
                    if coord_exists and char == self.puzzle.grid[row_key][col_key]:
                        test_coords.append([row_key, col_key])
                    else:
                        break
                if len(test_coords) >= len(word_chars):
                    found_coords = found_coords + test_coords
        return found_coords

    def find_words(self, words):
        all_coords = []
        for word in words:
            coords = self.find_word(word)
            all_coords = all_coords + coords
        return all_coords

    def find_from_wordlist(self, wordlist):
        words = File.get_contents_upper(wordlist).splitlines()
        return self.find_words(words)
