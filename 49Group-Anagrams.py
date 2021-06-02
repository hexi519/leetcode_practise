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


# 快是挺快，就是有点费空间，毕竟每次都存的chars
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        >>> sol = Solution()
        >>> sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
        >>> sol.groupAnagrams([''])
        [['']]
        """
        from collections import defaultdict
        lookup = defaultdict(list)
        for chars in strs:
            lookup[tuple(sorted(chars))].append(chars)

        return lookup.values()