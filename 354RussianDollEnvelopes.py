<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
import numpy as np

from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        arr.sort(key=lambda x: (x[0], -x[1]))       #* 比较的值是一个元组，默认先比较第一维度，然后再比较第二维度。调用的是数据结构本身默认的比较函数

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])      # TODO 这是查找最比他小的节点?
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
import numpy as np

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # TODO python的排序和C语言的排序
        envelopes = np.array(envelopes)
        envelopes = envelopes[np.argsort(envelopes[:,0])]
        print(envelopes)
        for num in 

from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        arr.sort(key=lambda x: (x[0], -x[1]))       # TODO 读都都不栋...

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])      # TODO 这是查找最比他小的节点?
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
>>>>>>> hesy/master
        return lis([i[1] for i in arr])