import Piece
import Grid


class Game:

    def __init__(self):
        self.grid_size = tuple([int(x) for x in input().split()])
        self.piece = None
        self.grid = Grid.Grid(self.grid_size)

    def new_piece(self):
        letter = input()
        self.piece = Piece.Piece(letter, self.grid_size)

    def piece_locked(self, new=False):
        self.grid.piece_locked(self.piece)
        if new:
            self.new_piece()

    def check_piece(self, command="down"):
        bool = True
        if command == "right" and any(
                [self.grid.board[(cord + 1) % self.grid_size[0], (cord + 1) // self.grid_size[0]] == "0" for cord in
                 self.piece.piece_coordinates[self.piece.rotation] if
                 (cord + 1) < ((self.grid_size[0] * self.grid_size[1]) - 1)]):
            bool = False
        elif command == "left" and any(
                [self.grid.board[(cord - 1) % self.grid_size[0], (cord - 1) // self.grid_size[0]] == "0" for cord in
                 self.piece.piece_coordinates[self.piece.rotation]]):
            bool = False
        if any([self.grid.board[
                    (cord + self.grid_size[0]) % self.grid_size[0], (cord + self.grid_size[0]) // self.grid_size[0]
                ] == "0" for cord in self.piece.piece_coordinates[self.piece.rotation] if
                (cord + self.grid_size[0]) < (self.grid_size[0] * self.grid_size[1]) - 1]):
            self.piece.lock = True

        if self.piece.lock:
            self.piece_locked()

        return bool

    def start_game(self):
        command = ""
        while command != "exit":
            if command == "left":
                if command_left:
                    self.piece.left()
                else:
                    self.piece.down()
                command_left = self.check_piece(command)
            elif command == "right":
                if command_right:
                    self.piece.right()
                else:
                    self.piece.down()
                command_right = self.check_piece(command)
            elif command == "down":
                self.piece.down()
                self.check_piece()
            elif command == "rotate":
                self.piece.rotate()
                self.check_piece()
            elif command == "piece":
                self.piece_locked(new=True)
                command_right = True
                command_left = True
                self.check_piece()
            elif command == "break":
                self.check_piece()
                self.grid.check_if_line_full()
                self.piece = None

            self.grid.print_grid(self.piece)
            if self.grid.game_over and command != "piece":
                print("Game Over!")
                break

            command = input()
