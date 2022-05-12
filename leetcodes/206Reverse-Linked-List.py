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
    # 我这个插入的方法不是很主流，每次要修改三根link，主流的每次只要修改1次，所以我的时间复杂度比较高
    def reverseList(self, head: ListNode) -> ListNode:
        """
        [3,4,5]    cur                         cur
                    V                           V
        dummy->None 3->4->5->6  dummy->3->None  4->5->6
        """
        cur = head
        dummy = ListNode()
        while cur:
            dummy.next, cur.next ,cur = cur, dummy.next,cur.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(f"ori chain is {linkA}")
    print(f"ans is {sol.reverseList(linkA)}")