""" Mobject used to represent a multigraph """

__all__ = [
        "MultiGraph",
]

from typing import Hashable, List, Tuple

import networkx as nx

from manim import Graph

class MultiGraph(Graph):

    def __init__(
            self,
            nodes: List[Hashable],
            edges: List[Tuple[Hashable, Hashable]]
    ) -> None:
        super().__init__(self, nodes, edges, edge_type=BezierCurve??)

        nx_multigraph = nx.MultiGraph()
        nx_multigraph.add_nodes_from(nodes)
        nx_multigraph.add_edges_from(edges)
        self._multigraph = nx_multigraph

        self._layout = _determine_graph_layout(
                nx.layout.spring_layout(self._multigraph)
        )
