<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.lengthOfLIS([10,9,2,5,3,7,101,18])
        4
        >>> s.lengthOfLIS([0,1,0,3,2,3])
        4
        >>> s.lengthOfLIS([7,7,7,7,7,7,7])
        1
        >>> s.lengthOfLIS([7])
        1
        """
        if not len(nums): return 0
        dp = []
        for num in nums:
            if not len(dp):  # the first number
                dp.append(num)
            else:
                # 二分搜索 第一个比他大的. 如果找到他本身, 就退出,无需更新(因为要严格递增)
                #* 果然还是左闭右闭写得最快...
                left, right = 0, len(dp)-1
                mid = left + (right - left) // 2
                find_flag = False
                while left <= right:
                    # print(f"num is {num} , left ,mid , right is nums[{left}]:{nums[left]},nums[{mid}]:{nums[mid]},nums[{right}] ")
                    if dp[mid] == num:
                        find_flag = True
                        break
                    else:
                        left, right = (mid +1 ,right) if dp[mid] < num else (left,mid-1)
                    mid = left+ (right - left) // 2
                
                if find_flag : continue

                if left == len(dp):
                    dp.append(num)
                else:
                    dp[left] = num
                # print(f"dp update to {dp}")

        return len(dp)

# s = Solution()
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.lengthOfLIS([10,9,2,5,3,7,101,18])
        4
        >>> s.lengthOfLIS([0,1,0,3,2,3])
        4
        >>> s.lengthOfLIS([7,7,7,7,7,7,7])
        1
        >>> s.lengthOfLIS([7])
        1
        """
        if not len(nums): return 0
        dp = []
        for num in nums:
            if not len(dp):  # the first number
                dp.append(num)
            else:
                # 二分搜索 第一个比他大的. 如果找到他本身, 就退出,无需更新(因为要严格递增)
                #* 果然还是左闭右闭写得最快...
                left, right = 0, len(dp)-1
                mid = left + (right - left) // 2
                find_flag = False
                while left <= right:
                    # print(f"num is {num} , left ,mid , right is nums[{left}]:{nums[left]},nums[{mid}]:{nums[mid]},nums[{right}] ")
                    if dp[mid] == num:
                        find_flag = True
                        break
                    else:
                        left, right = (mid +1 ,right) if dp[mid] < num else (left,mid-1)
                    mid = left+ (right - left) // 2
                
                if find_flag : continue

                if left == len(dp):
                    dp.append(num)
                else:
                    dp[left] = num
                # print(f"dp update to {dp}")

        return len(dp)

# s = Solution()
>>>>>>> hesy/master
# s.lengthOfLIS([10,9,2,5,3,7,101,18])