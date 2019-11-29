from graph import Graph

class DemoGraph:

    def demo_graph_1(self):
        g = Graph(5)

        g.add_edge(0,3)
        g.add_edge(0,1)
        g.add_edge(1,2)
        g.add_edge(3,4)
        g.display_graph()


dg = DemoGraph()
dg.demo_graph_1()
