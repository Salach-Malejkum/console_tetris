import numpy as np


class Grid:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.board = np.full((self.grid_size[0], self.grid_size[1]), "-")
        self.game_over = False

    def print_grid(self, piece_inst=None):
        for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                if piece_inst is not None and (i * self.grid_size[0] + j) in piece_inst.piece_coordinates[piece_inst.rotation]:
                    if j == self.grid_size[0] - 1:
                        print("0")
                    else:
                        print("0 ", end="")
                else:
                    if j == self.grid_size[0] - 1:
                        print(self.board[j, i])
                    else:
                        print(self.board[j, i], end=" ")
        print()

    def piece_locked(self, piece_inst):
        if piece_inst:
            for num in piece_inst.piece_coordinates[piece_inst.rotation]:
                self.board[num % self.grid_size[0], num // self.grid_size[0]] = "0"
            self.check_if_lost()

    def check_if_lost(self):
        if any(self.board[:, 0] == "0"):
            self.game_over = True

    def remove_line(self, index):
        for i in range(index, -1, -1):
            for j in range(self.grid_size[0]):
                if i == 0:
                    self.board[j, i] = "-"
                else:
                    self.board[j, i] = self.board[j, i - 1]

    def check_if_line_full(self):
        for i in range(self.board.shape[1]):
            if all(self.board[:, i] == "0"):
                self.remove_line(i)
