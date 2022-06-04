# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] bt
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        lines = [root]
        level = 1

        while len(lines):
            tmpNodes = []
            for node in lines:
                if not node.left and not node.right:
                    return level

                if node.left:
                    tmpNodes.append(node.left)

                if node.right:
                    tmpNodes.append(node.right)

            lines = tmpNodes
            level += 1


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.minDepth(less_skew)}")