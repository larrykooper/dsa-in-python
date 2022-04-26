from graph import Graph

class DemoGraphOld:

    def demo_graph_1(self):
        g = Graph(5)

        # Add edge, by implication, adds vertices
        g.insert_edge(0,3)
        g.insert_edge(0,1)
        g.insert_edge(1,2)
        g.insert_edge(3,4)
        g.display_graph()


dg = DemoGraphOld()
dg.demo_graph_1()
