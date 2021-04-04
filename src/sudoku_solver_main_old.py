from sudoku_solver_functions import *
import board_file

board = board_file.board1

board_candidate_list = []
board_candidate_list = initialize_candidates(board_candidate_list, board)

cont = 0
while cont<10:

	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				eliminate_candidates_row(i, j, board_candidate_list[i][j], board)		
				eliminate_candidates_col(i, j, board_candidate_list[i][j], board)
				eliminate_candidates_box((i//3)*3, (j//3)*3, i, j, board_candidate_list[i][j], board)
				set_values(i,j, board_candidate_list, board)
				catch_compare = compare_candidate_list_row(i,board_candidate_list[i][j], j, board_candidate_list)
				if catch_compare:
					board_candidate_list[i][j] = [catch_compare]
					board[i][j] = catch_compare
				catch_compare = compare_candidate_list_col(j,board_candidate_list[i][j], i, board_candidate_list)
				if catch_compare:
					board_candidate_list[i][j] = [catch_compare]
					board[i][j] = catch_compare
				catch_compare = compare_candidate_list_box(i//3*3, j//3*3, board_candidate_list[i][j], i, j, board_candidate_list)
				if catch_compare:
					board_candidate_list[i][j] = [catch_compare]
					board[i][j] = catch_compare
				find_pairs_row(i, board_candidate_list[i][j], j, board_candidate_list)
				find_pairs_col(j, board_candidate_list[i][j], i, board_candidate_list)
				find_pairs_box(i//3*3, j//3*3, board_candidate_list[i][j], i, j, board_candidate_list)
				pointing_triple_row(i, j, board_candidate_list[i][j], board_candidate_list)
				pointing_triple_col(i, j, board_candidate_list[i][j], board_candidate_list)
				claiming_triple_row(i,j, board_candidate_list[i][j], board_candidate_list)
				claiming_triple_col(i,j, board_candidate_list[i][j], board_candidate_list)

	for i in range(9):
		print(board[i])
	print()
	cont+=1