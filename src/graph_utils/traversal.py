"""Utility functions for traversing graphs."""



def breadth_first(start_node):
    """An implementation of breadth-first traversal."""
    # TODO: Add support for yielding each node as it is visited and popped from queue.
    start_node.visited = True
    queue = [start_node]
    while queue:
        current_node = queue.pop(0)
        for node in current_node.edges:
            if not node.visited:
                node.visited = True
                queue.append(node)

def dfs(graph, start_node):
    """An implementation of depth-first traversal."""
    raise NotImplementedError

def dijkstra(graph, start_node):
    """An implementation of Dijkstra's shortest path algorithm."""
    raise NotImplementedError

def bellman_ford(graph, start_node):
    """An implementation of Bellman-Ford shortest path algorithm."""
    raise NotImplementedError

def prim(graph):
    """An implementation of Prim's minimum spanning tree algorithm."""
    raise NotImplementedError

def kruskal(graph):
    """An implementation of Kruskal's minimum spanning tree algorithm."""
    raise NotImplementedError

def a_star(graph, start_node):
    """An implementation of A* search algorithm."""
    raise NotImplementedError
