
import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Create the game board
        self.board = [" "] * 9
        self.buttons = []

        # Create the game board GUI
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", width=5, height=2,
                                  command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # Create the restart button
        self.restart_button = tk.Button(master, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)

        self.current_player = "X"

    def make_move(self, row, col):
        if self.board[row * 3 + col] == " ":
            self.board[row * 3 + col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.check_winner()
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                self.display_winner(self.board[i])
                return

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                self.display_winner(self.board[i])
                return

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            self.display_winner(self.board[0])
            return
        if self.board[2] == self.board[4] == self.board[6] != " ":
            self.display_winner(self.board[2])
            return

        # Check for a tie
        if " " not in self.board:
            self.display_winner("tie")

    def display_winner(self, winner):
        if winner == "tie":
            message = "It's a tie!"
        else:
            message = f"Player {winner} wins!"
        tk.messagebox.showinfo("Winner", message)
        self.restart_game()

    def restart_game(self):
        self.board = [" "] * 9
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.config(text=" ")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
