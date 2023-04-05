import time
import matplotlib.pyplot as plt

from puzzle import Puzzle
from rbfs_solver import RBFSSolver
from ucs_solver import UCSSolver

time_rbfs = []
time_ucs = []
state_rbfs = []
state_ucs = []

n = 20
board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
puzzle = Puzzle(board)
for i in range(n):
    puzzle = puzzle.shuffle()
    rbfs_slv = RBFSSolver(puzzle)
    ucs_slv = UCSSolver(puzzle)

    tic = time.time()
    slv_puzzle_rbfs = rbfs_slv.solve()
    toc = time.time()

    time_rbfs.append(toc - tic)
    steps = 0
    for smth in slv_puzzle_rbfs:
        steps += 1
    state_rbfs.append(steps)
#
    tic = time.time()
    slv_puzzle_ucs = ucs_slv.solve()
    toc = time.time()

    time_ucs.append(toc - tic)
    steps = 0
    for smth in slv_puzzle_ucs:
        steps += 1
    state_ucs.append(steps)

print("Average number of steps for RBFS: " + str(sum(state_rbfs) / n))
print("Average number of steps for UCS: " + str(sum(state_ucs) / n))


plt.plot(range(1, n+1), state_rbfs)
plt.show()
plt.plot(range(1, n+1), state_ucs)
plt.show()

print("Average time for computing: " + str(sum(time_rbfs) / n) + "s")
print("Average time for computing: " + str(sum(time_ucs) / n) + "s")

plt.plot(range(1, n+1), time_rbfs)
plt.show()
plt.plot(range(1, n+1), time_ucs)
plt.show()

print(state_rbfs)
print(state_ucs)
print(time_rbfs)
print(time_ucs)