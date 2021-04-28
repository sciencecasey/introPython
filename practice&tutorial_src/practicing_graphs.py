"""
from lecture DS 2 in python course
"""
import networkx as nx

g = nx.Graph()

g.add_nodes_from(["BWI", "DFW", "PDX"])

g.add_edges_from([("BWI", "DFW", {"price":100, "time": 3.25}),
                  ("DFW", "PDX", {"price":100, "time": 1.75}),
                  ("BWI", "PDX", {"price":225, "time": 4})])

# compute shortest path
print(nx.dijkstra_path(g, "BWI", "PDX"))
print(nx.dijkstra_path(g, "BWI", "PDX", weight = "price"))
print(nx.dijkstra_path(g, "BWI", "PDX", weight = "time"))
