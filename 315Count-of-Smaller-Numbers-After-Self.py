# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   []
'''

from typing import Dict, List
from util import *

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        record = dict()
        for item in nums.reverse():
            
            