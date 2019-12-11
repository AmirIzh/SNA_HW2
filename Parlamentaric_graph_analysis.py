import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import collections
import copy

g = None


def preprocess_graph():
    global g
    small_weight_edges = [(u, v) for (u, v, d) in g.edges(data=True) if d['weight'] < 3]
    g.remove_edges_from(small_weight_edges)


def get_degree_dest():
    global g
    degree_dest = {}

    for node in g.nodes:
        degree = g.degree(node)
        if degree not in degree_dest:
            degree_dest[degree] = 1
        else:
            degree_dest[degree] += 1
    return degree_dest


def get_diameter():
    global g
    diameter = -1

    for node in g.nodes:
        cur_node_shortest_path = nx.shortest_path_length(g, node)
        for length in cur_node_shortest_path.values():
            if diameter < length:
                diameter = length
    return diameter


def get_aspl():
    global g
    shortest_paths = list()

    for node in g.nodes:
        cur_node_shortest_path = list(nx.shortest_path_length(g, node).values())
        shortest_paths += cur_node_shortest_path

    return sum(shortest_paths) / len(shortest_paths)


def print_properties():
    global g

    print("density = " + str(nx.density(g)))
    print("diameter = " + str(get_diameter()))
    print("Clustering Coefficient = " + str(nx.clustering(g)))
    print("average shortest path length = " + str(get_aspl()))
    print("Degree Distribution = " + str(get_degree_dest()))


def main():
    global g
    g = nx.read_gexf("C:\\Users\\amiri\\Desktop\\net_il2015-2018.gexf")
    preprocess_graph()
    print_properties()
    nx.draw(g)
    plt.show()


if __name__ == '__main__':
    main()