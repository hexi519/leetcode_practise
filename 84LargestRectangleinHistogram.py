# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        listLen = len(heights)
        res = [ [0*listLen] for _ in range(listLen) ]
        for height in heights:
            res[ height ] = 