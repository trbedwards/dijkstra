inf = float('Inf')
nan = float('NaN')


class Graph(object):
    """
    A graph class. A graph consists of a collection of vertices connected by edges with associated weights
    """
    def __init__(self):
        self.vertices = []
        self.counter = 0

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.vertices)

    def next(self):
        self.counter = self.counter + 1
        if self.counter > len(self):
            raise StopIteration
        return self.vertices[self.counter-1]

    def append(self,v):
        self.vertices.append(v)

    def extend(self,v_list):
        for v in v_list:
            self.vertices.append(v)

    def remove(self,v):
        self.vertices.remove(v)

    # def vertices(self):
    #     return self

    def vertex_with_min_dist(self):
        vertex = self.vertices[0]
        min_dist = vertex.dist
        for v in self:
            dst = v.dist
            if dst < min_dist:
                min_dist = dst
                vertex = v
        return vertex


class Vertex(object):
    """
    A vertex.
    """
    def __init__(self, dist=inf, prev=nan):
        self.dist = dist
        self.prev = prev

    def neighbours(self):
        return []

def Dijkstra(graph=Graph(), source=Vertex()):
    Q = Graph()

    source.dist = 0  # distance from source to source
    source.prev = nan  # previous node in optimal path initialisation

    # initialisation
    for v in graph:
        if v != source:  # where v has not yet been removed from Q (unvisited nodes)
            v.dist = inf  # unknown distance from source to v
            v.prev = nan  # previous node in optimal path from source
        Q.append(v)  # all nodes initially in Q (unvisited nodes)

    while Q.vertices:
        u = Q.vertex_with_min_dist()
        Q.remove(u)

        for v in u.neighbours():
            pass  # TODO: u.neighbours

    return None,None

if __name__ == "__main__":
    G = Graph()

    a = Vertex()
    b = Vertex()
    c = Vertex()

    G.extend([a,b,c])

    G = Graph([(a,b,1),(b,c,1),(a,c,3)])

    print Dijkstra(G, a)


