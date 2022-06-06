######################################
############# Functions #############
######################################
import sys, os


# ============ print ============
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


# ============ ipdb ============
import ipdb


def blockIpdb():
    pass


######################################
############# Data Structures #########
######################################


# ============ Definition for a binary tree node. ============
def preTraverse(root):  # root should be a TreeNode
    if not root:
        print('None', end='\t')
        return

    print(f"{root.val}", end='\t')
    preTraverse(root.left)
    preTraverse(root.right)


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


# * BST
BST = TreeNode(7)
BST_left, BST_right = TreeNode(2), TreeNode(8)
BST__left, BST__right = TreeNode(1), TreeNode(5)
BST.left, BST.right = BST_left, BST_right
BST_left.left = BST__left
BST_right.right = BST__right
BST__left.left = TreeNode(-1)
BST__right.left, BST__right.right = TreeNode(4), TreeNode(6)
''' s
                7
        2             8
    1      null  null    5
-1  null               4   6
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
skew_left, skew_right = None, TreeNode(-5)
skew.left, skew.right = skew_left, skew_right
skew_left_, skew_right_ = TreeNode(2), TreeNode(1)
# skew.right.left, skew.right.right = skew_left_, skew_right_
skew.right.left, skew.right.right = skew_left_, skew_right_
''' skew
    3      
null    -5
      2   1
'''

# * skew tree
less_skew = TreeNode(-10)
less_skew_left, less_skew_right = TreeNode(9), TreeNode(20)
less_skew.left, less_skew.right = less_skew_left, less_skew_right
less_skew_left_, less_skew_right_ = TreeNode(15), TreeNode(15)
# less_skew.right.left, less_skew.right.right = less_skew_left_, less_skew_right_
less_skew.right.left, less_skew.right.right = less_skew_left_, less_skew_right_
''' skew
         -10      
    9           20
null null     15   15
'''

# * deep tree -- dt
dt = TreeNode(0)
dt_left, dt_right = TreeNode(2), TreeNode(4)
dt.left, dt.right = dt_left, dt_right
dt.left.left = TreeNode(1)
dt.left.left.left, dt.left.left.right = TreeNode(5), TreeNode(1)
dt_right_l, dt_right_r = TreeNode(-1), TreeNode(-1)
dt_right.left, dt_right.right = dt_right_l, dt_right_r
dt_right_l.right = TreeNode(8)
dt_right_r.right = TreeNode(8)
''' deep tree
            0      
      2             4
  1     null     -1      -1
5   1         null 8 null 8
'''

# * sysmetric tree -- st
st = TreeNode(0)
st_left, st_right = TreeNode(4), TreeNode(4)
st.left, st.right = st_left, st_right
st.left.left, st.left.right = TreeNode(1), TreeNode(-3)
st_right_l, st_right_r = TreeNode(-3), TreeNode(1)
st_right.left, st_right.right = st_right_l, st_right_r
''' sysmetric tree
            0      
      4             4
  1     -3     -3      1
'''

# ============ Definition for a linked list. ============


class ListNode:

    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        cur = self
        repre = ""
        while cur:
            repre += f"{cur.val}-->"
            cur = cur.next
        return repre


# 没有重复数字的链表  3->4->5->6
linkA = ListNode(3)
An = ListNode(4)
Ann = ListNode(5)
Annn = ListNode(6)
linkA.next, An.next = An, Ann
Ann.next = Annn

# 与linkA相交的linkB（有重复数字）
# 4->3->4->5    4->linkA
linkB = ListNode(4)
# Bn = ListNode(4)
# Bnn = ListNode(5)
# linkB.next, Bn.next = Bn, Bnn
linkB.next = linkA

# 有重复数字的linkC
# 4->4->5
linkC = ListNode(4)
Cn = ListNode(4)
Cnn = ListNode(5)
linkC.next, Cn.next = Cn, Cnn
# linkB.next = linkA
""" oj输入

# 输入输入
s = input()
s = [i for i in s.split()]
print(s)


# 两行输入
while True:
    s = input()
    if s != "":
        length = int(s)
        nums = [int(i) for i in input().split()]
        print(length, nums)
        break
    else:
        break

# 第一行输入操作个数，下面输入n个数组
data = []
length = int(input())
n = 0
while n < length:
    s = input()
    if s != "":
        temp = [i for i in s.split()]
        data.append(temp)
        n = n + 1
    else:
        break
print(data)
"""
