import collections
from ucs_node import UCSNode

class UCSSolver:
    def __init__(self, init_board):
        self.init_board = init_board
        self.explored = []
        self.frontier = []

    def solve(self):
        node = UCSNode(self.init_board)
        self.frontier.append([node, 0])
        while len(self.frontier) != 0:
            self.frontier.sort(key=lambda i: i[1])
            node = self.frontier.pop(0)[0]
            if node.if_solved:
                return node.path
            self.explored.append(node)
            for move, action in node.actions:
                child = UCSNode(move(), node, action)
                if child in self.explored:
                    continue
                self.frontier.append([child, child.parent.f + 1])