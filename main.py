from file_loader import get_data
from data_filter import network_filter
from decay import compute_decay
import networkx as nx
import matplotlib.pyplot as plt


def main():
    infos = get_data()
    data, start, end = network_filter(infos)
    G = compute_decay(infos, data, start, end)
    # G = nx.Graph()
    # G.add_edges_from(data[:, 0:2])
    # edges = G.edges
    # time_stamp = data[:, 2]
    # time_stamp_dict = {}
    # index = 0
    # for edge in edges:
    #     time_stamp_dict[edge] = time_stamp[index]
    #     index += 1
    # nx.set_edge_attributes(G, time_stamp_dict, "time_stamp")
    # H = compute_decay(G, infos)
    print(G)
    # print(G.number_of_nodes())
    # print(G.number_of_edges())
    print(start/infos.shape[0])
    print(end/infos.shape[0])


if __name__ == '__main__':
    main()
