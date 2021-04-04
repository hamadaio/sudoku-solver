import time
start_time = time.clock()

from sudoku_solver_functions import *
from support_functions import *
from guess_function import *
import board_file

print('load functions:', time.clock() - start_time)
board = board_file.boardInput3 #change name here to run another board
board_candidate_list = []
board_candidate_list = initialize_candidates(board_candidate_list, board)
print('load board:', time.clock()-start_time)
normal_operation(board_candidate_list, board)
print('runtime', time.clock()-start_time)