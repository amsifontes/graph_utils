class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        pass

    def add_edge(self, node1, node2):
        pass

    def remove_node(self, node):
        pass

    def remove_edge(self, node1, node2):
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node):
        pass

    def remove_edge(self, node):
        pass

class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

def bfs(graph, start_node):
    pass

def dfs(graph, start_node):
    pass

def dijkstra(graph, start_node):
    pass

def bellman_ford(graph, start_node):
    pass

def prim(graph):
    pass

def kruskal(graph):
    pass

