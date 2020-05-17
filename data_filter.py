from config import time_window


def network_filter(infos):
    if time_window[0] >= time_window[1]:
        time_window[0], time_window[1] = time_window[1], time_window[0]

    infos_length = infos.shape[0]
    for index in range(infos_length):
        current_value = infos[index][-1]
        try:
            next_value = infos[index+1][-1]
        except IndexError:
            break
        if current_value <= time_window[0] <= next_value:
            start = index

        if current_value <= time_window[1] <= next_value:
            end = index
            break
    data = infos[start:end]
    return data, start, end
