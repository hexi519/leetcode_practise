# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

"""
我的思路其实是找len为x的word，然后找len为x-1的word，去比较一下看是否match(只差一个字符)，match就递推。 O(NNS)
但是大佬的思路就比较快，找len为x的word，然后将其变化一下找出len-1组合的可能性，看看是否在词典里，在的话就递推。O(NSS)  利用了S范围比N小的特性 
具体代码在网上，我就不在这里CV了
"""
class Solution:
    """
    >>> s = Solution()
    >>> s.longestStrChain(["a","b","ab","bac"])
    2
    >>> s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])
    5
    >>> s.longestStrChain(["a","b","ba","bca","bda","bdca"])
    4
    >>> s.longestStrChain(["bb"])
    1
    """
    def longestStrChain(self, words: List[str]) -> int:

        def match(string1, string2):
            p, q = 0, 0
            if len(string1) - len(string2) == 1:
                shorter, longer = string2, string1
            elif len(string1) - len(string2) == -1:
                shorter, longer = string1, string2
            else:
                return False

            while p < len(shorter) and q < len(longer) and q-p < 2:
                if shorter[p] == longer[q]:
                    p, q = p+1, q+1
                else:
                    q = q+1
            
            if q-p >1: return False

            return True

        # dict 用于记录 len_of_str : [ index1,index2,...]
        from collections import defaultdict
        len2idx = defaultdict(list)
        for idx, word in enumerate(words):  # O(N) 
            len2idx[len(word)].append(idx)

        dp = [0]*(len(words)+1)
        # debug
        # log.info(f"len2idx is {len2idx}")
        keys_of_len = len2idx.keys()
        for key in sorted(len2idx.keys()):     # 从短序开始找   # O(NlogN)
            # log.info(f"key is {key}")   # 确认有无序
            indices = len2idx[key]

            for idx in indices:  # 寻找的就是words[idx]和之前的 O(n^2)无法再简了？
                dp[idx] = max(dp[idx], 1)
                if key-1 in keys_of_len:    # 可以有人递推过来
                    for idx2 in len2idx[key-1]:
                        if match(words[idx], words[idx2]):
                            dp[idx] = max(dp[idx2] + 1, dp[idx])

        return max(dp)
