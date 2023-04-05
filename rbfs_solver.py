from puzzle import Puzzle
from sys import maxsize
from rbfs_node import RBFSNode
from random import randint

class RBFSSolver:
    def __init__(self, init_board):
        self.init_board = init_board
        self.max_depth = 900

    def solve(self):
        node = RBFSNode(self.init_board)
        goal_node = self.RBFS_search(node, f_limit=maxsize)[0]
        return goal_node.path

    def RBFS_search(self, node, f_limit):
        successors, count = [], -1
        if node.if_solved:
            return node, None
        for move, action in node.actions:
            child = RBFSNode(move(), node, action)
            count += 1
            successors.append((child.f, count, child))
        while len(successors):
            successors.sort()
            best_node = successors[0][2]
            if best_node.f > f_limit:
                return None, best_node.f
            alternative = successors[1][0]
            result = self.RBFS_search(best_node, min(f_limit, alternative))[0]
            successors[0] = (best_node.f, successors[0][1], best_node)
            if result is not None:
                break
        return result, None

