# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   []
'''

from typing import Dict, List
from util import *
from loguru import logger as log

class Solution(object):
    # iterative
    def inorderTraversal(self, root):   # with the help of a stack
        """
        >>> sol = Solution()
        >>> sol.inorderTraversal(skew)
        [3, 2, 5]
        >>> sol.inorderTraversal(None)
        []
        >>> sol.inorderTraversal(TreeNode(1))
        [1]
        >>> sol.inorderTraversal(tt)
        [4, 3, 5]
        """
        nodeStack,res = [],[]  # first push right and then mid, finally left
        if root is None: return res
        nodeStack.append(root)
        cur = root.left
        # ! while里面尽量不要套while...能用单次解决的，就让他单次...别套。套了就会像下面这样纠结错掉...
        """
        while len(nodeStack):
            while cur:
                log.info(f"压入左子节点 {cur.val}，且cur前进到{cur.left.val}")
                nodeStack.append(cur)
                cur = cur.left
            cur = nodeStack.pop()
            log.info(f"弹出节点 {cur.val}")
            res.append(cur.val)
            if not cur.right:    # keep poping until get sth.
                cur = nodeStack.pop()   
                log.info(f"接着弹出节点 {cur.val}")
                res.append(cur.val)
            else:
                cur = cur.right
                log.info(f"cur前进到{cur.val}")
        """
        while len(nodeStack) or cur:  # 有可能遍历到整棵树的根节点，which means 栈空，但是还没有处理完
            if cur:    # 防止上一次弹出的节点无右子节点，得接着弹
                # log.info(f"压入左子节点 {cur.val}，且cur前进到{cur.left.val}")
                nodeStack.append(cur)
                cur = cur.left
            else:
                cur = nodeStack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
        # while len(nodeStack):
        #     cur = nodeStack.pop()
        #     res.

    """
    # recursive
    def inorderTraversal(self, root):   # with the help of a stack
        def help_recur( root, res):
            if root.left:
                print(f"\t 进入左子节点({root.left.val}) with res of {res}")
                help_recur(root.left,res)

            res.append(root.val)
            print(f"\t 添加自身信息({root.val}) with res of {res}")

            if root.right:
                print(f"\t 进入右子节点({root.right.val}) with res of {res}")
                help_recur(root.right,res)
        
        res=[]
        if root is None: 
            print(f"root is Nones")
            return res
        help_recur(root,res)
        log.info(f"res is {res}")
        return res
    """
    # morris
    """
        其实左神的morris遍历是真的不错，省去了冗余代码。但是我的morris遍历就比较便于阅读
    """
    """
    def inorderTraversal(self, root):
        res = []
        # 不需要额外的空间，所以递归是不可能滴~只用循环即可，外加两个哨兵
        cur, mor = root, None     # in case of [null]
        
        while cur :
            # 进入
            mor = cur.left
            # mor = cur.left if cur.left else cur.right 
            #! 下面这里不能写成while mor的形式，因为有可能cur会变成None,如果只根据mor的情况去,有可能mor一直为非空，但是cur为空，导致死循环！
            # 其实这主要是牵扯一个写代码的小常识...当外面有一个while的时候，里面除非很确认不会死循环，否则不要轻易嵌套while...
            # 感觉还是要非常小心....
            if mor: # 如果存在左子节点，就找出左子树的最右节点建立关系，并且后面每个节点都会经过两次遍历
                while mor.right and mor.right!=cur:
                    mor = mor.right
                if mor.right==cur:  # 第二次遍历到了，拆除关系，右移
                    res.append(cur.val)
                    cur = cur.right
                    # mor.right = None # 不拆除也没关系..反正也是最后一次(第二次)遍历了..

                else :  # 第一次遍历到，处理完cur的前序节点，就可以接着左移了
                    mor.right = cur
                    cur = cur.left
            else: 
                res.append(cur.val) # 因为没有左子节点，直接走向右子节点，所以相当于第二次遍历到自己了
                cur = cur.right
            总结为:
            1. 中序遍历中，只要一个节点想要往右子树移动了，就得打印(说明第二次遍历自己了)。
                因为只有两次遍历到，第一次遍历到，后续要往左子树移动，第二次遍历到，
                就要往右子树移动，第二次遍历打印就是中序遍历。
            2. 在Morris遍历中，每一次cur都在变换位置，就没有不变的时候
        return res
            """
