# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]437PathSumIII find path number in a tree ,where path sum equals to the given number
'''

from typing import Dict, List
from util import *


# 双重递归 - O(n^2)  1000个node python跑出了1000ms...
class Solution:
    """
    >>> sol = Solution()
    >>> sol.pathSum(s,8)
    2
    >>> sol.pathSum(tt,8)
    1
    >>> sol.pathSum(tt,15)
    0
    """
    # 这里就是套之前的paradigm(见到112 和113 )。注意，外层的递归由于不需要额外的参数，所以不需要多创建一个助手函数，内层的递归也是。
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # bound
        if not root:
            return 0
        # process para
        def dfs(root, sum):
            # TODO 记录：如果count需要向下传递，则要设置成全局变量(并且在参数中传递)，但是这里是向上传递，所以设置成局部变量(函数参数里面也没有它)。
            count = 0
            # bound
            if not root:
                return 0
            if root.val == sum:
                count += 1
            # process para
            count += dfs(root.left,sum-root.val)
            count += dfs(root.right,sum-root.val)

            return count
        # recursion
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(
            root.right, sum)



# TODO dp -- O(n)
