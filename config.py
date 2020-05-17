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

#  选择接触之后的影响力恢复方式，True为原数值 +1， False原数值重置为1
is_para_add_one = False

# 开始和结束时间
time_window = [1085440961, 1086000000]

# 选择参数

# 当选择指数衰减，到这里配置参数
alpha = 0.01
