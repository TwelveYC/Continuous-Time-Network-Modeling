from config import dataset_path
import numpy as np


#  数据有20296条
#  一共59835条
def get_data():
    data = np.empty((0,3), dtype=int)
    with open(dataset_path, 'r') as fp:
        while True:
            lines = fp.readline()
            if not lines:
                break
            lines_list = lines.split(" ")
            data = np.append(data, [[int(lines_list[0]), int(lines_list[1]), int(lines_list[2])]], axis=0)
    print(data.shape)
    return data
