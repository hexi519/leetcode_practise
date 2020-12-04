# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] find whether there is a path from root to leaf whose sum is equal to a given number
'''

from typing import Dict, List
from util import *


class Solution:
    """
    >>> sol = Solution()
    >>> sol.hasPathSum0(s,8)
    True
    >>> sol.hasPathSum0(s,7)
    False
    >>> sol.hasPathSum0(s,15)
    False

    >>> sol.hasPathSum4(s,8)
    True
    >>> sol.hasPathSum4(s,7)
    False
    >>> sol.hasPathSum4(s,15)
    False

    >>> sol.hasPathSum1(s,8)
    True
    >>> sol.hasPathSum1(s,7)
    False
    >>> sol.hasPathSum1(s,15)
    False

    >>> sol.hasPathSum2(s,7)
    True

    """
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return 0==
        
        return 
        res = []
        def addSum(self , root ):
            nonlocal res
            if not root ：
                return 0
            res.append(addSum(root.left)+root.val,addSum(root.left)+root.val)
            return 
    """

    ################################
    ############ 剑指思路 ##########
    ########### recursive ##########
    ################################
    def hasPathSum0(self, root, sum):
        # TODO 这里需要总结下
        # TODO iterative的写法还没有熟练 (其实这里用iterasive才能更节省时间吧，毕竟可以中途退出)
        # TODO 主要卡的一些测试点：斜树；子节点和父节点一致的情况[1,1]；空的根节点；val是负数的情况（所以请不要随便用大于号或者小于号之类的...只用不等号！）
        """
        两种都要会实现： recursive和iterative的参数传递
            前者方便实现，后者方便中途退出。
            无论是路径还是总体路径和，都可以当作路径传递，只不过前者传递得比较多罢了(要求路径的话，还得注意返回值的写法不一样，没法直接return preTraverse(left) or preTraverse(right),因为判断子节点的遍历成功与否后，还得再对传递的参数进行修改)。
            其他的求解方法不过是在其基础上进行一些简化或者改进，比如hasPathSum1只不过是把路径参数的传递省下来了。

        必须要包含根节点-》 前序遍历 ；
        """
        def preTraverse(root, sum, pathSum):
            if not root:
                return False

            pathSum += root.val
            # TODO 呵呵我这里完全忽视了val是负数的情况，本来是想早点截止的
            # if  pathSum > sum :
            #     return False

            if pathSum == sum:
                # leaf node
                if (not root.left) and (not root.right):
                    return True
                # TODO 呵呵，这里惨死的一个样例：
                # [1,-2,-3,1,3,-2,null,-1]
                # -1
                # 明明是想早点停止的。。。画蛇添足，以后还是先实现一个最基本的，然后再考虑能不能早点停止吧
                # else :
                #     return False

            return preTraverse(root.left, sum, pathSum) or preTraverse(
                root.right, sum, pathSum)

        return preTraverse(root, sum, 0)

################################
##### 剑指思路改成iterative #####
################################
# TODO iterasion的参数传递就没有办法像recursion那么elegant了，每次recursion进行修改然后用参数传递修改值，iterasion必须要把参数和node绑定在一起进行压栈和弹栈,which means每个节点进出各一次
# 目前参数比较少，所以空间上还能胜过recursive，which占用内存比较多
    def hasPathSum4(self, root, sum):
        if not root:
            return False
        status = [(root,0)]

        while (len(status)):
            node, value = status.pop()
            pathSum = value + node.val
            # leaf
            if pathSum == sum and (not node.left) and (not node.right):
                return True

            # TODO 其实一般不在这里判断，在上面判断，which和 [] 的判断结合在一起，有时间修改一下。这样代码比较短，但是会多余一些节点的进出栈
            if node.left:
                status.append( (node.left,pathSum) )
            if node.right:
                status.append( (node.right,pathSum) )

        return False


################################
###########  精妙，省空间 ##########
########### recursive ##########
################################
# TODO 如果是从头到树的中间呢? 如果是不一定root，也不一定是leaf呢？
# TODO 如果是从底部向上呢

    """ case(1) from root to leaf """
    def hasPathSum1(self, root, sum):
        if not root:
            return False

        # 得判断确实是个leaf
        if not root.left and not root.right and root.val == sum:
            return True

        # print(f"sum is {sum} and cur.val is {root.val}")
        sum -= root.val

        return self.hasPathSum1(root.left, sum) or self.hasPathSum1(
            root.right, sum)

    """ case(2) from root to any node( whether is to leaf is not important) """

    def hasPathSum2(self, root, sum):
        if not root:
            return False

        # 无需判断是否是个leaf
        if root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum2(root.left, sum) or self.hasPathSum2(
            root.right, sum)

    """ case(3) from any node to leaf ( whether is from root is not important) 
    
        从root到any node(including leaf)需要前序遍历(保证是从root开始)
        从any node(including root)到leaf需要后序遍历(保证是到leaf结束)
    """

    def hasPathSum3(self, root, sum):
        res = self.hasPathSum(root.left, sum) or self.hasPathSum(
            root.right, sum)
        if not root:
            return False

        # 无需判断是否是个leaf
        if root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum3(root.left, sum) or self.hasPathSum3(
            root.right, sum)
