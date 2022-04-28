from src.linked_list.linked_list import LinkedList
from src.queue.queue import Queue
from typing import List
"""
 I will represent a graph as a collection of adjacency lists. Each adjacency list 
 is a linked list. The collection is called "edges."
 
 "nvertices" is the number of vertices in the graph
 "nedges" is the number of edges in the graph.

 For this code module I'm assuming all the graphs are undirected. 

 By my convention, vertices are numbered from 0 to (number of vertices minus 1)

"""

"""
It's important to know basic graph algorithms like BFS and DFS, but the main challenge is to 
correctly model your problem as a graph. 
p. 146

"""

# 5.2 Data Structures for Graphs

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
        print("Displaying graph:")
        for i in range(self.nvertices):
            adj_list = self.edges[i]
            print("{v_num} ->".format(v_num=i), end=" ")
            print(adj_list.display_recursive(" "))
        print("  ")


# 5.6 Breadth-First Search

    """
    Breadth-first search (BFS)
    s is the starting vertex for BFS
    which can be any vertex

    BFS outputs an ordered list (a Python list) of vertices it has visited
    """

    def bfs(self, s):
        discovered = [False] * self.nvertices
        processed = [False] * self.nvertices
        parent = [None] * self.nvertices
        discovered[s] = True
        q = Queue()
        q.enqueue(s)
        while not q.is_empty():
            v = q.dequeue()
            self.process_vertex_early(v)
            processed[v] = True
            neighbors = self.edges[v].traverse()
            for y in neighbors:
                # so we only process each edge once
                if not processed[y]:
                    self.process_edge_bfs(v, y)
                if not discovered[y]:
                    q.enqueue(y)
                    discovered[y] = True
                    parent[y] = v
            self.process_vertex_late(v)
        return parent

    def process_vertex_late(self, v):
        print(f"processed vertex late {v}")

    def process_vertex_early(self, v):
        print(f"processed vertex early {v}")

    def process_edge_bfs(self, x, y):
        print(f"processed edge {x}, {y}")


    def find_path(self, start, end, parents: List[int]):
        if (start == end) or (end is None):
            print(f"{start}")
        else:
            self.find_path(start, parents[end], parents)
            print(f"{end}")

# 5.7 Applications of BFS

    # not implemented
    # Compare Skiena p. 167
    def connected_components(self):

        """
        Testing whether Rubik's cube or 15 puzzle can be solved with a graph. each vertex is a legal
         configuration connected to the last vertex by however you transform it

         # not implemented
            # Compare Skiena p. 168
        """
        pass



    def twocolor(self):
        pass


# 5.8 Depth-First Search



    def dfs(
            self,
            v,
            discovered,
            processed,
            entry_time,
            exit_time,
            parent,
            time):
        """


P. 169 take home lesson

Breadth-first and depth-first searches provide mechanisms to visit each edge and vertex of the graph.
 They prove the basis of most simple, efficient graph algorithms.

For some problems you can use either BFS or DFS, but for some the difference is crucial.



           Alternative to passing all the arrays is make the arrays members of the graph object
           """
        discovered[v] = True
        time += 1
        entry_time[v] = time
        # before we've traversed any outgoing edges from v
        self.process_vertex_early(v)
        neighbors = self.edges[v].traverse()
        for y in neighbors:
            if not discovered[y]:
                parent[y] = v
                self.process_edge_cycle_detection(v, y, discovered, parent)
                self.dfs(y, discovered, processed, entry_time, exit_time, parent, time)
            elif (not processed[y] and parent[v] != y):
                self.process_edge_cycle_detection(v, y, discovered, parent)
        # We have finished processing all outgoing edges from v
        self.process_vertex_late(v)
        time += 1
        exit_time[v] = time
        processed[v] = True

    """
    p. 172 take-home lesson
    DFS organizes vertices by entry/exit times, and edges into tree and back edges. 
    This organizaiton is what gives DFS its real power. 
    """

    def process_edge_cycle_detection(self, x, y, discovered, parent):
        print(f"processing edge {x}, {y}")
        if discovered[y] and (parent[x] != y):
            # found back edge
            print(f"Cycle from {y} to {x}")
            self.find_path(y, x, parent)
            print("\n")
            finished = True
        return

    # Finding articulation vertices - not implemented

    # DFS on directed graphs - in other code file

    # Strongly connected components

