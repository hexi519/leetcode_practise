# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# test case
s = TreeNode(3)
s_left, s_right = TreeNode(4), TreeNode(5) 
s__left, s__right = TreeNode(1), TreeNode(2)
s.left, s.right = s_left, s_right
s.left.left, s.left.right = s__left, s__right
''' s
        3
   4        5
1     2  null null
'''
t = TreeNode(4)
t_left, t_right = TreeNode(1), TreeNode(2)
t.left, t.right = t_left, t_right
''' t
    4      
1       2
'''
tt = TreeNode(3)
tt_left, tt_right = TreeNode(4), TreeNode(5)
# t_left,t_right = TreeNode(3),TreeNode(2)
tt.left, tt.right = tt_left, tt_right
''' tt
    3      
4       5
'''

skew = TreeNode(3)
skew_left, skew_right = None, TreeNode(5)
skew.left, skew.right = skew_left, skew_right
skew_left_, skew_right_ = TreeNode(2), TreeNode(1)
# skew.right.left, skew.right.right = skew_left_, skew_right_
skew.right.left,skew.right.right = skew_left_,skew_right_

''' skew
    3      
null    5
      2   1
'''