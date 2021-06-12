class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, start, end, weight):
        self.graph.append([start, end, weight])

    def printArr(self, dist):
        ls = ["A", "B", "C", "D", "E"]
        for i in range(self.V):
            print("Дистанція до", ls[i], dist[i])

    def BellmanFord(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for start, end, weight in self.graph:
                if dist[start] != float("Inf") and dist[start] + weight < dist[end]:
                    dist[end] = dist[start] + weight

        for start, end, weight in self.graph:
            if dist[start] != float("Inf") and dist[start] + weight < dist[end]:
                print("Якісь проблеми, Шериф?")
                return

        self.printArr(dist)


g = Graph(5)

# A = 0, B = 1, C = 2, D = 3, E = 4,
g.addEdge(0, 1, 6)
g.addEdge(0, 3, 1)

g.addEdge(1, 0, 6)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)

g.addEdge(2, 1, 5)
g.addEdge(2, 4, 5)

g.addEdge(3, 0, 1)
g.addEdge(3, 1, 2)
g.addEdge(3, 4, 1)

g.addEdge(4, 3, 1)
g.addEdge(4, 1, 2)
g.addEdge(4, 2, 5)

g.BellmanFord(0)