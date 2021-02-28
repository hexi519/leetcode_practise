<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]331VerifyPreorderSerializationofBinaryTree
'''
# TODO 逻辑上不难，但是要注意边界情况--》虽然给的字符串格式没有问题， 但是人家没说给的字符串符合逻辑啊...所以要注意一些边界情况，还有考虑到一个字符后面的各种可能性

from typing import Dict, List
from util import *
"""
331cnt的想法做一次，再用递归的思路做一次
平衡二叉树题目有感：递归的辅助函数的返回值不需要压倒栈里面，参数是要压进去的，但是返回值可以做一个全局变量，因为他不是从下到上传递的，而是只根据当前已经遍历处理过的节点计算出来的（不需要利用到以往的信息），所以该变量值随着我们的当前节点而变动
"""


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
    slot当前可以放置新node(including null node)的位置 
    或者理解成还需要被node填充的位置
    另一个比较不同的角度就是理解成树的出度(outdegree)
    但还是要考虑到有个问题，两棵树拼在一起的特殊案例
    """
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

    # recursion  时空开销都不大
    # motivated by [this](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/362721/10-lines-concise-C%2B%2B-solution-recursion.) and transform into pythonic codes.
    def isValidSerialization(self, preorder: str) -> bool:
        from collections import deque
        array = deque(preorder.split(','))

        def validSubtree(array):
            if not array:
                return False

            node = array.popleft()

            return True if node == '#' else (validSubtree(array) and validSubtree(array)
)
        # len ==0 to avoid 两颗完整子树拼在一起的情况
        return validSubtree(array) and len(array) == 0


#         7
#     2   #
# 2   #
# # #

# recursion
# def isValidSerialization(self, preorder: str) -> bool:
#     array = preorder.split(',')
#     if len(array)==1 and :
#         return isValidSerialization(preorder[2:])
#     if preorder=="#":
#         return True

#     return cnt==0
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]331VerifyPreorderSerializationofBinaryTree
'''
# TODO 逻辑上不难，但是要注意边界情况--》虽然给的字符串格式没有问题， 但是人家没说给的字符串符合逻辑啊...所以要注意一些边界情况，还有考虑到一个字符后面的各种可能性

from typing import Dict, List
from util import *
"""
331cnt的想法做一次，再用递归的思路做一次
平衡二叉树题目有感：递归的辅助函数的返回值不需要压倒栈里面，参数是要压进去的，但是返回值可以做一个全局变量，因为他不是从下到上传递的，而是只根据当前已经遍历处理过的节点计算出来的（不需要利用到以往的信息），所以该变量值随着我们的当前节点而变动
"""


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
    slot当前可以放置新node(including null node)的位置 
    或者理解成还需要被node填充的位置
    另一个比较不同的角度就是理解成树的出度(outdegree)
    但还是要考虑到有个问题，两棵树拼在一起的特殊案例
    """
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

    # recursion  时空开销都不大
    # motivated by [this](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/362721/10-lines-concise-C%2B%2B-solution-recursion.) and transform into pythonic codes.
    def isValidSerialization(self, preorder: str) -> bool:
        from collections import deque
        array = deque(preorder.split(','))

        def validSubtree(array):
            if not array:
                return False

            node = array.popleft()

            return True if node == '#' else (validSubtree(array) and validSubtree(array)
)
        # len ==0 to avoid 两颗完整子树拼在一起的情况
        return validSubtree(array) and len(array) == 0


#         7
#     2   #
# 2   #
# # #

# recursion
# def isValidSerialization(self, preorder: str) -> bool:
#     array = preorder.split(',')
#     if len(array)==1 and :
#         return isValidSerialization(preorder[2:])
#     if preorder=="#":
#         return True

#     return cnt==0
>>>>>>> hesy/master
