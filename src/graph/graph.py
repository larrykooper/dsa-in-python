from src.linked_list.linked_list import LinkedList
from src.queue.queue import Queue
"""
 I will represent a graph as a collection of adjacency lists. Each adjacency list 
 is a linked list. The collection is called "edges."
 
 "nvertices" is the number of vertices in the graph
 "nedges" is the number of edges in the graph.

 This is an undirected graph.

 By my convention, vertices are numbered from 0 to (number of vertices minus 1)

"""

class Graph:

    MAXV = 100  # maximum number of vertices allowed

    def __init__(self):

        # Initialize the edges collection
        self.edges = []
        # Set edges to empty linked lists
        for i in range(self.MAXV):
            l = LinkedList()
            self.edges.append(l)
        self.nvertices = 0
        self.nedges = 0
        """
         the marked list [its indices match the adjacency list]
         contains which vertices have been visited
         Now, no vertices have been visited
        """
        self.marked = False * self.MAXV

    @classmethod
    def read_graph(cls, path):
        g = Graph()
        with open(path) as f:
            lines = f.readlines()
            v, e = lines[0].split(' ')
            g.nvertices = int(v)
            g.nedges = int(e)
            for i in range(1, g.nedges + 1):
                x, y = lines[i].split(' ')
                g.insert_edge(int(x), int(y))
        return g



    def insert_edge(self, v, w):
        self.edges[v].insert_at_beginning(w)
        self.edges[w].insert_at_beginning(v)
        self.nedges += 1

    def display_graph(self):
        for i in range(self.nvertices):
            adj_list = self.edges[i]
            print("{v_num} ->".format(v_num=i), end=" ")
            print(adj_list.display_recursive(" "))


    """
    Breadth-first search (BFS)
    s is the starting vertex for BFS
    which can be any vertex

    BFS outputs an ordered list (a Python list) of vertices it has visited

    Pseudocode for BFS:

    enqueue s
    do this until the queue is exhausted:
        dequeue
        visit the vertex that was dequeued
        enqueue all of that vertex's unvisited neighbors

    """
    def bfs(self, s):   # BFS is iterative, not recursive
        visited = []
        q = Queue()
        q.enqueue(s)
        while not q.is_empty():
            v = q.dequeue()
            self.marked[v] = True
            visited.append(v)
            # enqueue all vertex's unvisited neighbors
            neighbors = self.edges[v].traverse()   # calls traverse on linked list
            # print("neighbors: {}".format(neighbors))
            for vertex in neighbors:
                if not self.marked[vertex]:
                    q.enqueue(vertex)
        return visited

    """
    Pseudocode for DFS:

    visit s
        for each unvisited neighbor, nabe, of s:
            dfs(nabe)
    """

    def dfs(self, s):
        self.marked[s] = True
        visited = [s]
        neighbors = self.edges[s].traverse()
        for vertex in neighbors:
            if not self.marked[vertex]:
                visited = visited + self.dfs(vertex) # Recursive
        return visited



