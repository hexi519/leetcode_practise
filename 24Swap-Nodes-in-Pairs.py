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
    # recursive
    def swapPairs(self, head: ListNode) -> ListNode:
        # 可以写成有返回值的，也可以写成没有返回值的
        def recur(prev: ListNode):  # 传进来的是prev,保证了不为None
            if prev.next and prev.next.next:
                cur, curN = prev.next, prev.next.next
                prev.next, cur.next, curN.next = curN, curN.next, cur
                recur(cur)

        ans=ListNode(next=head)
        recur(ans)
        return ans.next

    # iterasive
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        ans = ListNode(next=head)
        prev, cur, curN = ans, head, None
        while cur and cur.next:
            curN = cur.next
            prev.next, cur.next, curN.next = curN, curN.next, cur
            prev, cur = cur, cur.next

        return ans.next


if __name__ == "__main__":
    sol = Solution()
    print(f"linkA is {linkA}")
    print(f"ans is {sol.swapPairs(linkA)}")