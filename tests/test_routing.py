import unittest
from routing import *
import numpy as np
inf = float('Inf')
nan = float('NaN')

class TestVertex(unittest.TestCase):
    def test___init__(self):
        v = Vertex()
        self.assertTrue(np.isinf(v.dist))
        self.assertTrue(np.isnan(v.prev))

    def test_init_dist(self):
        v = Vertex(dist=5)
        u = Vertex(dist=10)
        self.assertEqual(v.dist,5)
        self.assertEqual(u.dist,10)

    def test_init_prev(self):
        v = Vertex()
        u = Vertex(prev=v)
        self.assertEqual(u.prev,v)


class TestGraph(unittest.TestCase):
    def test___init__(self):
        graph = Graph()
        self.assertEqual(graph.vertices,[])

    def test_append(self):
        graph = Graph()
        v = Vertex()
        graph.append(v)
        self.assertEqual(graph.vertices, [v])
        u = Vertex()
        graph.append(u)
        self.assertEqual(graph.vertices, [v,u])

    def test_extend(self):
        graph = Graph()
        v,u = Vertex(),Vertex()
        graph.extend([v,u])
        self.assertEqual(graph.vertices,[v,u])

    def test_remove(self):
        graph = Graph()
        v,u = Vertex(),Vertex()
        graph.extend([v,u])
        self.assertEqual(graph.vertices, [v,u])
        graph.remove(v)
        self.assertEqual(graph.vertices, [u])
        graph.remove(u)
        self.assertEqual(graph.vertices, [])

    def test___len__(self):
        graph = Graph()
        v,u = Vertex(),Vertex()
        graph.extend([v,u])
        self.assertEqual(len(graph),2)

    def test_iterate_graph(self):
        graph = Graph()
        v_list = []
        a,b,c = Vertex(),Vertex(),Vertex()
        graph.extend([a,b,c])

        for v in graph:
            self.assertIsInstance(v,Vertex)
            v_list.append(v)
        self.assertEqual(v_list,[a,b,c])

        for v in graph:
            self.assertIsInstance(v,Vertex)
            v_list.append(v)
        self.assertEqual(v_list,[a,b,c])

    def test_vertex_with_min_dist(self):
        graph = Graph()
        a = Vertex(dist=5)
        b = Vertex(dist=4)
        c = Vertex(dist=3)
        d = Vertex(dist=6)
        graph.extend([a,b,c,d])
        self.assertEqual(graph.vertex_with_min_dist(),c)

    def test_vertex_with_min_dist_inf(self):
        graph = Graph()
        a = Vertex()
        b = Vertex()
        c = Vertex()
        d = Vertex()
        graph.extend([a,b,c,d])
        self.assertEqual(graph.vertex_with_min_dist(),a)

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        # self.assertEqual(expected, Dijkstra(graph, source))
        assert True # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
