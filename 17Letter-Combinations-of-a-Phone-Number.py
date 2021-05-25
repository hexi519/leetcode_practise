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


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        >>> sol= Solution()
        >>> sol.letterCombinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> sol.letterCombinations("2")
        ['a', 'b', 'c']
        >>> sol.letterCombinations("")
        []
        >>> sol.letterCombinations("7")
        ['p', 'q', 'r', 's']
        """
        # 9 需要注意下
        ans = []
        digitsLen = len(digits)
        if not digitsLen: return ans

        def dfs(index, tmpStrList):  # 当前的位置
            # log.info(f"index,digitsLen,tmpStrList is {index},{digitsLen},{tmpStrList}")
            nonlocal ans
            if index >= digitsLen:
                ans.append(''.join(tmpStrList))
                # log.info(f"ans  updates to {ans}")
                return
            digit = int(digits[index])
            baseStart = 97
            for _ in range(3, digit + 1):
                baseStart += 4 if _ == 8 else 3

            for letter in [chr(baseStart + x) for x in range(4 if (digit == 9) or (digit == 7) else 3)]:
                tmpStrList.append(letter)
                dfs(index + 1, tmpStrList)
                tmpStrList.pop()

        dfs(0, [])

        # print(f"ans is {ans}")
        return ans
