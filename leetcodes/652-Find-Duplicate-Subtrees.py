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

from collections import defaultdict


class Solution:
    tupleDict = defaultdict(int)
    res = []

    def findDuplicateSubtrees(self, root):
        self.res = []
        self.postTraverse(root)
        return self.res

    def postTraverse(self, root):
        if not root:
            return None

        left = self.postTraverse(root.left)
        right = self.postTraverse(root.right)
        # print(f"root is {root.val}")
        # print(f"\tleft is {left.val if left else 'None'}")
        # print(f"\tright is {right.val if right else 'None'}")

        # curTuple = f"{str(root.val)}"  #",".join([str(root.val), str(left.val) if left else "", str(right.val) if right else ""])
        curTuple = [root]  #",".join([str(root.val), str(left.val) if left else "", str(right.val) if right else ""])
        if left:
            # curTuple += f",{left.val}"
            curTuple.append(left)

        if right:
            # curTuple += f",{right.val}"
            curTuple.append(right)

        curStr = ','.join([str(node.val) for node in curTuple])

        if self.tupleDict[curStr] == 1:
            # self.res.append(curTuple)
            # self.res.append([curTuple[0]])
            self.res.append(curTuple[0])

        self.tupleDict[curStr] += 1
        # print(f"\ttupleDict is {self.tupleDict}")
        # print(f"\tres is {self.res}")

        # print(f"\troot to return is {root.val}")
        return root


class Solution(object):
    # from https://leetcode.cn/problems/find-duplicate-subtrees/solution/xun-zhao-zhong-fu-de-zi-shu-by-leetcode/, 绝了
    # 再看下Stephen的这个 https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left, root.right.right = TreeNode(2), TreeNode(4)
    root.right.left.left = TreeNode(4)

    root = TreeNode(2)
    root.left, root.right = TreeNode(1), TreeNode(1)

    root = TreeNode(0)
    root.left, root.right = TreeNode(0), TreeNode(0)
    root.left.left, root.left.right = TreeNode(0), TreeNode(0)
    root.left.left.left = TreeNode(0)

    preTraverse(root)
    print()

    results = sol.findDuplicateSubtrees(root)
    for node in results:
        preTraverse(node)
        print()
    # print(f"{[node.val for node in results]}")

    # print(f"results is {results}")
