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
    # iterasive
    def reverseList(self, head: ListNode) -> ListNode:
        """
        [3,4,5]   
                   cur                      cur
        dummy->None 3->4->5  dummy->1->None  3->4
        """
        cur = head
        dummy = ListNode()
        while cur:
            log.info(f"cur is {cur.val}")
            log.info(f"\tcur.next is {cur.next.val if cur.next else None}")
            log.info(f"\tdummy.next is {dummy.next.val if dummy.next else None}")
            dummy.next, cur, cur.next = cur, cur.next, dummy.next
            print(dummy)
            print(cur)

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(f"ori chain is {linkA}")
    print(f"ans is {sol.reverseList(linkA)}")