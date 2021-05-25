# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        index1, index2 = l1, l2
        value = 0
        dummy = ListNode()
        cur = dummy
        while index1 or index2 or value:
            if index1:
                value += index1.val
                index1 = index1.next
            if index2:
                value += index2.val
                index2 = index2.next
            cur.next = ListNode(value % 10)
            value = value // 10
            cur = cur.next
        return dummy.next