from linked_list import LinkedList
"""
 I will represent a graph as a collection of adjacency lists
 which is very similar to how I represented a hash table.

Each adjacency list is a linked list

 This is an UNDIRECTED graph

 Vertices are numbered from 0 to (number of vertices minus 1)

Vertex constructor  done
Graph constructor   done
addEdge  done
showGraph   done
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






