from file_loader import get_data
from config import decay_way, alpha
from network_models import ContinuousTimeNetwork
import matplotlib.pyplot as plt

# (41, 63)
# (663,343)


def main():
    infos = get_data()
    network = ContinuousTimeNetwork(infos, decay_way=decay_way)
    plt_data = []
    data_key = (41, 63)
    for i,j in network.run():
        if data_key in j.keys():
            plt_data.append(i[j[data_key]])
    plt.plot(plt_data[0:1000])
    plt.show()


if __name__ == '__main__':
    main()
