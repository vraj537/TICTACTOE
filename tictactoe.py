# tic_tac_toe.py

import tkinter as tk
from itertools import cycle

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = None
        self.players = cycle([("X", "blue"), ("O", "red")])
        self.board = [[None]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.status = tk.Label(root, text="Welcome to Tic-Tac-Toe!", font=("Arial", 14))
        self.status.grid(row=0, column=0, columnspan=3, pady=10)
        self.build_board()
        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, state='disabled')
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.next_turn()

    def build_board(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.root, text="", width=6, height=3,
                                font=("Arial", 24),
                                command=lambda r=r, c=c: self.on_click(r, c))
                btn.grid(row=r+1, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

    def on_click(self, row, col):
        if not self.buttons[row][col]["text"] and self.current_player:
            mark, color = self.current_player
            self.buttons[row][col].config(text=mark, fg=color)
            self.board[row][col] = mark
            if self.check_winner(mark):
                self.status.config(text=f"Player {mark} wins!", fg=color)
                self.end_game()
            elif all(self.board[r][c] for r in range(3) for c in range(3)):
                self.status.config(text="It's a tie!", fg="green")
                self.end_game()
            else:
                self.next_turn()

    def next_turn(self):
        self.current_player = next(self.players)
        mark, color = self.current_player
        self.status.config(text=f"Player {mark}'s turn", fg=color)

    def check_winner(self, mark):
        lines = (
            [(r, c) for c in range(3)] for r in range(3)
        ), (
            [(r, c) for r in range(3)] for c in range(3)
        ), (
            [(i, i) for i in range(3)],
            [(i, 2 - i) for i in range(3)]
        )
        for group in lines:
            for line in group:
                if all(self.board[r][c] == mark for r, c in line):
                    for r, c in line:
                        self.buttons[r][c].config(bg="yellow")
                    return True
        return False

    def end_game(self):
        self.current_player = None
        self.reset_button.config(state='normal')

    def reset_game(self):
        self.board = [[None]*3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                btn = self.buttons[r][c]
                btn.config(text="", bg=self.root.cget('bg'))
        self.reset_button.config(state='disabled')
        self.next_turn()

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
