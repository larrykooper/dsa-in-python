from src.linked_list.linked_list import LinkedList
from src.queue.queue import Queue
"""
 I will represent a graph as a collection of adjacency lists
 which is very similar to how I represented a hash table.

Each adjacency list is a linked list.

 This is an undirected graph.

 By my convention, vertices are numbered from 0 to (number of vertices minus 1)

Vertex constructor  - I took it out, put back if need it
Graph constructor   done
add_Edge      done
display_Graph   done
   writes out graph as
   v ->  v1 v2 v3
unmarkGraph  (marks all vertices as unvisited)
dfs
bfs

"""

class Graph:

    def __init__(self, number_of_vertices):
        self.vertices = number_of_vertices
        self.adj = [None] * self.vertices   # adj array is [None, None,..]
        for i, adj_list in enumerate(self.adj):
            l = LinkedList()
            self.adj[i] = l
        self.edges = 0
        """
         the marked list [its indices match the adj list]
         contains which vertices have been visited
         Now, no vertices have been visited
        """
        self.marked = [False] * self.vertices

    def add_edge(self, v, w):
        self.adj[v].insert_at_beginning(w)
        self.adj[w].insert_at_beginning(v)
        self.edges += 1

    def display_graph(self):
        for i, adj_list in enumerate(self.adj):
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
    def bfs(self, s):
        visited = []
        q = Queue()
        q.enqueue(s)
        while not q.is_empty():
            v = q.dequeue()
            self.marked[v] = True
            visited.append(v)
            # enqueue all vertex's unvisited neighbors
            neighbors = self.adj[v].traverse()
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
        neighbors = self.adj[s].traverse()
        for vertex in neighbors:
            if not self.marked[vertex]:
                visited = visited + self.dfs(vertex)
        return visited



