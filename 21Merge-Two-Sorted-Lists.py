# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Input: l1 = [1,2,4], l2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        
        Input: l1 = [], l2 = [0]
        Output: [0]
        
        Input: l1 = [], l2 = []
        Output: []
        """
        ans = ListNode()
        cur = ans

        index1, index2 = l1, l2
        while index1 and index2:
            if index1.val < index2.val:
                cur.next, index1 = index1, index1.next
            else:
                cur.next, index2 = index2, index2.next
            
            cur=cur.next

        while index1:
            cur.next, index1 = index1, index1.next
            cur = cur.next
            
        while index2:
            cur.next, index2 = index2, index2.next
            cur = cur.next

        return ans.next
