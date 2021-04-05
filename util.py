############# Definition for a binary tree node. #############
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# * BST
BST = TreeNode(4)
BST_left, BST_right = TreeNode(2), TreeNode(5)
BST__left, BST__right = TreeNode(1), TreeNode(3)
BST.left, BST.right = BST_left, BST_right
BST.left.left, BST.left.right = BST__left, BST__right
''' s
        4
   2        5
1     3  null null
'''
BST_ = TreeNode(2)
t_left, t_right = TreeNode(1), TreeNode(4)
BST_.left, BST_.right = t_left, t_right
''' t
    2      
1       4
'''
tt = TreeNode(3)
tt_left, tt_right = TreeNode(4), TreeNode(5)
# t_left,t_right = TreeNode(3),TreeNode(2)
tt.left, tt.right = tt_left, tt_right
''' tt
    3      
4       5
'''

# * skew tree
skew = TreeNode(3)
skew_left, skew_right = None, TreeNode(5)
skew.left, skew.right = skew_left, skew_right
skew_left_, skew_right_ = TreeNode(2), TreeNode(1)
# skew.right.left, skew.right.right = skew_left_, skew_right_
skew.right.left, skew.right.right = skew_left_, skew_right_

''' skew
    3      
null    5
      2   1
'''
############# Definition for a linked list. #############


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 没有重复数字的链表  3->4->5
linkA = ListNode(3)
An = ListNode(4)
Ann = ListNode(5)
linkA.next, An.next = An, Ann

# 与linkA相交的linkB（有重复数字） 3->3->4->5
linkB = ListNode(4)
# Bn = ListNode(4)
# Bnn = ListNode(5)
# linkB.next, Bn.next = Bn, Bnn
linkB.next = linkA
