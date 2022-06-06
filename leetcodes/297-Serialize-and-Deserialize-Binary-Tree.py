# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] bt
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Codec:
    idx = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'N#'

        strs = f"{root.val}#"
        strL = self.serialize(root.left)
        strR = self.serialize(root.right)
        strs += strL + strR

        return strs

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            raise ValueError("len(data) is 0")

        nextIdx = self.getEndIdx(data)
        if data[self.idx:nextIdx] == 'N':
            self.idx = nextIdx + 1
            return None

        root = TreeNode(int(data[self.idx:nextIdx]))
        self.idx = nextIdx + 1

        left = self.deserialize(data)
        right = self.deserialize(data)
        root.left = left
        root.right = right

        return root

    def getEndIdx(self, strs):
        idx = self.idx
        while idx < len(strs):
            idx += 1
            if strs[idx] == '#':
                return idx

        raise ValueError(f"# not found when self.idx is {self.idx}")


if __name__ == "__main__":
    sol = Codec()
    # strs = sol.serialize(BST_)
    # strs = sol.serialize(BST)
    strs = sol.serialize(skew)
    print(f"strs is {strs}")
    preTraverse(sol.deserialize(strs))