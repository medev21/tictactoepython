import random

def show_board(arr_board):
	#displays the tictactoe board view
	print('')
	print(str(arr_board[6])  + ' | ' + str(arr_board[7]) + ' | ' +  str(arr_board[8]))
	print('_________')
	print(str(arr_board[3])  + ' | ' + str(arr_board[4]) + ' | ' +  str(arr_board[5]))
	print('_________')
	print(str(arr_board[0])  + ' | ' + str(arr_board[1]) + ' | ' +  str(arr_board[2]))

def game():
	board =  [0,1,2, 3,4,5, 6,7,8]	#tictactoe array numbers

	print('type the letter you want to be, X or O\n')
	player_symbol = input().upper()	#gets the player's symbol
	if player_symbol =='X':
		comp_symbol = 'O'
	else:
		comp_symbol = 'X'

	show_board(board)	#call the show_board function init setpu

	count = 1
	while True:
		print('\n\nPlease enter the number you wish to place your move, you are the ' + player_symbol + ' btw\n')
		player_position = int(input())	#get the player position by pressing a number and convert it to an integer

		#set the player symbol if not filled by x or o, else ask again for input
		while True:
			if board[player_position] == 'X' or board[player_position] == 'O':
				print('\nPlease try again, that position has been taken\n')
				player_position = int(input())
			else:
				board[player_position] = player_symbol
				break

		#call computer_move function and store modified board and computer position
		board, comp_position = computer_move(board, player_position, comp_symbol)

		print("\ncomputer's move is " + str(comp_position))
		show_board(board)	#display updated board with player and computers move

		#call check_winner function by returning a boolean
		if check_winner(board,player_symbol):	#check player winning status
			print('\nYou won the game')
			return False	#get out of the while loop
		elif check_winner(board,comp_symbol):	#check computer winning status
			print("\nSorry, the computer beat you and it's smarter than you")
			return False	#get out of the while loop
		elif comp_position == 'Out':	#check if game it's a Draw
			print("\nDraw, nobody wins")
			return False	#get out of the while loop

def check_winner(board, symbol):
	#check diffirent winning combinations
	#horizontal
	if board[6] == symbol and board[7] == symbol and board[8] == symbol:
		return True
	elif board[3] == symbol and board[4] == symbol and board[5] == symbol:
		return True
	elif board[0] == symbol and board[1] == symbol and board[2] == symbol:
		return True
	#vertical
	elif board[6] == symbol and board[3] == symbol and board[0] == symbol:
		return True
	elif board[7] == symbol and board[4] == symbol and board[1] == symbol:
		return True
	elif board[8] == symbol and board[5] == symbol and board[2] == symbol:
		return True
	#diagonal
	elif board[6] == symbol and board[4] == symbol and board[2] == symbol:
		return True
	elif board[8] == symbol and board[4] == symbol and board[0] == symbol:
		return True
	else:
		return False

def check_draw(board):
	bool = True
	for val in board:
		if type(val) is int:
			bool = False
			break
	return bool

def computer_move(board, player_position, comp_symbol):
	while True:
		comp_position = random.randint(0,8)	#get random number between 0 and 8
		check_pos = board[comp_position]	#set computer position and check if it's available

		#if check_pos type is an integer, then set the computer symbol in the board
		if type(check_pos) is int:
			board[comp_position] = comp_symbol
			break
		#else, check it's out of move by calling check_draw function
		elif check_draw(board):
			comp_position = 'Out'
			break
	return (board, comp_position)

game()
