<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] find whether B is a subtree of A
'''

from typing import Dict, List
from util import *

################################
########### 剑指代码 ##########
################################
"""
* 这个后面的代码都利用了API(有字符串查找功能)所以写起来比较简单，但是这种思路开销比较大，递归之后还需要进一步的字符串查找
* 明明可以在递归中就顺便完成的事情不要拖到最后另外做，一方面代码繁琐，另一方面可能会引起更多的开销（比如说这里）
* 注意，这里跟剑指offer的题目要求还稍有出入(子树不能在中间，必须得在底部)。
"""
class Solution:
    """
    >>> sol = Solution()
    >>> sol.isSubtree(s,t)
    True
    >>> sol.isSubtree(s,tt)
    False
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        if s.val == t.val:
            if self.hasSubTree(s,t):
                return True
        
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def hasSubTree(self,s: TreeNode, t: TreeNode):
        if not t:
            return False if s else True
        
        if not s: 
            return False

        if not s.val==t.val:
            return False

        return self.hasSubTree(s.left,t.left) and self.hasSubTree(s.right,t.right)


"""
################################
########### 优化的代码 ##########
################################
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        # print(f"(subTree@wholeTree) is ({string_t}@{string_s})")
        if string_t in string_s:
            return True
        return False
    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None

################################
########### 更短的代码 ##########
################################

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traverse_tree(node):
            if not node: return None
            return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"

        return traverse_tree(t) in traverse_tree(s)

################################
########### 自己的代码 ##########
################################
#* 其实写得跟优化版本差不多，但是在拼接字符串那儿不够简洁。而且人家前后使用的是不同的符号标注(前面是# 后面是space)，显得很清楚
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        subTree = self.preTraverse(t)
        wholeTree = self.preTraverse(s)
        # print(f"(subTree@wholeTree) is ({subTree}@{wholeTree})")
        return True if wholeTree.find(subTree) != -1 else False

    def preTraverse(self, node: TreeNode):
        if (node == None):
            return "N"
        sep, treeStr = ",", ""
        treeStr += sep + str(node.val)
        treeStr += sep + self.preTraverse(node.left)
        treeStr += sep + self.preTraverse(node.right)
        return treeStr

=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] find whether B is a subtree of A
'''

from typing import Dict, List
from util import *

################################
########### 剑指代码 ##########
################################
"""
* 这个后面的代码都利用了API(有字符串查找功能)所以写起来比较简单，但是这种思路开销比较大，递归之后还需要进一步的字符串查找
* 明明可以在递归中就顺便完成的事情不要拖到最后另外做，一方面代码繁琐，另一方面可能会引起更多的开销（比如说这里）
* 注意，这里跟剑指offer的题目要求还稍有出入(子树不能在中间，必须得在底部)。
"""
class Solution:
    """
    >>> sol = Solution()
    >>> sol.isSubtree(s,t)
    True
    >>> sol.isSubtree(s,tt)
    False
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        if s.val == t.val:
            if self.hasSubTree(s,t):
                return True
        
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def hasSubTree(self,s: TreeNode, t: TreeNode):
        if not t:
            return False if s else True
        
        if not s: 
            return False

        if not s.val==t.val:
            return False

        return self.hasSubTree(s.left,t.left) and self.hasSubTree(s.right,t.right)


"""
################################
########### 优化的代码 ##########
################################
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        # print(f"(subTree@wholeTree) is ({string_t}@{string_s})")
        if string_t in string_s:
            return True
        return False
    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None

################################
########### 更短的代码 ##########
################################

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traverse_tree(node):
            if not node: return None
            return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"

        return traverse_tree(t) in traverse_tree(s)

################################
########### 自己的代码 ##########
################################
#* 其实写得跟优化版本差不多，但是在拼接字符串那儿不够简洁。而且人家前后使用的是不同的符号标注(前面是# 后面是space)，显得很清楚
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        subTree = self.preTraverse(t)
        wholeTree = self.preTraverse(s)
        # print(f"(subTree@wholeTree) is ({subTree}@{wholeTree})")
        return True if wholeTree.find(subTree) != -1 else False

    def preTraverse(self, node: TreeNode):
        if (node == None):
            return "N"
        sep, treeStr = ",", ""
        treeStr += sep + str(node.val)
        treeStr += sep + self.preTraverse(node.left)
        treeStr += sep + self.preTraverse(node.right)
        return treeStr

>>>>>>> hesy/master
"""