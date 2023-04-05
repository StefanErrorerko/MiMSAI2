class UCSNode:

    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if self.parent != None:
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def f(self):
        return self.g

    @property
    def board(self):
        return self.puzzle

    @property
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def if_solved(self):
        return self.puzzle.if_solved

    @property
    def actions(self):
        return self.puzzle.actions

    def __str__(self):
        return str(self.puzzle)
