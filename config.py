# CollegeMsg 数据，最早4.15，最晚10.26
# 1098 777142 2004年10月26日15时52分22秒0毫秒
# 1082040961 2004年4月15日22时56分1秒0毫秒
# 选择数据集
data_order = 0
DataSets = ["dataset/CollegeMsg.txt"]
dataset = DataSets[data_order]

#  选择衰减方式
decay_order = 0
decay_ways = ["exponent"]
decay_way = decay_ways[decay_order]

is_all_calculation = True

# 开始和结束时间
time_window = [1085980961, 1086000000]

# 选择参数

# 当选择指数衰减，到这里配置参数
alpha = 0.00000000001
