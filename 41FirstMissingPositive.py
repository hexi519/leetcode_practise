<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *

# 每次换位置，都至少会有一个元素被换到正确位置上去。

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.firstMissingPositive([1,2,0])
        3
        >>> s.firstMissingPositive([3,4,-1,1])
        2
        >>> s.firstMissingPositive([7,8,9,11,12])
        1
        >>> s.firstMissingPositive([])
        1
        >>> s.firstMissingPositive([1,2])
        3
        >>> s.firstMissingPositive([1,1])
        2
        """
        numsLen = len(nums)
        for (idx, num) in enumerate(nums):
            while idx+1 != num:
                if num<=0  or num>numsLen: 
                    break
                if nums[num-1]!=num:        #* 防止有重复元素出现陷入死循环
                    nums[idx] ,nums[num-1] = nums[num-1] ,num
                    num = nums[idx]
                else: break

        for (idx, num) in enumerate(nums): 
            if nums[idx]-1!=idx : 
                return idx+1

        return numsLen+1

    #* 在网上看到最妙的就是这个，不用走交换的方式...
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *

# 每次换位置，都至少会有一个元素被换到正确位置上去。

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.firstMissingPositive([1,2,0])
        3
        >>> s.firstMissingPositive([3,4,-1,1])
        2
        >>> s.firstMissingPositive([7,8,9,11,12])
        1
        >>> s.firstMissingPositive([])
        1
        >>> s.firstMissingPositive([1,2])
        3
        >>> s.firstMissingPositive([1,1])
        2
        """
        numsLen = len(nums)
        for (idx, num) in enumerate(nums):
            while idx+1 != num:
                if num<=0  or num>numsLen: 
                    break
                if nums[num-1]!=num:        #* 防止有重复元素出现陷入死循环
                    nums[idx] ,nums[num-1] = nums[num-1] ,num
                    num = nums[idx]
                else: break

        for (idx, num) in enumerate(nums): 
            if nums[idx]-1!=idx : 
                return idx+1

        return numsLen+1

    #* 在网上看到最妙的就是这个，不用走交换的方式...
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
>>>>>>> hesy/master
        return n