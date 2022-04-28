from graph import Graph
from src.utils import get_project_root

root = get_project_root()
print("graph_cycle.txt")

g = Graph.read_graph(root / 'src' / 'graph' / 'graph_cycle.txt')

g.display_graph()

print("Doing dfs and detecting cycles")

g.dfs(1,
      [False] * g.nvertices,
      [False] * g.nvertices,
      [0] * g.nvertices,
      [0] * g.nvertices,
      [None] * g.nvertices,
      0)