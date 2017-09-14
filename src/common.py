#-*- encoding=utf-8 -*-
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
#通用绘图(频率分布直方图)操作

# 按照固定区间长度绘制频率分布直方图
# bins_interval 区间的长度
# margin        设定的左边和右边空留的大小
def probability_distribution(data, bins_interval=1, margin=1):
    bins = range(min(data), max(data), bins_interval)
    plt.xlim(min(data) - margin, max(data) + margin)
    plt.title("probability-distribution")
    plt.xlabel('Interval')
    plt.ylabel('Probability')
    plt.hist(x=data, bins=bins, histtype='bar', color=['r'])
    plt.show()


# 自己给定区间，小于区间左端点和大于区间右端点的统一做处理，对于数据分布不均很的情况处理较友好
# bins      自己设定的区间数值列表
# margin    设定的左边和右边空留的大小
# label     右上方显示的图例文字
"""e
    import numpy as np
    data = np.random.normal(0, 1, 1000)
    bins = np.arange(-5, 5, 0.1)
    probability_distribution_extend(data=data, bins=bins)
"""
def probability_distribution_extend(data, bins, margin=1, label='Distribution'):
    bins = sorted(bins)
    length = len(bins)
    intervals = np.zeros(length+1)
    for value in data:
        i = 0
        while  i < length and value >= bins[i]:
            i += 1
        intervals[i] += 1
    intervals = intervals / float(len(data))
    plt.xlim(min(bins) - margin, max(bins) + margin)
    bins.insert(0, -999)
    plt.title("probability-distribution")
    plt.xlabel('Interval')
    plt.ylabel('Probability')
    plt.bar(bins, intervals, color=['r'], label=label)
    plt.legend()
    plt.show()
