def initialize_board(m = 6, n = 7):
	"""Initializes a Connect 4 game board as a 2D list.
    :param m: The number of rows in the board.
    :param n: The number of columns in the board.
    :return: A 2D list representing the game board with each cell initialized to a space character " ".
    This function creates an empty board for a new game of Connect 4, where each cell is represented by a space character, indicating that it is unoccupied.
    """
	# Creates a 2D list (m x n) with each cell initialized as a space character " ".
	# 'm' represents the number of rows, and 'n' represents the number of columns.
	return [[" " for i in range(n)] for i in range(m)]


def display_board(board):
	"""
	Displays the current state of the Connect 4 board.
	:param board: The 2D list representing the game board.
	This function prints the board to the console with each cell separated by vertical bars and rows numbered from the bottom. It also prints column headers for easier reference during gameplay.
	"""
	# Print column headers. Numbers start from 1 to the number of columns.
	# " ".join(...) combines the column numbers into a single string with spaces.
	print("  " + " ".join([str(i) for i in range(1, len(board[0]) + 1)]))

	# Iterate over each row in the board.
	for i in range(len(board)):
		row_display = "|"  # Add the cell value and a right border to the row display.
		row_lowEdge = " +" # Initialize the string for the lower edge of the row.

		# Iterate over each cell in the current row
		for j in range(len(board[0])):
			row_display += board[i][j] + "|" # Add the cell value and a right border to the row display.
			row_lowEdge += "-+" # Add a segment to the horizontal separator.

		# Print the current row. Prepend the row number, counting from the bottom.
		print(str(len(board) - i) + row_display)

		# Print the horizontal separator after the current row.
		print(row_lowEdge)
	return


def inputStep(board, player):
    """
    Allow a player to input their move on the board.
    :param board: The current state of the game board.
    :param player: The current player (1 or 2).
    :return: A list containing the row and column where the token was placed.
    """
    # Prompt the current player to input the column number for their move.
    col = input("Player " + str(player) + ", please input the column number: ")

    # Continuously loop to handle invalid inputs.
    while True:
        try:
            # Attempt to convert the input to an integer and minus 1 for python index.
            col = int(col) - 1

            # Validate the column input.
            if col < 0 or col >= len(board[0]) or not isValid(board, col):
                # Prompt again if the input is out of range or the column is full.
                print("Invalid input. Please try again.")
                col = input("Player " + str(player) + ", please input the column number: ")
            else:
                # Break the loop if a valid column is entered.
                break
        except ValueError:
            # Handle cases where the input is not an integer.
            print("Invalid input. Please enter a number.")
            col = input("Player " + str(player) + ", please input the column number: ")

    # Assign a token based on the player number.
    sign = "X" if player == 1 else "O"

    # Place the token in the lowest empty space in the chosen column.
    for i in range(len(board) - 1, -1, -1):
        if board[i][col] == " ":
            board[i][col] = sign
            break  # Stop after placing the token.

    # Return the coordinates where the token was placed.
    return [i, col]

def isValid(board, col):
    """
    Check if a move in the given column is valid (i.e., if there is space available).
    :param board: The game board.
    :param col: The column to check.
    :return: True if the move is valid, False otherwise.
    """
    # Return True if the top cell of the column is empty, indicating space is available.
    return board[0][col] == " "





def checkWin(board, row, col, player):
    """
    Check if the last move by a player in the given row and column led to a win.
    :param board: The game board (2D list).
    :param row: The row where the last token was placed.
    :param col: The column where the last token was placed.
    :param player: The player who made the last move.
    :return: True if the player won, False otherwise.
    """
    # Determine the token (X or O) based on the player number.
    sign = "X" if player == 1 else "O"

    # Initialize a counter to keep track of consecutive tokens.
    count = 0

    # Check for a vertical win.
    for i in range(len(board)):
        if board[i][col] == sign:  # Check if the current cell contains the player's token.
            count += 1  # Increment the count for consecutive tokens.
            if count == 4:  # Check if there are 4 consecutive tokens.
                return True  # Return True indicating a win.
        else:
            count = 0  # Reset the count if a different token is encountered.

    # Check for a horizontal win.
    for j in range(len(board[0])):
        if board[row][j] == sign:  # Check if the current cell contains the player's token.
            count += 1  # Increment the count for consecutive tokens.
            if count == 4:  # Check if there are 4 consecutive tokens.
                return True  # Return True indicating a win.
        else:
            count = 0  # Reset the count if a different token is encountered.

    # Check for a diagonal win (down-right and up-left).
    count = 0
    for d in range(-3, 4):
        if 0 <= row + d < len(board) and 0 <= col + d < len(board[0]) and board[row + d][col + d] == sign:
            count += 1  # Increment the count for consecutive tokens.
            if count == 4:  # Check if there are 4 consecutive tokens.
                return True  # Return True indicating a win.
        else:
            count = 0  # Reset the count if the sequence is broken.

    # Check for a diagonal win (down-left and up-right).
    count = 0
    for d in range(-3, 4):
        if 0 <= row + d < len(board) and 0 <= col - d < len(board[0]) and board[row + d][col - d] == sign:
            count += 1  # Increment the count for consecutive tokens.
            if count == 4:  # Check if there are 4 consecutive tokens.
                return True  # Return True indicating a win.
        else:
            count = 0  # Reset the count if the sequence is broken.

    # Return False if no win condition is met.
    return False


def runGame():
	"""
	Runs the Connect 4 game.
	This function controls the game flow, alternating between players,
	displaying the game board, and checking for a win after each move.
	"""
	# Initialize the game board with specific dimensions, e.g., 6 rows and 7 columns.
	gameBoard = initialize_board(6, 7)
	# Display the current state of the game board.
	display_board(gameBoard)

	# Set the starting player.
	player = 1

	# Main game loop.
	while True:


		# Get the current player's move.
		lastStep = inputStep(gameBoard, player)

		# Display the board again to show the result of the last move.
		display_board(gameBoard)

		# Check if the last move resulted in a win.
		if checkWin(gameBoard, lastStep[0], lastStep[1], player):
			print("Player " + str(player) + " WINS the game!!!")
			break  # End the game if there's a winner.
		else:
			# Switch to the other player.
			player = 2 if player == 1 else 1

def main():
    """
    The main function to run the Connect 4 game. It allows players to play multiple rounds of the game
    and decide whether to start a new game after each round.
    """
    while True:
        # Run a round of the game.
        runGame()

        # Loop to handle the response for a new game.
        while True:
            # Ask if players want to play another round.
            newGame = input("Wanna play another round? (yes/no): ")

            # Convert the input to lower case for case-insensitive comparison.
            newGame = newGame.lower()

            # Check if the response is either 'yes' or 'no'.
            if newGame in ["yes", "no"]:
                break  # Exit the loop if a valid response is given.
            else:
                # Show an error message if the input is not valid.
                print("Invalid input. Please answer with 'yes' or 'no'.")

        # Exit the main loop and end the game if the answer is 'no'.
        if newGame == "no":
            break

    return


'''
GOOD LUCK CHRISTINE 
 /\_/\  
( o.o ) 
 > ^ <

'''

main()

