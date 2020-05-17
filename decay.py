from decay_function import decay_func
import numpy as np


def compute_decay(infos, datum, start, end):
    before_data = infos[0:start, 0:2]
    for data in datum:
        edge = data[0:2]
        print(np.where(before_data==edge))
        # print(edge in before_data)
        # print(edge)
        # print("*" * 30)
    return 1
