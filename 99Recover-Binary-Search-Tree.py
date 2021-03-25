# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

class Solution: # 中序遍历
    # with O(n) space 
    def recoverTree(self, root: TreeNode) -> None:
        """
        >>> s = Solution()
        >>> s.recoverTree(tt)
        [3, 4, 5]
        """
        traverse = []
        nodeStack = [root]
        cur = root.left
        
        while len(nodeStack) or cur:
            if cur:
                nodeStack.append(cur)
                cur = cur.left       
            else:
                cur = nodeStack.pop()
                traverse.append(cur.val)
                cur = cur.right

        # log.info(f"inorder is {traverse}")
        time = 0
        index = [0,0]
        prev = traverse[0]
        for idx in range(1,len(traverse)):
        # 遇到第一个大小颠倒的，就记录下大的那个数字,遇到第二个大小颠倒的，就记录下小的那个数字
            if traverse[idx] > traverse[idx+1]:
                index[time] = idx if time==0 else idx+1
                time+=1
                # log.info(f"update index to be {index}")

        if time ==1:
            traverse[index[0]],traverse[index[0]+1] = traverse[index[0]+1],traverse[index[0]] 
        else:
            traverse[index[0]],traverse[index[1]] = traverse[index[1]],traverse[index[0]] 
        return traverse