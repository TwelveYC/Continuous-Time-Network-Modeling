from file_loader import get_data
from data_filter import network_filter
from decay import compute_decay
import networkx as nx
import matplotlib.pyplot as plt


def main():
    infos = get_data()
    data, start, end = network_filter(infos)
    weight = compute_decay(infos, data, start, end)
    G = nx.Graph()
    G.add_edges_from(data[:, 0:2])
    nx.set_edge_attributes(G, weight, "strength")


if __name__ == '__main__':
    main()
