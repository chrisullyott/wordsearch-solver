from .file import read_file_upper

class Puzzle:
    def __init__(self, file):
        self.file = file
        self.grid = []
        for line in read_file_upper(file).splitlines():
            row = list(line.replace(' ', ''))
            self.grid.append(row)
        self.dim = [len(self.grid), len(self.grid[0])]

    def coord_exists(self, row_key, col_key):
        return row_key < self.dim[0] and col_key < self.dim[1]

    def coord_matches(self, row_key, col_key, char):
        return (self.coord_exists(row_key, col_key)
            and self.grid[row_key][col_key] == char)

    def print_all(self):
        string = ''
        for row in self.grid:
            for cell in row:
                string += ' ' + cell + ' '
            string += '\n'
        print(string)

    def print_coords(self, coords):
        string = ''
        for row_key, row in enumerate(self.grid):
            for col_key, cell in enumerate(row):
                print_cell = False
                for coord in coords:
                    if row_key == coord[0] and col_key == coord[1]:
                        print_cell = True
                        break
                string += ' ' + cell + ' ' if print_cell is True else ' · '
            string += '\n'
        print(string)
