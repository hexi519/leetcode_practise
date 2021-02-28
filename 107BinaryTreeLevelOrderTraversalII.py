<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] level traverse from bottom to top
'''

##############################
### 把102的reverse就可以... ###
##############################
class Solution:
    """
    >>> sol = Solution()
    >>> sol.levelOrder(s)
    [[3], [4, 5], [1, 2]]
    >>> sol.levelOrder(t)
    [[4], [1, 2]]
    """
    def levelOrderBottom(self, root) :#-> List[List[int]]:
        res = []
        cur_lev_node = [ root ] if root else []
        while len(cur_lev_node):
            res.append([ node.val for node in cur_lev_node ] )
            LRpair = [(node.left, node.right) for node in cur_lev_node]
            #* 外层循环先写，然后再是内层循环
            #* 这里很容易把 if leaf 漏掉... 然后就会报错val为None
            cur_lev_node = [leaf for LR in LRpair for leaf in LR if leaf ] 

=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] level traverse from bottom to top
'''

##############################
### 把102的reverse就可以... ###
##############################
class Solution:
    """
    >>> sol = Solution()
    >>> sol.levelOrder(s)
    [[3], [4, 5], [1, 2]]
    >>> sol.levelOrder(t)
    [[4], [1, 2]]
    """
    def levelOrderBottom(self, root) :#-> List[List[int]]:
        res = []
        cur_lev_node = [ root ] if root else []
        while len(cur_lev_node):
            res.append([ node.val for node in cur_lev_node ] )
            LRpair = [(node.left, node.right) for node in cur_lev_node]
            #* 外层循环先写，然后再是内层循环
            #* 这里很容易把 if leaf 漏掉... 然后就会报错val为None
            cur_lev_node = [leaf for LR in LRpair for leaf in LR if leaf ] 

>>>>>>> hesy/master
        return res[::-1]