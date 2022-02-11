import numpy as np
import sys
import pydot
from IPython.core.display import SVG

sys.setrecursionlimit(20000)

class Graph(object):
    def __init__(self, nodes: list['Node'], gtype = "digraph"):
        self.nodes = nodes
        self.gtype = gtype

    def show(self) -> 'SVG':
        graph = pydot.Dot("graphic", graph_type=self.gtype, bgcolor="white")

        for child in self.nodes:
            graph = child.get_graph(graph)

        return SVG(data=graph.create_svg())

    def get_by_tag(self, tag) -> 'Node':
        #print("searching %s" % tag)
        res = list(map(lambda x: x if x.tag == tag else None, self.nodes))
        #print(self.nodes)
        if len(res) > 0:
            return res[0]

        return None

    def to_tags(self):
        return self._to_tags(self.nodes)

    @classmethod
    def _to_tags(self, nodes: list['Node']) -> list:
        return list(map(lambda x: x.tag, nodes))

class Node():
    def __init__(self, tag: str):
        self.tag = tag
        self.nodes = []

    def get_graph(self, graph: 'pydot.Dot' = None) -> Graph:
        if graph is None:
            graph = pydot.Dot("graphic", graph_type="digraph", bgcolor="white")

        childs = self.__dict__().items()

        graph.add_node(pydot.Node(self.tag))

        for tag, childs in childs:
            graph.add_node(pydot.Node(tag))

            for c in childs:
                if len(graph.get_edge(tag, c)) > 0:
                    continue
                graph.add_edge(pydot.Edge(tag, c, color="black"))

        return graph

    def show(self) -> 'SVG':
        return SVG(data=self.get_graph().create_svg())

    def is_reachable(self, n: 'Node', already_tested = []) -> bool:
        res = False
        for child in self.nodes:
            already_tested.append(child)

            if n == child:
                res = True
                break
            res = child.is_reachable(n, already_tested)

        return res

    def deep_search(self: 'Node', visited: list['Node'] = [], dest: 'Node' = None) -> list['Node']:
        if self in visited or (dest != None and dest in visited):
            return visited

        visited.append(self)

        for n in self.nodes:
            visited = n.deep_search(visited, dest)

        return visited

    def __dict__(self):
        def to_child_tags(childs: list[Node]) -> list:
            return list(map(lambda x : x.tag, childs))

        node_dict = {self.tag: to_child_tags(self.nodes)}
        tmp_nodes = self.nodes

        def nodes_to_dict(tmp_nodes):
            for i, n in enumerate(tmp_nodes):
                if n.tag in node_dict:
                    del tmp_nodes[i]
                    continue
                node_dict[n.tag] = to_child_tags(n.nodes)
                nodes_to_dict(n.nodes)

        nodes_to_dict(tmp_nodes)

        return node_dict

# TODO create result with splitted graphs
def matrix_to_graph(matrix: np.array, labels: list[str] = []) -> Graph:

    if len(matrix) <= 0 and len(matrix[0]) <= 0:
        print("Empty matrix")

    res: list[Node] = []

    def label_from_row(irow: int) -> str:
        l = labels[irow] if irow < len(labels) else irow
        return str(l)

    for irow, _ in enumerate(matrix):
        res.append(Node(label_from_row(irow)))

    for irow, row in enumerate(matrix):
        n = res[irow]
        for icol, col in enumerate(row):
            if col >= 1:
                for _ in range(0, col):
                    res[icol].nodes.append(n)

    return Graph(res)

def dijkstra(src: Node, dest: Node) -> list['Node']:
    s, lambd, p = [[], [], []]
    print(s, lambd, p)
    print(src, dest)

