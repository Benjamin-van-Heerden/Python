class KnightsTour:

    def __init__(self, board_size):
        self.board_size = board_size
        # possible horizontal components of the moves
        # horizontal (+) -> move right
        # veritical (+) -> move down
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]

    def solve_problem(self):
        # start in top left corner
        self.solution_matrix[0][0] = 0

        # solve(counter, location_row, location_col)
        if self.solve(1, 0, 0):
            self.print_solution()
        else:
            print("No feasible solution!")

    def solve(self, step_counter, x, y):

        # base case
        if step_counter == self.board_size**2:
            return True

        # consider all the possible moves and find the valid one
        for move_index in range(len(self.x_moves)):
            # try all the possible moves
            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_move(next_x, next_y):
                # valid step so we can update the solution matrix
                self.solution_matrix[next_x][next_y] = step_counter

                if self.solve(step_counter+1, next_x, next_y):
                    return True

                # BACKTRACKING - reset the cell to be -1
                self.solution_matrix[next_x][next_y] = -1
        
        return False

    def is_valid_move(self, x, y):
        
        # make sure the knight does not step outside the chessboard
        if x < 0 or x >= self.board_size:
            return False

        if y < 0 or y >= self.board_size:
            return False

        # now check wheter the space has been visited or not
        if self.solution_matrix[x][y] == -1:
            return True
        
        return False

    def print_solution(self):
        print()
        print(f"Knights Tour On A {self.board_size}X{self.board_size} Board\n")
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(f"\t{self.solution_matrix[i][j]}", end="")
            print("\n")
            



if __name__ == "__main__":
    tour = KnightsTour(8)
    tour.solve_problem()