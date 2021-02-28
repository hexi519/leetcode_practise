# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head and head.next and head.next:
            fast ,slow = head.next.next, head.next
        else: return None

        while fast!= slow :
            if fast and fast.next:
                fast,slow = fast.next.next, slow.next
            else: break
        
        if fast==slow:
        # if slow.next and fast.next.next: # do exit circle
            fast = head
            while fast!= slow:
                fast ,slow = fast.next, slow.next
        else:
            return None
        return fast