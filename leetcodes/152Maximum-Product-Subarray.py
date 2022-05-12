# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution(object):
    def maxProduct(self, nums):
        """
        >>> s = Solution()
        >>> s.maxProduct([2,3,-2,4])
        6
        >>> s.maxProduct([-2,0,-1])
        0
        >>> s.maxProduct([-2])
        -2
        >>> s.maxProduct([-2,-3,7])
        42
        """
        min_, max_ = nums[0], nums[0]
        res = max_
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            else:
                if nums[idx] < 0:
                    min_, max_ = max_, min_
                min_, max_ = min(num, num*min_), max(num, num*max_)

                res = max(res, max_)
        return res

    ## 大佬秀法
    """
    假设数组中无零，负数只有奇数个或者偶数个。偶数个就是全乘起来，奇数个就是剔除第一个奇数，累乘所有后面奇数（前向累乘），或者剔除最后一个奇数，累乘所有前面的奇数（后向累乘）
    那么如果数组中有0，那么只要重置为1即可。
    ....算了，不记这个了。。太秀了
    """
    class Solution(object):
        def maxProduct(self, A):
            B = A[::-1]
            for i in range(1, len(A)):
                A[i] *= A[i - 1] or 1   # 遇到0的话，置为1，方便后续累乘用
                B[i] *= B[i - 1] or 1
            return max(A + B)   # list的加号指的是concate，别搞错了
