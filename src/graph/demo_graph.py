from graph import Graph
from src.utils import get_project_root

root = get_project_root()
g = Graph.read_graph(root / 'src' / 'graph' / 'graphinput.txt')
g.display_graph()






