import re

class Search:
    def __init__(self, filename='default_text.txt'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found.")
        
    def clean(self):
        self.lines = [re.sub(r'[^a-zA-Z0-9\s]', '', line) for line in self.lines]

    def getLines(self, pattern):
        result = [pattern]
        for index, line in enumerate(self.lines, start=1):
            if pattern in line:
                result.append((index, line.strip()))
        return result
