class QueensProblem:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def solve_n_queens(self):
        # we start with the first queen (with index 0)
        if self.solve(0):
            self.print_queens()
        else:
            # when we have considered all the possible configurations without success then there is no solution e.g (3x3)
            print("There is no solution to the problem!")

    # col index is the same as the index of the queen
    def solve(self, col_index):
        # we have to check if we have solved the problem - base case
        if col_index == self.n:
            return True

        # try to find a position for queen (col_index) within a given column
        for row_index in range(self.n):
            if self.is_valid_place(row_index, col_index):
                # 1 means there is a queen at the location
                self.chess_table[row_index][col_index] = 1

                # we call the solve function with the next queen
                # hence, try to find the location of the next queen in the next column
                if self.solve(col_index+1):
                    return True
                
                # BACKTRACK
                # print("BACKTRACKING...")
                self.chess_table[row_index][col_index] = 0
        
        # when we have considered all the rows in a column for a given queen we backtrack!
        return False

    def is_valid_place(self, row_index, col_index):
        # check the rows (queens can attack horizontally)
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        # do not have to check the columns
        
        # check the diagonals
        # from top left to bottom right
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            
            if self.chess_table[i][j] == 1:
                return False
            
            j -= 1
        
        # from top right to bottom left
        j = col_index
        for i in range(row_index, self.n):
            if j < 0:
                break
            
            if self.chess_table[i][j] == 1:
                return False
            
            j -= 1

        return True




    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print("\n")


if __name__ == "__main__":
    queens = QueensProblem(8 )
    queens.solve_n_queens()
