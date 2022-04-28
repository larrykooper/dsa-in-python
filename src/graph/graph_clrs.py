"""
   Pseudocode for BFS:

   enqueue s
   do this until the queue is exhausted:
       dequeue
       visit the vertex that was dequeued
       enqueue all of that vertex's unvisited neighbors

   """


def bfs_clrs(self, s):  # BFS is iterative, not recursive
    """
    Compare CLRS page 595
    :param s:
    :return:
    """
    visited = []
    q = Queue()
    q.enqueue(s)
    while not q.is_empty():
        v = q.dequeue()
        self.marked[v] = True
        visited.append(v)
        # enqueue all vertex's unvisited neighbors
        # traverse returns a list of all linked list members from beginning to end
        neighbors = self.edges[v].traverse()
        for vertex in neighbors:
            if not self.marked[vertex]:
                q.enqueue(vertex)  # we mark it when we dequeue it
    return visited


"""
Pseudocode for DFS:

visit s
    for each unvisited neighbor, nabe, of s:
        dfs(nabe)
"""


def dfs_clrs(self, s):
    self.marked[s] = True
    visited = [s]
    neighbors = self.edges[s].traverse()
    for vertex in neighbors:
        if not self.marked[vertex]:
            visited = visited + self.dfs(vertex)  # Recursive
    return visited



