# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        >>> sol = Solution()
        >>> sol.wordBreak("leetcode",["leet","code"])
        True
        >>> sol.wordBreak("applepenapple",["apple","pen"])
        True
        >>> sol.wordBreak("catsandog",["cats","dog","sand","and","cat"])
        False
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for len_idx in range(1, len(s) + 1):
            for word in wordDict:
                # print(f"index({len_idx}),word({word}): dp is {dp}")
                if len_idx >= len(word) and s[len_idx - len(word):len_idx] == word and dp[len_idx - len(word)]:
                    dp[len_idx] = True
                    break

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))
