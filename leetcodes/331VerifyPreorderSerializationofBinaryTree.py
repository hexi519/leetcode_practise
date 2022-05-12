# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]331VerifyPreorderSerializationofBinaryTree 第二遍做对了
'''
from typing import Dict, List
from util import *
from loguru import logger as log

class Solution:
    """
    >>> sol = Solution()
    >>> sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    True
    >>> sol.isValidSerialization("")
    False
    >>> sol.isValidSerialization("7,2,#,2,#,#,#,6,#")
    False

    # 根据错误新赠的...
    >>> sol.isValidSerialization("#")
    True
    >>> sol.isValidSerialization("#,#,3,4")
    False
    """
    """
    slot当前可以放置新node(including null node)的位置   #* 还是看recursive比较省事
    或者理解成还需要被node填充的位置
    另一个比较不同的角度就是理解成树的出度(outdegree)
    但还是要考虑到有个问题，两棵树拼在一起的特殊案例
    
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1  # 我们目前只知道会有个根节点，所以就slot为1
        array = preorder.split(',')

        for node in array:
            # 可能重新开了一颗子树，这个时候树值上最后还是会等于0，但这个已经不对了。
            if not slot:
                return False

            # 下面这个if else语句 steven大佬用了slot-=" #".find(node) 来代替，确实是精妙！不过有点炫技之嫌
            if node == "#":
                slot -= 1
            else:
                slot += 1

        return slot == 0
    """
    # recursion  时空开销都不大
    # motivated by [this](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/362721/10-lines-concise-C%2B%2B-solution-recursion.) and transform into pythonic codes.
    def isValidSerialization(self, preorder: str) -> bool:
        from collections import deque
        array = deque(preorder.split(','))

        def validSubtree(array):
            if not array:
                return False
            node = array.popleft()
            return True if node == '#' else (validSubtree(array) and validSubtree(array))

        # len ==0 to avoid 两颗完整子树拼在一起的情况
        return validSubtree(array) and len(array) == 0
