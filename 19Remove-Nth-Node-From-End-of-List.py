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


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        [1,2,3,4,5],2-->[1,2,3,5]
        [1],1-->[]
        """
        dummy, fast = ListNode(next=head), head
        slow = dummy
        n -= 1
        while n:
            fast = fast.next
            n -= 1

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    print(f"ans is {sol.removeNthFromEnd(linkA, 4)}")
