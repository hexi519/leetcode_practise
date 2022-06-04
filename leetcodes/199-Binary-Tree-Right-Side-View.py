# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] bt
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def rightSideView(self, root):
        if not root: return []
        st = [[root]]

        while len(st[-1]):
            # print(f"st is :")
            # print(f"{[node.val if node else 0 for nodes in st for node in nodes ]}")

            tmp = []
            node = st[-1][-1]
            if node.right:
                # print(f"node {node.val} has right {node.right.val}")
                tmp.append(node.right)

            elif node.left:
                # print(f"node {node.val} has left {node.left.val}")
                tmp.append(node.left)

            st.append(tmp)

        # print(f"st is {st}")
        return [nodes[-1].val for nodes in st[:-1]]


if __name__ == "__main__":
    sol = Solution()

    print(f"res is {sol.rightSideView(BST)}")
    # print(f"res is {sol.rightSideView(less_skew)}")
