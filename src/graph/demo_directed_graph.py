from directed_graph import DirectedGraph
from src.utils import get_project_root

root = get_project_root()


print("graphinput.txt")

g = DirectedGraph.read_graph(root / 'src' / 'graph' / 'directed_graph.txt', True)
g.display_graph()


print("Doing dfs")

g.dfs(6)

print("doing topological sort")

g.topsort()


