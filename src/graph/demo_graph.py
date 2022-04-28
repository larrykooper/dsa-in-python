from graph import Graph
from src.utils import get_project_root

root = get_project_root()

print("graphinput.txt")

g = Graph.read_graph(root / 'src' / 'graph' / 'graphinput.txt')
g.display_graph()

print("graphp162.txt")

h = Graph.read_graph(root / 'src' / 'graph' / 'graphp162.txt')
h.display_graph()
print("Doing BFS and finding parents")
parents = h.bfs(1)
print("Listing parents")
for i, parent in enumerate(parents):
    print(f"{i}: {parent}")

print("Finding path from 0 to 4")
h.find_path(0, 4, parents)

print("Doing dfs and detecting cycles")

h.dfs(1,
      [False] * h.nvertices,
      [False] * h.nvertices,
      [0] * h.nvertices,
      [0] * h.nvertices,
      [None] * h.nvertices,
      0)









