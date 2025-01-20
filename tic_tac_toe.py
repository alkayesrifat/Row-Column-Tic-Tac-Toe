def print_board(board):
  """Prints the Tic Tac Toe board."""
  print("-------------")
  for row in board:
    print("|", end="")
    for cell in row:
      print(f" {cell} |", end="")
    print("\n-------------")

def get_player_move(player):
  """Gets the player's move."""
  while True:
    try:
      row, col = map(int, input(f"Player {player}, enter your move (row, col): ").split(","))
      if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
        return row, col
      else:
        print("Invalid move. Please try again.")
    except ValueError:
      print("Invalid input. Please enter two numbers separated by a comma.")

def check_win(board):
  """Checks if there is a winner."""
  
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return row[0]
  
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return board[0][col]
 
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return board[0][2]

  return None


board = [[" " for _ in range(3)] for _ in range(3)]


current_player = "X"
while True:
  
  print_board(board)

  row, col = get_player_move(current_player)


  board[row][col] = current_player


  winner = check_win(board)
  if winner:
    print_board(board)
    print(f"Player {winner} wins!")
    break

 
  if all(cell != " " for row in board for cell in row):
    print_board(board)
    print("It's a tie!")
    break

  current_player = "O" if current_player == "X" else "X"
