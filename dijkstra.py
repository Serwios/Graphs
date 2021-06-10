import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        ls = ["A", "B", "C", "D", "E"]
        for node in range(self.V):
            print("Дистанція до", ls[node], dist[node])

    def minDistance(self, dist, sptSet):
        global min_index
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)



g = Graph(5)

g.graph = [[0, 6, 0, 1, 0],
           [6, 0, 5, 2, 2],
           [0, 5, 0, 0, 5],
           [1, 2, 0, 0, 1],
           [0, 2, 5, 1, 0]]


g.dijkstra(0)