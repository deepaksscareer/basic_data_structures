class Connection:

    def __init__(self, vertex, weight=1):
        
        # Edge cases
        
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return f"vertex: {self.vertex}, weight: {self.weight}"

class Graph:

    def __init__(self, directed=False):
        
        # Edge

        self.vertices = {}

        # Is directed
        self.directed = directed

    def insert_vertex(self, vertex):
        # Edge

        # If the vertex does not exist add it
        if vertex not in self.vertices:
            self.vertices[vertex] = []


    def insert_edge(self, start, end, weight=1):
        """
        Insert the vertex and then the edges
        """
        # Edge
        # Invalid, start end etc. check

        # Add the start
        self.insert_vertex(vertex=start)

        # Add the end
        self.insert_vertex(vertex=end)

        # Add from start to end
        self.vertices[start].append(Connection(vertex=end, weight=weight))

        # If this is non directed, add also from end to start
        if not self.directed:
            self.vertices[end].append(Connection(vertex=start, weight=weight))


    def print(self):

        # Normal routine
        for node, neighbors in self.vertices.items():
            # Format each node and its list of (neighbor, weight) pairs
            print(f"{node}", end=" -> ")
            for neighbour in neighbors:
                print(f"{neighbour}", end=" - ")
            
            print()

if __name__ == "__main__":
    graph = Graph(directed=False)
    graph.insert_edge(start=0, end=1, weight=1)
    graph.insert_edge(start=0, end=5, weight=1)
    graph.insert_edge(start=0, end=4, weight=1)
    graph.insert_edge(start=1, end=3, weight=1)
    graph.insert_edge(start=1, end=4, weight=1)
    graph.insert_edge(start=3, end=2, weight=1)
    graph.insert_edge(start=3, end=4, weight=1)

    graph.print()