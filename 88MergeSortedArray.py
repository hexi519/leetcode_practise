# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        >>> s = Solution()
        >>> s.merge( [1,2,3,0,0,0] , 3, [2,5,6] , 3 )
        [1, 2, 2, 3, 5, 6]
        >>> s.merge( [7,7,0,0,0] , 2, [2,5,6] , 3 )
        [2, 5, 6, 7, 7]
        >>> s.merge( [7] , 1, [] , 0 )
        [7]
        >>> s.merge( [] , 0, [] , 0 )
        []
        """
        tailOne, tailTwo = m - 1, n - 1
        tail = m + n - 1
        while tail > 0 and tailOne >= 0 and tailTwo >= 0:
            if nums1[tailOne] > nums2[tailTwo]:
                nums1[tail], tailOne, tailTwo, tail = nums1[tailOne], tailOne - 1, tailTwo, tail - 1
            else:
                nums1[tail], tailOne, tailTwo, tail = nums2[tailTwo], tailOne, tailTwo - 1, tail - 1

        if tailTwo >= 0:  # nums1先结束了
            nums1[:tailTwo+1] = nums2[:tail+1]
        return nums1
