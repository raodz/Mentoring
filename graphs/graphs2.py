from typing import List


class Graph:
    def __init__(self):
        self.matrix: List[List[int]] = []
        self.no_vertices = 0

    def add_vertex(self) -> None:
        self.no_vertices += 1

        for vertices in self.matrix:
            vertices.append(0)

        self.matrix.append([0] * self.no_vertices)

    def get_neighbours(self, id) -> List[int]:
        return self.matrix[id]

    def add_edge(self, start, end, weight) -> None:
        if self.matrix[end][start] == 0:
            self.matrix[start][end] = weight
        else:
            print(f'There is already a connection from {end} to {start}')

    def show_graph(self) -> None:
        for id, vertices in enumerate(self.matrix):
            print(str(id) + ' sends connection to: ' + ', '.join(
                [str(nbr_id) for nbr_id, weight in enumerate(vertices) if weight != 0]))

    def search(self, start_vertex: int, mode: str = 'dts'):
        modes = {'dts': 0, 'bts': -1}
        visited_vertices = []
        stack = [start_vertex]
        while len(stack) > 0:
            curr_vertex = stack.pop(modes[mode])
            # print(curr_vertex)
            if curr_vertex not in visited_vertices:
                visited_vertices.append(curr_vertex)
                curr_connections = self.get_neighbours(curr_vertex)
                for i in range(len(curr_connections)):
                    if curr_connections[i] > 0:
                        stack.insert(0, i)
                # print(stack)
        return visited_vertices


g = Graph()

for i in range(8):
    g.add_vertex()

g.add_edge(0, 2, 1)
g.add_edge(0, 5, 6)
g.add_edge(0, 4, 2)
g.add_edge(1, 7, 9)
g.add_edge(2, 3, 5)
g.add_edge(3, 6, 2)
g.add_edge(4, 2, 3)
g.add_edge(4, 1, 10)
g.add_edge(5, 1, 8)
g.add_edge(5, 4, 2)
g.add_edge(6, 7, 12)
g.add_edge(7, 0, 1)

print(g.search(0, mode='dts'))
print(g.search(0, mode='bts'))
