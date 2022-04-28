from src.linked_list.linked_list import LinkedList
from src.stack.stack import Stack
from src.queue.queue import Queue
from typing import List


class DirectedGraph:

    MAXV = 100  # maximum number of vertices allowed

    def __init__(self, directed: bool):

        # Initialize the edges collection
        self.edges = []
        # Set edges to empty linked lists
        for i in range(self.MAXV):
            l = LinkedList()
            self.edges.append(l)
        self.nvertices = 0
        self.nedges = 0
        self.directed = directed
        self.stack = Stack()





    @classmethod
    def read_graph(cls, path, directed):
        g = DirectedGraph(directed)
        with open(path) as f:
            lines = f.readlines()
            v, e = lines[0].split(' ')
            g.nvertices = int(v)
            g.nedges = int(e)
            for i in range(1, g.nedges + 1):
                x, y = lines[i].split(' ')
                g.insert_edge(int(x), int(y))
        # metadata
        g.discovered = [False] * g.nvertices
        g.processed = [False] * g.nvertices
        g.entry_time = [0] * g.nvertices
        g.exit_time = [0] * g.nvertices
        g.parent = [None] * g.nvertices
        g.time = 0
        return g



    def insert_edge(self, v, w):
        self.edges[v].insert_at_beginning(w)
        if not self.directed:
            self.edges[w].insert_at_beginning(v)
        self.nedges += 1

    def display_graph(self):
        print("Displaying graph:")
        for i in range(self.nvertices):
            adj_list = self.edges[i]
            print("{v_num} ->".format(v_num=i), end=" ")
            print(adj_list.display_recursive(" "))
        print("  ")

    def dfs(self, v):
        self.discovered[v] = True
        self.time += 1
        self.entry_time[v] = self.time
        # before we've traversed any outgoing edges from v
        self.process_vertex_early(v)
        neighbors = self.edges[v].traverse()
        for y in neighbors:
            if not self.discovered[y]:
                self.parent[y] = v
                self.process_edge(v, y)
                self.dfs(y)
            elif (not self.processed[y] and self.parent[v] != y) or self.directed:
                self.process_edge(v, y)
        # We have finished processing all outgoing edges from v
        self.process_vertex_late(v)
        self.time += 1
        self.exit_time[v] = self.time
        self.processed[v] = True

    def edge_classification(self, x, y):
        if self.parent[y] == x:
            return "TREE"
        if self.discovered[y] and not self.processed[y]:
            return "BACK"
        if self.processed[y] and (self.entry_time[y] > self.entry_time[x]):
            return "FORWARD"
        if self.processed[y] and (self.entry_time[y] < self.entry_time[x]):
            return "CROSS"
        print(f"warning -- unclassified edge {x}, {y} ")


    def process_vertex_late(self, v):
        print(f"processed vertex late {v}")
        self.stack.push(v)



    def process_vertex_early(self, v):
        print(f"processed vertex early {v}")

    def process_edge(self, x, y):
        print(f"processed edge {x}, {y}")
        klass = self.edge_classification(x, y)
        if (klass == "BACK"):
            print("Directed cycle found, not a DAG")

    def topsort(self):
        for v in range(self.nvertices):
            if not self.discovered[v]:
                self.dfs(v)
        self.stack.display_stack()


