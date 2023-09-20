import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create variables to track player turns and board state
player_x_turn = True
board = [["" for _ in range(3)] for _ in range(3)]

# Function to check for a win or a draw
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Draw"
    return False

# Function to handle button clicks
def button_click(row, col):
    global player_x_turn

    if board[row][col] == "" and not check_winner():
        if player_x_turn:
            board[row][col] = "X"
            buttons[row][col].config(text="X", fg="blue")
        else:
            board[row][col] = "O"
            buttons[row][col].config(text="O", fg="red")

        player_x_turn = not player_x_turn

        result = check_winner()
        if result:
            if result == "Draw":
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {result} wins!")
            root.quit()

# Create buttons for the Tic Tac Toe grid
buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Run the main loop
root.mainloop()
