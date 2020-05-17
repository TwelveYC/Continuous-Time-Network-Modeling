from decay_function import decay_func
import numpy as np


def compute_decay(infos, datum, start, end):
    #  datum是过滤出来的网络数据
    #  infos是原始数据
    before_datum = infos[0:start, :][::-1]
    time_delta = np.zeros((datum.shape[0], 1),dtype=float)
    index = 0
    length = datum.shape[0]
    for data in datum:
        edge = data[0:2]
        index += 1
        print(index/length)
        edge_time_stamp = data[2]
        for before_data in before_datum:
            link = before_data[0:2]
            link_time_stamp = before_data[2]
            if (edge == link).all():
                time_delta[index] = edge_time_stamp - link_time_stamp
                break
    delta = np.concatenate((datum, time_delta),axis=1)

    return decay_func(delta)
