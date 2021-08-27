class MazeProblem:

    def __init__(self, maze_table):
        self.maze_table = maze_table
        self.maze_size = len(maze_table)
        self.solution_table = [[0 for _ in range(self.maze_size)] for _ in range(self.maze_size)]

    def solve_maze(self):

        if self.solve(0, 0):
            self.show_result()
        else:
            print("No feasible solution!")

    def solve(self, x, y):

        if self.is_finished(x, y):
            self.solution_table[x][y] = 1
            return True

        if self.is_valid(x, y):
            # the point is valid so set it as part of the solution
            self.solution_table[x][y] = 1

            # try moving in x first
            if self.solve(x+1, y):
                return True

            # move in y
            if self.solve(x, y+1):
                return True

            # if we get here the solution is not feasible - BACKTRACKING
            self.solution_table[x][y] = 0

    def is_finished(self, x, y):
        # the finished position is defined to be the bottom right of the maze
        if x == y and x == self.maze_size-1:
            return True
        return False

    def is_valid(self, x, y):
        # x and y must be within the maze
        if x < 0 or x >= self.maze_size: return False
        if y < 0 or y >= self.maze_size: return False
        # if there is a wall the point is not valid
        if self.maze_table[x][y] == 0: return False

        return True

    def show_result(self):
        print()
        print("Maze Solution: (-|-: Wall, ***: Unused Path Cell)")
        print()
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if self.solution_table[i][j] == 1:
                    print("\tSSS", end="")
                elif self.maze_table[i][j] == 0:
                    print("\t-|-", end="")
                else:
                    print("\t***", end="")
            print("\n")



if __name__ == "__main__":
    maze1 = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1]
    ]

    maze_problem = MazeProblem(maze1)
    maze_problem.solve_maze()