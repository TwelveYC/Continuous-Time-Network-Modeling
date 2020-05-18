from file_loader import get_data
from data_filter import network_filter
from decay import compute_decay
import networkx as nx
from config import is_all_calculation, alpha
import matplotlib.pyplot as plt
import numpy as np


def main():
    infos = get_data()
    if not is_all_calculation:
        data, start, end = network_filter(infos)
        weight = compute_decay(infos, data, start, end)
        G = nx.Graph()
        G.add_edges_from(data[:, 0:2])
        nx.set_edge_attributes(G, weight, "strength")
    else:
        #  数据有20296条
        #  一共59835条
        links_index = dict()
        links = np.empty((0, 3), dtype=int)
        links_num = 0
        link_strength = np.empty((0,1))
        plot_data = []
        for info in infos:
            edge = info[0: 2].copy()
            link = tuple(edge)
            current_time_stamp = info[2]
            link_strength = link_strength * np.exp(-alpha * (current_time_stamp - links[:, 2]))

            if link in links_index.keys():
                link_index = links_index[link]
                current_time_stamp = info[2]
                current_link_strength = link_strength[link_index]
                link_strength[link_index] = current_link_strength + 1
                links[link_index, 2] = current_time_stamp

            else:
                links_index[link] = links_num
                links_num += 1
                links = np.append(links, [info], axis=0)
                link_strength = np.append(link_strength, [1])

            if (44, 84) in links_index.keys():
                plot_data.append(link_strength[links_index[(44,84)]])
            else:
                plot_data.append(0)

        plt.plot(plot_data)
        plt.show()



if __name__ == '__main__':
    main()
