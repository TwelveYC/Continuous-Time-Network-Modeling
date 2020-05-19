import numpy as np
from config import alpha, cutoff_time, const_decay_parameter


class ContinuousTimeNetwork:
    def __init__(self, infos, **kwargs):
        decay_function_dict = {
            "exponent": self.exponent_decay,
            "exponent_cutoff": self.exponent_cutoff_decay,
            "constant": self.constant_decay
        }
        self.infos = infos
        #  输入的数据，分别是起始点，终止点和时间戳
        self.links = np.empty((0, 3), dtype=int)
        #  用来存放最新边的，它会存储最新的所有边，最后会剔除重复，时间戳是最新的
        self.links_index = dict()
        #  索引数组，边索引在links当中的位置
        self.links_num = 0
        #  用作计数
        self.link_strength = np.empty((0, 1))
        #  存储对应边当前的强度，位置由links_index数组决定
        self.current_time_stamp = 0
        #  当前时间戳
        self.alpha = alpha
        #  衰减系数
        self.decay_func = decay_function_dict.get(kwargs.get("decay_way"))

    def run(self):
        for info in self.infos:
            edge = info[0:2].copy()
            link = tuple(edge)
            self.current_time_stamp = info[2]
            delta = self.current_time_stamp - self.links[:, 2]
            if link in self.links_index.keys():
                link_index = self.links_index[link]
                current_link_strength = self.link_strength[link_index]
                self.decay_func(delta)
                # self.link_strength[link_index] = current_link_strength + 1
                self.link_strength[link_index] = 1
                self.links[link_index, 2] = self.current_time_stamp
            else:
                self.decay_func(delta)
                self.links_index[link] = self.links_num
                self.links_num += 1
                self.links = np.append(self.links, [info], axis=0)
                self.link_strength = np.append(self.link_strength, [1])

            # yield self.current_time_stamp
            # yield self.link_strength, self.current_time_stamp, self.links, self.links_index
            yield self.link_strength, self.links_index

    def exponent_decay(self, delta):
        self.link_strength = self.link_strength * np.exp(-self.alpha * delta)

    def exponent_cutoff_decay(self, delta):
        self.link_strength = self.link_strength * np.where(delta < cutoff_time, 1,
                                                           np.exp(-self.alpha * (delta - cutoff_time)))

    def constant_decay(self, delta):
        self.link_strength = self.link_strength * np.power(const_decay_parameter, delta)