import numpy as np
import sys
import pydot
from IPython.core.display import SVG

sys.setrecursionlimit(20000)

class Graph(object):
    def __init__(self, nodes: list["Node"], gtype="digraph"):
        self.nodes = nodes
        self.gtype = gtype

    def show(self) -> "SVG":
        graph = pydot.Dot("graphic", graph_type=self.gtype, bgcolor="white")

        for child in self.nodes:
            graph = child.get_graph(graph)

        return SVG(data=graph.create_svg())

    def get_by_tag(self, tag) -> "Node":
        res = list(filter(lambda x: x.tag == tag, self.nodes))

        if len(res) > 0:
            return res[0]

        return None

    def to_tags(self):
        return self._to_tags(self.nodes)

    @classmethod
    def _to_tags(self, nodes: list["Node"]) -> list:
        return list(map(lambda x: x.tag, nodes))

class Node:
    def __init__(self, tag: str):
        self.tag: str = tag
        self.weight = 0
        self.nodes: list["Node"] = []

    def get_graph(self, graph: "pydot.Dot" = None, visited: list['Node'] = []) -> Graph:
        if graph is None:
            graph = pydot.Dot("graphic", graph_type="digraph", bgcolor="white")

        graph.add_node(pydot.Node(self.tag))

        for child in self.nodes:
            visited_id = "%s-%s" % (self.tag, child.tag)

            if visited_id in visited:
                continue

            graph.add_node(pydot.Node(child.tag))
            visited.append(visited_id)

            if len(graph.get_edge(self.tag, child.tag)) > 0:
                continue

            graph.add_edge(pydot.Edge(self.tag, child.tag, color="black"))

            child.get_graph(graph, visited)

        return graph

    def dijkstra(self: 'Node', dest: 'Node') -> list["Node"]:
        s, lambd, p = [[], [], []]
        print(s, lambd, p)
        print(self, dest)

        return []

    def show(self) -> "SVG":
        return SVG(data=self.get_graph().create_svg())

    def is_reachable(self, n: "Node", already_tested=[]):
        res = False
        for child in self.nodes:
            already_tested.append(child)

            if n == child:
                res = True
                break
            res, already_tested = child.is_reachable(n, already_tested)

        return (res, already_tested)

    def deep_search(
        self: "Node", visited: list["Node"] = [], dest: "Node" = None, graph: Graph = None
    ) -> list["Node"]:

        if dest in visited or (graph != None and len(visited) >= len(graph.nodes)):
            return visited

        visited.append(self)

        for n in self.nodes:
            visited = n.deep_search(visited, dest, graph)

        return visited

    def debug_nodes(self):
        print(list(map(lambda x: x.tag, self.nodes)))

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
                    n.weight = col
                    res[icol].nodes.append(n)

    return Graph(res)
