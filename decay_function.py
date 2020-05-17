from config import decay_way


def exponent_decay(G, delta):
    pass


decay_dict = {
    "exponent": exponent_decay
}
decay_func = decay_dict.get(decay_way)



