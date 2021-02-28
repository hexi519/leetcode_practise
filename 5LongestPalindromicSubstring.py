<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp 字符串 
'''

from typing import Dict, List
from util import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        >>> s=Solution()
        >>> s.longestPalindrome("babad")
        "bab"
        """
        s = s[::-1]
        s= s+'0'
        s = s[::-1]
        
        strLen = len(s)
        print(f"s is {s} and length is {strLen}")

        dp = [[False] * strLen for _ in range(strLen)]

        for i in range(strLen):
            dp[i][1] = True
            dp[i][0] = True

        for idx in range(1, strLen):
            for length in range(2,strLen - idx + 1) :
                if s[idx]==s[idx+length-1]  and idx<strLen and dp[idx+1][length-2] :
                    dp[idx][length]=True
                else:
                    break
        
        print(dp)
        
        for length in range(1,strLen):
            if any(dp[:][length]):
                for idx in range(1,strLen):
                    if dp[idx][length]:
                        print(f"{s[idx:idx+length-1]}")
                        break


s=Solution()
res = s.longestPalindrome("babad")
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp 字符串 
'''

from typing import Dict, List
from util import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        >>> s=Solution()
        >>> s.longestPalindrome("babad")
        "bab"
        """
        s = s[::-1]
        s= s+'0'
        s = s[::-1]
        
        strLen = len(s)
        print(f"s is {s} and length is {strLen}")

        dp = [[False] * strLen for _ in range(strLen)]

        for i in range(strLen):
            dp[i][1] = True
            dp[i][0] = True

        for idx in range(1, strLen):
            for length in range(2,strLen - idx + 1) :
                if s[idx]==s[idx+length-1]  and idx<strLen and dp[idx+1][length-2] :
                    dp[idx][length]=True
                else:
                    break
        
        print(dp)
        
        for length in range(1,strLen):
            if any(dp[:][length]):
                for idx in range(1,strLen):
                    if dp[idx][length]:
                        print(f"{s[idx:idx+length-1]}")
                        break


s=Solution()
res = s.longestPalindrome("babad")
>>>>>>> hesy/master
