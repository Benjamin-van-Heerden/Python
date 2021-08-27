class HamiltonianPath:

    def __init__(self, adjacency_matrix):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]

    def hamiltonian_path(self):

        if self.solve(1):
            self.show_path()
        else:
            print("No solution exists!")

    def solve(self, position):
        # BASE CASE

        if position == self.n:
            # Already considered all nodes (index starting from 0)
            return True

        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                # include this vertex in the solution
                self.path.append(vertex_index)

                if self.solve(position+1):
                    return True

                # when we have to backtrack we remove this vertex from the path
                self.path.pop()

        # have considered all the vertices without success
        return False

    def is_feasible(self, vertex, actual_posision):

        # make sure the vertex is connected
        if self.adjacency_matrix[self.path[actual_posision-1]][vertex] == 0:
            return False

        # check if the vertex is already included
        for i in range(actual_posision):
            if self.path[i] == vertex:
                return False

        return True

    def show_path(self):
        for v in self.path:
            print(v)

if __name__ == "__main__":
    m = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0],
    ]

    hamilton_path = HamiltonianPath(m)
    hamilton_path.hamiltonian_path()

