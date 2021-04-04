from sudoku_solver_functions import *
from support_functions import *
import copy

#we're stuck, make a guess that is likely to lead to a solution
def make_guess(board_candidate_list, board):
	old_board = copy.deepcopy(board)	#copy so we can return if guess was wrong
	old_board_candidate_list = copy.deepcopy(board_candidate_list)
	x,y = find_shortest(board_candidate_list)
	for element in old_board_candidate_list[x][y]:	#guess, one by one, all possible solutions
		board[x][y] = element
		board_candidate_list[x][y] = [element]
		result = normal_operation(board_candidate_list, board)
		if result == 1:	#guess led to a solution, we're done!
			return 1
		board = copy.deepcopy(old_board)	#guess was wrong, reset board
		board_candidate_list = copy.deepcopy(old_board_candidate_list)

#find shortest list of at least length 2, return coordinates
def find_shortest(board_candidate_list):
	for length in range(2,9):
		for i in range(9):
			for j in range(9):
				len(board_candidate_list[i][j])
				if len(board_candidate_list[i][j]) == length:
					return i,j

#try to eliminate solutions with logic
def normal_operation(board_candidate_list, board):
	for n in range(2):
		eliminate(board_candidate_list, board)
		call_set_values(board_candidate_list, board)
		catch_compare(board_candidate_list, board)
		claiming_tripple(board_candidate_list, board)
		#pointing_triple(board_candidate_list, board)	#not worth the effort, benefits are slower than guessing
		#find_pairs(board_candidate_list, board)		#not worth the effort, benefits are slower than guessing
		call_set_values(board_candidate_list, board)

	done = check_done(board_candidate_list)
	if done == 1: #solution was found!
		print_board(board)
		return 1
	elif done == -1: #faulty guess, retry
		return 0
	return make_guess(board_candidate_list, board)