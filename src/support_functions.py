from sudoku_solver_functions import *

#display possible solutions for a square
def print_candidate_list(x, y, board_candidate_list):
	print(x,y,board_candidate_list[x][y])

#displays all lists with possible solutions
def print_board_candidates(board_candidate_list):
	for x in range(9):
		for y in range(9):
			print(x,y,board_candidate_list[x][y], end=' ')
		print()

#prints the board in a neat way
def print_board(board):
	for i in range(9):
		if i % 3 == 0 and not i == 0:
			#print('-'*6,'+','-'*5,'+','-'*6, sep='')
			print('-'*19)
		for j in range(9):
			if j % 3 == 0:
				print('|',end='')
			else:
				print(' ',end='')
			print(board[i][j],end='')
		print('|')

def eliminate(board_candidate_list, board):
	for i in range(9):
		for j in range(9):
			eliminate_candidates_row(i, j, board_candidate_list[i][j], board)		
			eliminate_candidates_col(i, j, board_candidate_list[i][j], board)
			eliminate_candidates_box((i//3)*3, (j//3)*3, i, j, board_candidate_list[i][j], board)

def call_set_values(board_candidate_list, board):
	for x in range(9):
		for y in range(9):
			set_values(x,y, board_candidate_list, board)

def catch_compare(board_candidate_list, board):
	for i in range(9):
		for j in range(9):
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


def find_pairs(board_candidate_list, board):
	for i in range(9):
		for j in range(9):
			find_pairs_row(i, board_candidate_list[i][j], j, board_candidate_list)
			find_pairs_col(j, board_candidate_list[i][j], i, board_candidate_list)
			find_pairs_box(i//3*3, j//3*3, board_candidate_list[i][j], i, j, board_candidate_list)

def claiming_tripple(board_candidate_list, board):
	for i in range(9):
		for j in range(9):
			claiming_triple_row(i,j, board_candidate_list[i][j], board_candidate_list)
			claiming_triple_col(i,j, board_candidate_list[i][j], board_candidate_list)

def pointing_triple(board_candidate_list, board):
	for i in range(9):
		for j in range(9):
			pointing_triple_row(i, j, board_candidate_list[i][j], board_candidate_list)
			pointing_triple_col(i, j, board_candidate_list[i][j], board_candidate_list)

#if board faulty: return -1 board full: return 1 else 0
def check_done(board_candidate_list):
	for i in range(9):
		for j in range(9):
			if len(board_candidate_list[i][j]) == 0:
				return -1
			if not (len(board_candidate_list[i][j]) == 1):
				return 0
	return 1