class RBFSNode:

    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if self.parent != None:
            self.g = parent.g + 1
        else:
            self.g = 0

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

    @property
    def h(self):
        """"h"""
        return self.puzzle.manhattan

    @property
    def f(self):
        """"f"""
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)
