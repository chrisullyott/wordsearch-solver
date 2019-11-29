class File:
    def get_contents_upper(filename):
        with open(filename) as f:
            contents = f.read().strip().upper()
        return contents
