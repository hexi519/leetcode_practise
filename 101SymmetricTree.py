# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] a symmetric tree or not
'''

from typing import Dict, List
from util import *

##############################
########### 剑指的思路，遍历完不需要再对比 ##########
########### 只走一遍，recursive ##########
##############################
class Solution:
    """
    >>> sol = Solution()
    >>> sol.isSymmetric(s)
    True
    >>> sol.isSymmetric(t)
    False
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  #* 之前自己老是喜欢写成 if root == None 太low了,还慢
            return True
        l, r = root.left, root.right
        if l == None or r == None:
            return True if l == r else False
        ll, lr = l.left, l.right
        rl, rr = r.left, r.right

        def compare(l_: root, r_: TreeNode) -> bool:
            if l_ == None or r_ == None:
                return True if l_ == r_ else False

            return l_.val == r_.val and compare(l_.left, r_.right) and compare(l_.right, r_.left)

        return compare(l, r)

"""
################################
########### my codes ##########
########### recursive ##########
################################
# 走了两趟,一遍是root,left,right这么走;另一遍是root,right,left。然后对比看结果是否一致。
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverse_tree(node, mode: bool):
            if not node: return None
            rl, rr = node.left, node.right
            return f"#{node.val} {traverse_tree(rl,mode)} {traverse_tree(rr,mode)}" if mode else f"#{node.val} {traverse_tree(rr,mode)} {traverse_tree(rl,mode)}"

        # print(
        #     f"2 travsercy is {traverse_tree(root,True)}@{traverse_tree(root,False)}"
        # )
        return traverse_tree(root, True) == traverse_tree(root, False)


################################
########### my codes ##########
########### iterative ##########
################################
# 走了两趟, 一遍是 root ,left ,right这么走;另一遍是root ,right,left。然后对比看结果是否一致。
# 相比于递归，时间没变少，空间反而变大了....
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ll, lr = [], []
        sl, sr = [], []  
        sl.append(root)
        sr.append(root)

        def traverse(s_: list, mode: bool, l_: list) -> list:
            while len(s_):
                cur = s_.pop()
                if cur:
                    cl, cr = cur.left, cur.right
                    # for recursive
                    if mode:
                        s_.extend([cl, cr])
                    else:
                        s_.extend([cr, cl])
                    # for record
                    l_.append(str(cur.val))
                else:
                    l_.append("None")

        traverse(sl, True, ll)
        traverse(sl, False, lr)
        return ll == lr  #* list对应元素比较,用==就可以~
"""