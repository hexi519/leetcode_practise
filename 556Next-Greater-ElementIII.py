# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

# 网上写的相当快的(都在90%多。我的空间可以90%但是时间只有50%多）
# 它主要是利用了str的拼合，而省去了我的除法、取余等等运算
class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(map(int, str(n)))
        i = len(s)-1
        while i-1>=0 and s[i]<=s[i-1]:
            i -= 1
            
        if i==0:
            return -1
        
        j = i
        while j+1<len(s) and s[j+1]>s[i-1]:
            j += 1
        
        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = reversed(s[i:])
        ret = int(''.join(map(str, s)))
        
        return ret if ret<=((1<<31)-1) else -1


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.nextGreaterElement(12)
        21
        >>> s.nextGreaterElement(21)
        -1
        >>> s.nextGreaterElement(230241)
        230412
        >>> s.nextGreaterElement(2147483476)
        2147483647
        >>> s.nextGreaterElement(12443322)
        13222344
        """
        if n > 2**31 - 1: return -1
        digits = []
        flag = -1
        while n:
            if len(digits) and n % 10 < digits[-1]:
                flag = n % 10
                break
            digits.append(n % 10)
            n = n // 10
        if not n: return -1
        from bisect import bisect_right 
        to_insert = bisect_right(digits, flag)
        flag, digits[to_insert] = digits[to_insert], flag
        n = (n//10) * 10 + flag
        for d in digits:  # in range(len(digits) - 1, -1, -1):  # d in enumerate(digits):
            n = n * 10 + d

        return n if n < 2**31 else -1
