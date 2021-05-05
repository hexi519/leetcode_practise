# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

import ipdb
ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

做一版只缩小或者平移窗口,不扩大窗口的版本
https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/632436

# TODO 总结 连续子数组 O(n)相关的解法 可以往 前缀和 和 双指针 这边去靠


556 跟下一个permutation有点像