<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] [dp series]
'''

from typing import Dict, List
from util import *
import numpy as np


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.rob([2,3,2])
        3
        >>> s.rob([1,2,3,1])
        4
        >>> s.rob([0])
        0
        """
        numAll = len(nums) + 1

        if(numAll ==1): return 0
        if(numAll ==2): return nums[0]

        nums.append(0)
        nums.reverse()
        nums.append(0)
        nums.reverse()

        withFirst, withoutFirst = np.array([[[0] * 2 for _ in range(numAll)] for _ in range(2)])

        # rob 1 to n-1
        withFirst[1] = [0, nums[1]]
        for i in range(2, numAll-1):
            withFirst[i][0] = max(withFirst[i - 1])
            withFirst[i][1] = withFirst[i - 1][0] + nums[i]

        # rob 2 to n
        nums.reverse()  # 0,n_1,n_2,...   --> n_n,n_{n-1},...,n_2,n_1,0
        withoutFirst[1] = [0, nums[1]]
        for i in range(2, numAll-1):
            withoutFirst[i][0] = max(withoutFirst[i - 1])
            withoutFirst[i][1] = withoutFirst[i - 1][0] + nums[i]

        return max(max(withFirst[numAll - 2]), max(withoutFirst[numAll - 2]))
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] [dp series]
'''

from typing import Dict, List
from util import *
import numpy as np


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.rob([2,3,2])
        3
        >>> s.rob([1,2,3,1])
        4
        >>> s.rob([0])
        0
        """
        numAll = len(nums) + 1

        if(numAll ==1): return 0
        if(numAll ==2): return nums[0]

        nums.append(0)
        nums.reverse()
        nums.append(0)
        nums.reverse()

        withFirst, withoutFirst = np.array([[[0] * 2 for _ in range(numAll)] for _ in range(2)])

        # rob 1 to n-1
        withFirst[1] = [0, nums[1]]
        for i in range(2, numAll-1):
            withFirst[i][0] = max(withFirst[i - 1])
            withFirst[i][1] = withFirst[i - 1][0] + nums[i]

        # rob 2 to n
        nums.reverse()  # 0,n_1,n_2,...   --> n_n,n_{n-1},...,n_2,n_1,0
        withoutFirst[1] = [0, nums[1]]
        for i in range(2, numAll-1):
            withoutFirst[i][0] = max(withoutFirst[i - 1])
            withoutFirst[i][1] = withoutFirst[i - 1][0] + nums[i]

        return max(max(withFirst[numAll - 2]), max(withoutFirst[numAll - 2]))
>>>>>>> hesy/master
