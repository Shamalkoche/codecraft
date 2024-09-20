# Question : Depth-First Search (DFS) Sample Problem: Implement DepthFirst Search (DFS) to traverse a graph starting from a given vertex.The graph is represented by an adjacency list
# Define the graph as an adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        # Mark the current node as visited
        visited.add(start)
        print(start)  # Process the node (e.g., print it)

        # Recursively visit all the adjacent vertices
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    
    print("DFS traversal starting from vertex 0:")
    g.dfs(0)
