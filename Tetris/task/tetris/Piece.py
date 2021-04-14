import numpy as np
import copy


class Piece:
    piece_dict = {"O": np.array([[4, 14, 15, 5]]),
                  "I": np.array([[4, 14, 24, 34], [3, 4, 5, 6]]),
                  "S": np.array([[5, 4, 14, 13], [4, 14, 15, 25]]),
                  "Z": np.array([[4, 5, 15, 16], [5, 15, 14, 24]]),
                  "L": np.array([[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]),
                  "J": np.array([[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]),
                  "T": np.array([[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]])}

    def __init__(self, letter, grid_size):
        self.piece_coordinates = copy.copy(self.piece_dict[letter])
        self.grid_size = grid_size
        self.rotation = 0
        self.lock = False

    def down(self):
        if not self.lock:
            self.piece_coordinates += self.grid_size[0]
            if any(self.piece_coordinates[self.rotation] - self.grid_size[0] * (self.grid_size[1] - 1) > 0):
                self.lock = True

    def left(self):
        if not self.lock:
            if not any(self.piece_coordinates[self.rotation] % self.grid_size[0] == 0):
                self.piece_coordinates -= 1
            self.down()

    def right(self):
        if not self.lock:
            if not any(self.piece_coordinates[self.rotation] % self.grid_size[0] == self.grid_size[0] - 1):
                self.piece_coordinates += 1
            self.down()

    def rotate(self):
        if not self.lock:
            self.rotation = (self.rotation + 1) % self.piece_coordinates.shape[0]
            self.down()
