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

# dalao: from bottom to up
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next


# hesy: from up to bottom
class Solution(object):
    def sortList(self, head):
        # end case
        if (not head) or (not head.next):
            return head

        dummy = ListNode(next=head)
        slow, fast = dummy, dummy  #* must initialize like this, or things will go wrong
        # find the middle
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        lh, rh, slow.next = dummy.next, slow.next, None  # set slow.next to be none, otherwise will keep sort
        lh = self.sortList(lh)
        rh = self.sortList(rh)
        cur = dummy
        while lh and rh:  # merge sorted
            if lh.val < rh.val:
                cur.next,lh = lh,lh.next
            else:
                cur.next,rh = rh,rh.next
            
            cur = cur.next

        cur.next = lh if lh else rh

        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    print(f"before input is {linkA}")
    print(sol.sortList(linkA))
    