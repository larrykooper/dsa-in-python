from src.graph.graph import Graph

class TestGraph:

    def test_bfs(self):
        g =  Graph(7)  # 7 vertices

        g.add_edge(3,1)
        g.add_edge(1,0)
        g.add_edge(1,2)
        g.add_edge(3,5)
        g.add_edge(5,4)
        g.add_edge(5,6)
        g.display_graph()

        visited = g.bfs(3)  # I want to start at vertex 3
        # We use set in the assertion because order can differ
        assert set(visited) == set([3, 1, 5, 0, 2, 4, 6])


    def test_dfs(self):
        g = Graph(5)

        g.add_edge(0,4)
        g.add_edge(0,1)
        g.add_edge(0,3)
        g.add_edge(0,2)
        g.add_edge(4,3)
        g.add_edge(3,1)
        g.add_edge(1,2)

        visited = g.dfs(0)
        assert set(visited) == set([0, 4, 3, 1, 2])

