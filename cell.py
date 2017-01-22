class Cell:
    def __init__(self, content=None):
        self.content = content
        self.is_empty = True

    def set_content(self, content):
        self.content = content

    def is_empty(self, cell):
        return True

    def __str__(self):
        return "'"

    def __repr__(self):
        return "'"