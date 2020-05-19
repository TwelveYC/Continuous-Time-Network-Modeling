# CollegeMsg 数据，最早4.15，最晚10.26
# 1098 777142 2004年10月26日15时52分22秒0毫秒
# 1082040961 2004年4月15日22时56分1秒0毫秒
# 选择数据集
data_order = 0
DataSets = ["dataset/CollegeMsg.txt", "dataset/email-Eu-core-temporal.txt"]
dataset_path = DataSets[data_order]

#  选择衰减方式
decay_order = 0
decay_ways = ["exponent", "exponent_cutoff", "constant"]
decay_way = decay_ways[decay_order]

# 开始和结束时间


# 当选择指数衰减，到这里配置参数
alpha = 0.000000001

# 当选择指数截至衰减方式，到这里配置参数
cutoff_time = 600

# 当选择常数，到这里配置参数
const_decay_parameter = 0.99999

