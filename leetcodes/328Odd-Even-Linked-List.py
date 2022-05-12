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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not (head and head.next): return head
        odd_c, even_c = head, head.next
        odd_b, even_b = ListNode(next=odd_c), ListNode(next=even_c)
        # odd_b.next,cur = head,head
        while even_c.next:
            odd_c.next, odd_c = even_c.next, even_c.next
            if odd_c.next:
                even_c.next, even_c = odd_c.next, odd_c.next
            else:
                even_c.next=None
                break
            
        odd_c.next = even_b.next
        return odd_b.next

if __name__ == "__main__":
    sol = Solution()
    print(f"linkA is {linkA}")
    print(f"ans is {sol.oddEvenList(linkA)}")
