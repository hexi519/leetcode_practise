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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.fourSum([1,0,-1,0,-2,2],0)
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> s.fourSum([],0)
        []
        >>> s.fourSum([-2,-1,-1,1,1,2,2],0)
        """
        if len(nums)<4 : return []
        nums.sort()
        res = []
        min_,max_=0,0
        for cur, num in enumerate(nums[:-3]):
            if cur and num==nums[cur-1]: continue
            min_, max_ = num+nums[cur+1]+nums[cur+2] + \
                nums[cur+3], num+nums[-1]+nums[-2]+nums[-3]
            if min_ > target:
                break
            if max_ < target:
                continue
            
            for cur2 in range(cur+1,len(nums)-2):
                sec = nums[cur2]
                if cur2>cur+1 and sec==nums[cur2-1]: continue
                presum = num+sec
                min_, max_ = presum+nums[cur2+1] + \
                    nums[cur2+2], presum+nums[-1]+nums[-2]
                if min_ > target:
                    break
                if max_ < target:
                    continue

                thir, forth = cur2+1, len(nums)-1
                while thir < forth:
                    sum4= presum+nums[thir]+nums[forth]
                    if sum4 > target:
                        forth -= 1
                    elif sum4 < target:
                        thir += 1

                    else:
                        res.append( [num,sec,nums[thir],nums[forth]] )
                        forth -= 1
                        thir += 1

                    while thir > cur2+1 and thir+1 < len(nums) and  nums[thir-1] == nums[thir]:
                        thir += 1

                    while forth+1 < len(nums) and forth and  nums[forth+1] == nums[forth]:
                        forth -= 1
            
        return res
