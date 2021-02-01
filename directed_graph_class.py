
class DirectedGraph(object):

    def __init__(self, initial_graph_dict = None):
        if initial_graph_dict == None:
            initial_graph_dict = {}
        self.__initial_graph_dict = initial_graph_dict

    def vertices(self):
        return list(self.__initial_graph_dict.keys())

    def edges(self):
        edges = []
        for v in self.__initial_graph_dict:
            for i in self.__initial_graph_dict[v]:
                if (i, v)  in edges:
                    continue
                else:
                    edges.append((v, i))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.__initial_graph_dict:
            self.__initial_graph_dict[vertex] = []

    def add_edge(self, edge):
        (v, u) = tuple(edge)
        if (v,u) in self.edges():
            return None
        else:
            if v in self.__initial_graph_dict:
                self.__initial_graph_dict[v].append(u)
            else:
                self.__initial_graph_dict[v] = {u}

    def children(self, vertex):
        if vertex in list(self.__initial_graph_dict.keys()):
            return list(self.__initial_graph_dict[vertex])
        else:
            return None
