import numpy as np
import sys
import pydot
from IPython.core.display import SVG

sys.setrecursionlimit(20000)

class Node():
    def __init__(self, tag: str):
        self.tag = tag
        self.nodes = []

    def show(self):
        graph = pydot.Dot("graphic", graph_type="graph", bgcolor="white")

        for tag, childs in self.__dict__().items():
            graph.add_node(pydot.Node(tag))

            for c in childs:
                graph.add_edge(pydot.Edge(tag, c, color="black"))

        return SVG(data=graph.create_svg())

    def __dict__(self):
        def to_child_tags(childs: list[Node]):
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
def matrix_to_graph(matrix: np.array, labels: list[str] = []) -> Node:

    if len(matrix) <= 0 and len(matrix[0]) <= 0:
        print("Empty matrix")

    res: list[Node] = []

    def label_from_row(irow: int) -> str:
        l = irow if len(labels) < irow else labels[irow]
        return str(l)

    for irow, _ in enumerate(matrix):
        res.append(Node(label_from_row(irow)))

    for irow, row in enumerate(matrix):
        n = res[irow]
        for icol, col in enumerate(row):
            if col >= 1:
                for _ in range(0, col):
                    res[icol].nodes.append(n)

    return res[-1]
