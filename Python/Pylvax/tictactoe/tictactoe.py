# we start from planning on data structure

table_size = 5
win_length = 4

# if we define i and get do while until it is smaller
# than we should better use for loop

def generate_table (table_size):
	
	table = list()

	for _ in range (table_size):
		row = list()
		for _ in range(table_size):
			row.append(0)
		table.append(row)
# if we do not need a variable, we use underscore _ . It can also be applied to tuple

# the better way is 

T = [[0]] * 6] * 6 # the star does not copy it 

# but there is a problem - WHY? homework
# ANSWER - every row is the same object


a = [[1]] for _ in range[5]] # take 5 elements from a list and put them into a list

# mutable vs immutable 
# immutable are strings, integers, immutable,  and boolean - if you change a value the id also changes
# mutable are list, dict, set - the value changes and the id is the same
# set goes with curly braces - a {1,2,3}, tuple - a(1,2,3)

a = 'abcd' + 'hello' # calcualte value at right and put a lable of 'a' on it

# the correct code is 
T = [[0] * 6 for _ in range(6)

table_size  = 7
T = T = [[0] * table_size for _ in range(table_size)

def print_table():
	lookup = ['-'. 'x', 'o']
	for row in T:
		print (" ".join([lookup[cell]] for cell in row])		

# every function checks first its local scope and then checks the global
# to use variable outside the scopoe use word "global" -> global hello

def move(player, row, column):
	if player not in [1,2]:
		return False
	...
# the second strategy is to return an exception
# the third strategy is assert

try: 
	a = move(3, 2, 4)
except ValueError:
	print 'error heppened, try again'

####

try:
	a = move(3,2,4)
except AssertionError as e:
	print 'error happanened, try again: ', e

####

def move (player, row, column):

	row -= 1
	column -= 1

	assert row in range(table_size), 'row out of range'
	assert column in range(table_size), 'column out of range'
	assert T[row][column] == 0, 'illegal move'
	assert player == next_player, 'player not valid'

	T[row][column] = player

	global next_player
	if next_player == 1:
		next_player = 2
	else:
		next_player = 1

	print_table()

def is_winner(row, column):
	global table_size
	global win_length
	# row = 2
	# column = 1
	win_diagonal = 1
	win_horizontal = 1
	win_vertical = 1

	# checking at the NE
	i = 1 
	while (row-i >= 1 or column-i >= 1):
		if T[row-i][column-i] == T[row][column]:
			win_diagonal += 1
			if win_diagonal == win_length:
				victory()
			else: i+=1
		else: break

	# cheking at the SW
	i = 1
	while (row+i <= table_size or column+i <= table_size):
		if T[row+i][column+i] == T[row][column]:
			win_diagonal += 1
			if win_diagonal == win_length:
				victory()
			else: i+=1
		else: break
	
	# checking horizontal left
	i = 1
	while (column-i >= 1):
		if T[row][column-i] == T[row][column]:
			win_horizontal += 1
			if win_horizontal == win_length:
				victory()
			else: i+=1
		else: break


	# checking horizontal right
	i = 1
	while (column+i <= table_size):
		if T[row][column+i] == T[row][column]:
			win_horizontal += 1
			if win_horizontal == win_length:
				victory()
			else: i+=1
		else: break

	# checking vertical to top
	i = 1
	while (row-i >= 1):
		if T[row-i][column] == T[row][column]:
			win_horizontal += 1
			if win_horizontal == win_length:
				victory()
			else: i+=1
		else: break

	# checking vertical to bottom
	i = 1
	while (row+i >= 0):
		if T[row+i][column] == T[row][column]:
			win_horizontal += 1
			if win_horizontal == win_length:
				victory()
			else: i+=1

	# ortog_to_zero(array):
	# # row_changing index 0 -1
	# # row_stuck index 1 2
	# # column_changing index 2 3
	# # column_stuck index 3 -1
	# # if not applicable than value should be -1

	# 	# checking column
	# 	if (array[1] > 0 and array[2] > 0):
	# 		i = 1
	# 		while (array[2] >= 0):
	# 			if T[array[1]][array[2]-i] == T[array[1]][array[2]]:
	# 				win_horizontal += 1
	# 				if win_horizontal == win_length:
	# 					victory()
	# 				else: i+=1
	# 			else: break

	# 	elif (array[0] > 0 and array[3] > 0):
	# 		while ()







def is_winner_cell(row,column):
	# horizontal, row is the same



  0 1 2 3 4 
0 X 
1   X
2   O X
3       X
4         X
           
next_player = 1

