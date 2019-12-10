import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import collections

g = None


def preprocess_graph():
    global g
    small_weight_edges = [(u, v) for (u, v, d) in g.edges(data=True) if d['weight'] < 3]
    g.remove_edges_from(small_weight_edges)

""""
def show_deg_dest():
    global g

    degree_sequence = sorted([d for n, d in g.degree()], reverse=True)  # degree sequence
    # print "Degree sequence", degree_sequence
    degree_count = len(degree_sequence)
    deg, cnt = zip(*degree_count.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

    # draw graph in inset
    plt.axes([0.4, 0.4, 0.5, 0.5])
    Gcc = g.subgraph(sorted(nx.connected_components(g), key=len, reverse=True)[0])
    pos = nx.spring_layout(g)
    plt.axis('off')
    nx.draw_networkx_nodes(g, pos, node_size=20)
    nx.draw_networkx_edges(g, pos, alpha=0.4)

    plt.show()
"""


def check_properties():
    global g
    den = nx.density(g)             # int
    dia = nx.diameter(g)            # int
    clus = nx.clustering(g)


def main():
    global g
    g = nx.read_gexf("C:\\Users\\amiri\\Desktop\\net_il2015-2018.gexf")
    preprocess_graph()
    # show_deg_dest()
    # nx.draw(g)
    # plt.show()


if __name__ == '__main__':
    main()