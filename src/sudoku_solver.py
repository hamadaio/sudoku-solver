#board = [[]*9]*9

board = [[0,2,0,5,0,1,0,9,0],
		 [8,0,0,2,0,3,0,0,6],
		 [0,3,0,0,6,0,0,7,0],
		 [0,0,1,0,0,0,6,0,0],
		 [5,4,0,0,0,0,0,1,9],
		 [0,0,2,0,0,0,7,0,0],
		 [0,9,0,0,3,0,0,8,0],
		 [2,0,0,8,0,4,0,0,7],
		 [0,1,0,9,0,7,0,6,0]]

'''
board=[
   list("000000000"),
   list("503067000"),
   list("900342100"),
   list("000004000"),
   list("001000720"),
   list("002010000"),
   list("030000009"),
   list("080100200"),
   list("000750806")]


board=[
   list("007200090"),
   list("000130050"),
   list("240000800"),
   list("060000008"),
   list("000459000"),
   list("900000070"),
   list("008000016"),
   list("050081000"),
   list("010003200")]
'''

for i in range(9):
	for j in range(9):
		board[i][j]=int(board[i][j])
	print(board[i])
print()



#loop row and remove matches to candidate_list
def eliminate_candidates_row(row_number, candidate_list):
	for i in range(9):
		if board[row_number][i] in candidate_list:
			candidate_list.remove(board[row_number][i])

def eliminate_candidates_col(col_number, candidate_list):
	for i in range(9):
		if board[i][col_number] in candidate_list:
			candidate_list.remove(board[i][col_number])

def eliminate_candidates_box(x, y, candidate_list):
	for i in range(3):
		for j in range(3):
			if board[x+i][y+j] in candidate_list:
				candidate_list.remove(board[x+i][y+j])

def compare_candidate_list_row(row_number, candidate_list, index):
	for candidate_value in candidate_list:
		for i in range(9):
			if i == index:
				continue
			if candidate_value in board_candidate_list[row_number][i]:
				#print("break", candidate_value)
				break
			elif i == 8 or i == 7 and index == 8:
				return candidate_value
	return 0

def compare_candidate_list_col(col_number, candidate_list, index):
	for candidate_value in candidate_list:
		for i in range(9):
			if i == index:
				continue
			if candidate_value in board_candidate_list[i][col_number]:
				#print("break", candidate_value)
				break
			elif i == 8 or i == 7 and index == 8:
				return candidate_value
	return 0

def compare_candidate_list_box(x, y, candidate_list, index_x, index_y):
	done = False
	#print(candidate_list)
	for candidate_value in candidate_list:
		for i in range(3):
			for j in range(3):
				#print('box for j', board_candidate_list[x + i][y + j])
				if i == index_x and j == index_y:
					continue
				if candidate_value in board_candidate_list[x + i][y + j]:
					done = True
					break
				elif (i == 2 and j == 2) or (i == 2 and j == 1 and index_x == x + 2 and index_y == y + 2):
					return candidate_value
			if(done == True):
				break	
	return 0

def find_pairs_row(row_number, candidate_list, index):
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
						print('row before',board_candidate_list[row_number][i])
						board_candidate_list[row_number][j].remove(element)
				return

def find_pairs_col(col_number, candidate_list, index):
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
						print('col before',board_candidate_list[j][col_number])
						board_candidate_list[j][col_number].remove(element)
				return

def find_pairs_box(x, y, candidate_list, index_x, index_y):
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
				if not (i == pair_pos_x and j == pair_pos_y) or (i + x == index_x and j + y == index_y):
					for element in candidate_list:
						if element in board_candidate_list[i + x][j + y]:
							print('box before',board_candidate_list[i + x][j + y])
							board_candidate_list[i + x][j + y].remove(element)
					return

def pointing_triple_row(x, y, candidate_list):
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
			remove_candidate_row(x, y, element)

def pointing_triple_col(x, y, candidate_list):
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
			remove_candidate_col(x, y, element)


