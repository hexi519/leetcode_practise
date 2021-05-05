# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    def nextPermutation(self, nums):
        """
        >>> s = Solution()
        >>> s.nextPermutation([3,2,1])
        [1, 2, 3]
        >>> s.nextPermutation([1,2,3])
        [1, 3, 2]
        >>> s.nextPermutation([1,1,5])
        [1, 5, 1]
        >>> s.nextPermutation([5,1,1])
        [1, 1, 5]
        >>> s.nextPermutation([1])
        [1]
        """
        cur = len(nums)-1
        if cur == 0:
            return nums
        while cur:
            # log.info(f"cur is {cur}({nums[cur]})")
            if nums[cur] > nums[cur-1]: # 等于的话 也算一个
                # bisect_left如何处理逆序 还真是不记得了....
                idx = cur
                while idx < len(nums):
                    if nums[idx] < nums[cur-1]:
                        break
                    idx+=1
                # log.info(f"\tidx-1 is {idx-1}({nums[idx-1]})")
                nums[cur-1], nums[idx-1] = nums[idx-1], nums[cur-1]
                # log.info(f"\tcur after replace is {nums}")

                break
            cur-=1

        # log.info(f"\tcur, nums[:cur],nums[cur:][::-1] is {cur},{nums[:cur]},{nums[cur:][::-1]}")
        return nums[:cur]+nums[cur:][::-1] 

s= Solution()
print(s.nextPermutation([3,2,1]))
