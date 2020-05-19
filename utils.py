time_window = [1085980961, 1086000000]


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


def get_weight(delta):
    weight = {}
    index = 0
    for edge in delta:
        weight[(edge[0], edge[1])] = delta[index, 3]
        index += 1
    return weight
