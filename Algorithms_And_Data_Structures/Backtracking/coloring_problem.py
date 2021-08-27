class ColoringProblem:

    def __init__(self, adjacency_matrix, num_colors):
        self.adjacency_matrix = adjacency_matrix
        self.n = len(adjacency_matrix)
        self.num_colors = num_colors
        self.colors = [0 for _ in range(self.n)]

    def coloring_problem(self):

        # we call the solve function with the first vertex
        if self.solve(0):
            self.show_result()
        else:
            print("There is no feasible solution!")

    def solve(self, vertex_index):

        # base case - if we have used up every vertex we are done
        if vertex_index == self.n:
            return True

        # consider the colors
        for color_index in range(1, self.num_colors+1):
            if self.is_color_valid(vertex_index, color_index):
                self.colors[vertex_index] = color_index

                if self.solve(vertex_index+1):
                    return True

                # BACKTRACKING
                # in a sense backtracking here means doing nothing

        return False

    def is_color_valid(self, vertex_index, color_index):

        # check if the nodes are connected and the given color is not shared between the vertices
        for i in range(self.n):
            if self.adjacency_matrix[vertex_index][i] == 1 and color_index == self.colors[i]:
                return False

        return True

    def show_result(self):
        for v, c in zip(range(self.n), self.colors):
            print(f"Vertex {v} has color {c}")


if __name__ == "__main__":
    m = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    coloring = ColoringProblem(m, 3)
    coloring.coloring_problem()
