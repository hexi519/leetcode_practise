<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        >>> s = Solution()
        >>> s.twoSum( [2,7,11,15] , 9)
        [1, 2]
        >>> s.twoSum( [2,3,4] , 6)
        [1, 3]
        >>> s.twoSum( [-1,0] , -1)
        [1, 2]
        >>> s.twoSum( [0] , 0)
        [1, 1]
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            while numbers[left] + numbers[right]> target:
                right -=1
            # print(f"left,right is {left},{right} ,and numbers[left],numbers[right] is {numbers[left]},{numbers[right]}")
            if numbers[left] + numbers[right] == target:
                # return [left + 1, right + 1]
                break
            left += 1

        return [left + 1, right + 1]
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        >>> s = Solution()
        >>> s.twoSum( [2,7,11,15] , 9)
        [1, 2]
        >>> s.twoSum( [2,3,4] , 6)
        [1, 3]
        >>> s.twoSum( [-1,0] , -1)
        [1, 2]
        >>> s.twoSum( [0] , 0)
        [1, 1]
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            while numbers[left] + numbers[right]> target:
                right -=1
            # print(f"left,right is {left},{right} ,and numbers[left],numbers[right] is {numbers[left]},{numbers[right]}")
            if numbers[left] + numbers[right] == target:
                # return [left + 1, right + 1]
                break
            left += 1

        return [left + 1, right + 1]
>>>>>>> hesy/master
