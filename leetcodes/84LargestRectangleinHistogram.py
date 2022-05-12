# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.largestRectangleArea([2,0,2])
        2
        >>> s.largestRectangleArea([2,1,5,6,2,3])
        10
        >>> s.largestRectangleArea([2,4])
        4
        >>> s.largestRectangleArea([0])
        0
        """
        left = [ -1 for index in range(len(heights))]
        right = [ len(heights) for index in range(len(heights))]

        from collections import deque
        mq= deque()
        for index, height in enumerate(heights):
            # log.info(f"cur is {height}")
            while len(mq) and mq[-1][1]> height:    # 越矮的越进去
                # log.info(f"mq is {mq} and pop {mq[-1]}")
                right[mq.pop()[0]]=index

            left[index] = mq[-1][0] if len(mq) else left[index]
            mq.append( (index,height) )
        
        # log.info(f"summary is {[(left[index],heights[index],right[index])for index in range(len(heights))]}")

        ans = 0
        for index in range(len(heights)):
            # min_height = heights[index]
            # if not right[index] ==len(heights):
            #     min_height = min(min_height, heights[right[index]])
            # if not left[index] ==-1:
            #     min_height = min(min_height, heights[left[index]])
                
            ans = max( (right[index]-left[index]-1)*heights[index] ,ans)

        return ans