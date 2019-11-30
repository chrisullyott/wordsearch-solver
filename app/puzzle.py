from .file import *

class Puzzle:
    def __init__(self, file):
        self.file = file
        self.grid = []
        for line in File.get_contents_upper(file).splitlines():
            row = list(line.replace(' ', ''))
            self.grid.append(row)
        self.dim = [len(self.grid), len(self.grid[0])]

    def get_all_coords(self):
        coords = []
        for row_key in range(len(self.grid)):
            for col_key in range(len(self.grid[row_key])):
                coords.append([row_key, col_key])
        return coords

    def coord_exists(self, row_key, col_key):
        return (row_key < self.dim[0]) and (col_key < self.dim[1])

    def print_all(self):
        return self.print_coords(self.get_all_coords())

    def print_coords(self, coords):
        string = ''
        for row_key, row in enumerate(self.grid):
            for col_key, cell in enumerate(row):
                string_val = ''
                for coord in coords:
                    if (row_key == coord[0] and col_key == coord[1]):
                        string_val = ' ' + cell + ' '
                        break
                if (string_val):
                    string += string_val
                else:
                    string += ' · '
            string += '\n'
        print(string)
