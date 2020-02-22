from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, root):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(root)
        visited[root] = True

        while queue:
            root = queue.pop(0)
            print(root),
            for i in self.graph[root]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Breadth First Traversal: ")
    g.bfs(2)