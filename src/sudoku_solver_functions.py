#create 9*9*9 board with possible solutions based on a starting board
def initialize_candidates(board_candidate_list, board):
	for x in range(9):
		board_candidate_list.append([])
		for y in range(9):
			board_candidate_list[x].append([])
			if board[x][y] > 0:
				board_candidate_list[x][y].append(board[x][y])
			else:
				for z in range(1,10):
					board_candidate_list[x][y].append(z)
	return board_candidate_list

#update board based on possible solutions
def set_values(i,j, board_candidate_list, board):
	if len(board_candidate_list[i][j]) == 1:
		board[i][j]=board_candidate_list[i][j][0]

#loop row and remove matches to candidate_list
def eliminate_candidates_row(row_number, col_number, candidate_list, board):
	for i in range(9):
		if i == col_number:
			continue
		if board[row_number][i] in candidate_list:
			candidate_list.remove(board[row_number][i])


def eliminate_candidates_col(row_number, col_number, candidate_list, board):
	for i in range(9):
		if i == row_number:
			continue
		if board[i][col_number] in candidate_list:
			candidate_list.remove(board[i][col_number])

def eliminate_candidates_box(x, y, x_index, y_index, candidate_list, board):
	for i in range(3):
		for j in range(3):
			if i+x == x_index and j+y == y_index:
				continue
			if board[x+i][y+j] in candidate_list:
				candidate_list.remove(board[x+i][y+j])

def compare_candidate_list_row(row_number, candidate_list, index, board_candidate_list):
	for candidate_value in candidate_list:
		for i in range(9):
			if i == index:
				continue
			if candidate_value in board_candidate_list[row_number][i]:
				break
			elif i == 8 or i == 7 and index == 8:
				return candidate_value
	return 0

def compare_candidate_list_col(col_number, candidate_list, index, board_candidate_list):
	for candidate_value in candidate_list:
		for i in range(9):
			if i == index:
				continue
			if candidate_value in board_candidate_list[i][col_number]:
				break
			elif i == 8 or i == 7 and index == 8:
				return candidate_value
	return 0

def compare_candidate_list_box(x, y, candidate_list, index_x, index_y, board_candidate_list):
	done = False
	for candidate_value in candidate_list:
		for i in range(3):
			for j in range(3):
				if i == index_x and j == index_y:
					continue
				if candidate_value in board_candidate_list[x + i][y + j]:
					done = True
					break
				elif (i == 2 and j == 2) or (i == 2 and j == 1 and index_x == x + 2 and index_y == y + 2):
					return candidate_value
			if done == True:
				break	
	return 0

def find_pairs_row(row_number, candidate_list, index, board_candidate_list):
	pair_pos=-1
	if len(candidate_list) == 2:
		for i in range(9):
			if i == index:
				continue
			if candidate_list == board_candidate_list[row_number][i]:
				pair_pos = i
				break
	if not pair_pos == -1:
		for j in range(9):
			if not(j == pair_pos or j == index):
				for element in candidate_list:
					if element in board_candidate_list[row_number][j]:
						board_candidate_list[row_number][j].remove(element)
				return

def find_pairs_col(col_number, candidate_list, index, board_candidate_list):
	pair_pos=-1
	if len(candidate_list) == 2:
		for i in range(9):
			if i == index:
				continue
			if candidate_list == board_candidate_list[i][col_number]:
				pair_pos = i
				break
	if not pair_pos == -1:
		for j in range(9):
			if not(j == pair_pos or j == index):
				for element in candidate_list:
					if element in board_candidate_list[j][col_number]:
						board_candidate_list[j][col_number].remove(element)
				return

def find_pairs_box(x, y, candidate_list, index_x, index_y, board_candidate_list):
	pair_pos_x=-1
	pair_pos_y=-1
	if len(candidate_list) == 2:
		for i in range(3):
			if pair_pos_x == -1:
				for j in range(3):
					if i+x == index_x and j + y == index_y:
						continue
					if candidate_list == board_candidate_list[i + x][j + y]:
						pair_pos_x = i
						pair_pos_y = j
						break
	if not pair_pos_x == -1:
		for i in range(3):
			for j in range(3):
				if not ((i == pair_pos_x and j == pair_pos_y) or (i + x == index_x and j + y == index_y)):
					for element in candidate_list:
						if element in board_candidate_list[i + x][j + y]:
							board_candidate_list[i + x][j + y].remove(element)
					return

def pointing_triple_row(x, y, candidate_list, board_candidate_list):
	for element in candidate_list:
		done=0
		for i in range(3):
			if done==1:
				break
			if not i+x//3*3 == x:
				for j in range(3):	
					if element in board_candidate_list[i+x//3*3][j+y//3*3]:
						done=1
						break
		if done == 0:
			remove_candidate_row(x, y, element, board_candidate_list)

def pointing_triple_col(x, y, candidate_list, board_candidate_list):
	for element in candidate_list:
		done=0
		for i in range(3):
			if done==1:
				break
			for j in range(3):
				if not j+y//3*3 == y:
					if element in board_candidate_list[i+x//3*3][j+y//3*3]:
						done=1
						break
		if done == 0:
			remove_candidate_col(x, y, element, board_candidate_list)


def remove_candidate_row(row, col, element, board_candidate_list):
	for i in range(9):
		if i not in [col//3*3, col//3*3+1, col//3*3+2]:
			if element in board_candidate_list[row][i]:
				board_candidate_list[row][i].remove(element)

def remove_candidate_col(row, col, element, board_candidate_list):
	for i in range(9):
		if i not in [row//3*3, row//3*3+1, row//3*3+2]:
			if element in board_candidate_list[i][col]:
				board_candidate_list[i][col].remove(element)

def remove_candidate_row_in_box(row, col, element, board_candidate_list):
	for i in range(3):
		if not i == row % 3:
			for j in range(3):
				if element in board_candidate_list[i+row//3*3][j+col//3*3]:
					board_candidate_list[i+row//3*3][j+col//3*3].remove(element)

def remove_candidate_col_in_box(row, col, element, board_candidate_list):
	for i in range(3):	
		for j in range(3):
			if not j == col % 3:
				if element in board_candidate_list[i+row//3*3][j+col//3*3]:
					board_candidate_list[i+row//3*3][j+col//3*3].remove(element)

def claiming_triple_row(x,y, candidate_list, board_candidate_list):
	for element in candidate_list:
		done = 0
		for i in range(9):
			if i not in [y//3*3, y//3*3+1, y//3*3+2]:
				if element in board_candidate_list[x][i]:
					done=1
					break
		if done == 0:
			remove_candidate_row_in_box(x,y,element, board_candidate_list)

def claiming_triple_col(x,y, candidate_list, board_candidate_list):
	for element in candidate_list:
		done = 0
		for i in range(9):
			if i not in [x//3*3, x//3*3+1, x//3*3+2]:
				if element in board_candidate_list[i][y]:
					done=1
					break
		if done == 0:
			remove_candidate_col_in_box(x,y,element, board_candidate_list)