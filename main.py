import os
import argparse
from app import *

# Parse arguments
parser = argparse.ArgumentParser(description='Forecast command line')
parser.add_argument('puzzle', help='The puzzle file', type=str)
parser.add_argument('wordlist', help='A wordlist to search', type=str)
args = parser.parse_args()

puzzle = Puzzle(args.puzzle)
solver = Solver(puzzle)
coords = solver.find_from_wordlist(args.wordlist)
puzzle.print_all()
puzzle.print_coords(coords)

