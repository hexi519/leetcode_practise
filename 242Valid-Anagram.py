# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def isAnagram(self, source: str, destination: str) -> bool:
        if len(source)!= len(destination) : return False

        from collections import defaultdict
        com = defaultdict(int)
        for char in source:
            com[char]+=1

        for char in destination:
            com[char]-=1

        for value in com.values():
            if value:
                return False 

        return True       