def remove_candidate_row(row, col, element):
	for i in range(9):
		if i not in [col//3*3, col//3*3+1, col//3*3+2]:
			if element in board_candidate_list[row][i]:
				print('pointing triple Row removing', element, 'from list at', row,i)
				board_candidate_list[row][i].remove(element)

def remove_candidate_col(row, col, element):
	for i in range(9):
		if i not in [row//3*3, row//3*3+1, row//3*3+2]:
			if element in board_candidate_list[i][col]:
				print('pointing triple Col removing', element, 'from list at', i,col)
				board_candidate_list[i][col].remove(element)

def remove_candidate_row_in_box(row, col, element):
	for i in range(3):
		if not i == row % 3:
			for j in range(3):
				if element in board_candidate_list[i+row//3*3][j+col//3*3]:
					print('claiming triple col removing', element, 'from list at', i+row//3*3,j+col//3*3, 'coordinates', row, col)
					board_candidate_list[i+row//3*3][j+col//3*3].remove(element)

def remove_candidate_col_in_box(row, col, element):
	for i in range(3):	
		for j in range(3):
			if not j == col % 3:
				if element in board_candidate_list[i+row//3*3][j+col//3*3]:
					print('claiming triple col removing', element, 'from list at', i+row//3*3,j+col//3*3, 'coordinates', row, col)
					board_candidate_list[i+row//3*3][j+col//3*3].remove(element)

def claiming_triple_row(x,y, candidate_list):
	for element in candidate_list:
		done = 0
		for i in range(9):
			if i not in [y//3*3, y//3*3+1, y//3*3+2]:
				if element in board_candidate_list[x][i]:
					done=1
					break
		if done == 0:
			remove_candidate_row_in_box(x,y,element)

def claiming_triple_col(x,y, candidate_list):
	for element in candidate_list:
		done = 0
		for i in range(9):
			if i not in [x//3*3, x//3*3+1, x//3*3+2]:
				if element in board_candidate_list[i][y]:
					done=1
					break
		if done == 0:
			remove_candidate_col_in_box(x,y,element)



#=================================MAIN=============================


#board_candidate_list = [[['x']*9]*9]*9
board_candidate_list = []
for x in range(9):
	board_candidate_list.append([])
	for y in range(9):
		board_candidate_list[x].append([])
		if board[x][y] > 0:
			board_candidate_list[x][y].append(board[x][y])
		else:
			for z in range(1,10):
				board_candidate_list[x][y].append(z)

cont = 0
while cont<2:

	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				eliminate_candidates_row(i, board_candidate_list[i][j])		
				eliminate_candidates_col(j, board_candidate_list[i][j])
				eliminate_candidates_box((i//3)*3, (j//3)*3, board_candidate_list[i][j])
				if len(board_candidate_list[i][j]) == 1:
					board[i][j]=board_candidate_list[i][j][0]
					print(board_candidate_list[i][j])
					print("change was made!", i,j)
				catch_compare = compare_candidate_list_row(i,board_candidate_list[i][j], j)
				if catch_compare:
					board_candidate_list[i][j] = [catch_compare]
					board[i][j] = catch_compare
				catch_compare = compare_candidate_list_col(j,board_candidate_list[i][j], i)
				if catch_compare:
					board_candidate_list[i][j] = [catch_compare]
					board[i][j] = catch_compare
				catch_compare = compare_candidate_list_box(i//3*3, j//3*3, board_candidate_list[i][j], i, j)
				if catch_compare:
					board_candidate_list[i][j] = [catch_compare]
					board[i][j] = catch_compare
				find_pairs_row(i, board_candidate_list[i][j], j)
				find_pairs_col(j, board_candidate_list[i][j], i)
				find_pairs_box(i//3*3, j//3*3, board_candidate_list[i][j], i, j)
				pointing_triple_row(i, j, board_candidate_list[i][j])
				pointing_triple_col(i, j, board_candidate_list[i][j])
				claiming_triple_row(i,j, board_candidate_list[i][j])
				claiming_triple_col(i,j, board_candidate_list[i][j])

	for i in range(9):
		print(board[i])
	print()
	cont+=1