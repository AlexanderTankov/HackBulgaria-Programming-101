import unittest

from who_follows_you_back import DirectedGraph


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.test_graph = DirectedGraph()

    def test_graph_init(self):
        self.assertEqual(self.test_graph.graph, {})

    def test_addEdge(self):
        self.test_graph.addEdge("A", "B")
        self.assertIn("A", self.test_graph.graph)
        self.assertIn("B", self.test_graph.graph["A"])
        self.test_graph.addEdge("A", "D")
        self.assertIn("A", self.test_graph.graph)
        self.assertIn("D", self.test_graph.graph["A"])
        self.test_graph.addEdge("B", "C")
        self.assertIn("A", self.test_graph.graph)
        self.assertIn("B", self.test_graph.graph["A"])
        self.assertIn("B", self.test_graph.graph)
        self.assertIn("C", self.test_graph.graph["B"])

    def test_get_neighbors(self):
        self.test_graph.addEdge("A", "B")
        self.test_graph.addEdge("A", "D")
        self.assertEqual(["B", "D"], self.test_graph.getNeighborsFor("A"))

    def test_path_between(self):
        self.test_graph.addEdge("A", "B")
        self.test_graph.addEdge("B", "C")
        self.assertTrue(self.test_graph.pathBetween("A", "C"))
        self.assertFalse(self.test_graph.pathBetween("A", "E"))

    def test_toString(self):
        self.test_graph.addEdge("A", "B")
        self.assertEqual(self.test_graph.toString(), "A --> ['B']")

if __name__ == '__main__':
    unittest.main()
