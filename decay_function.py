from config import decay_way, alpha
import numpy as np


def exponent_decay(delta):
    delta[:, 3] = np.exp(-alpha * delta[:, 3])
    temp = delta[:, 3]
    delta[:, 3] = np.where(temp == 1, 0, temp)
    return get_weight(delta)


def get_weight(delta):
    weight = {}
    index = 0
    for edge in delta:
        weight[(edge[0], edge[1])] = delta[index, 3]
        index += 1
    return weight


decay_function_dict = {
    "exponent": exponent_decay
}
decay_func = decay_function_dict.get(decay_way)
