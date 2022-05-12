# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

#TODO 回溯和dp都要做一遍，其中回溯和递归都看下，哪个复杂度更低(分别对应  和 str+'(' 的方式)
#? 上面应该说的是回溯和递归都要做一次吧
# 讲道理，效果上应该是 dp>回溯>递归

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


# bfs —> 递归层数少，效率高，但这个就只能递归，不好回溯了(也可以，就是麻烦)
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = list()

        def help_recur(left, right, StrSet):
            if left == right == 0:
                self.ans.extend(StrSet)
            tmpStrSet = []
            if left > 0:
                for strItem in StrSet:
                    tmpStrSet.append(strItem + '(')
                help_recur(left - 1, right, tmpStrSet)  # 这个其实就是递归，不是回溯了

            tmpStrSet = []
            if left < right:  #  left剩下的可选数目必须要大于right剩下的可选
                for strItem in StrSet:  # 感觉只能用递归不能用回溯欸
                    tmpStrSet.append(strItem + ')')
                help_recur(left, right - 1, tmpStrSet)

        help_recur(n, n, set([""]))
        return list(self.ans)
"""

# dfs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        >>> sol=Solution()
        >>> sol.generateParenthesis(1)
        ['()']
        >>> sol.generateParenthesis(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        """
        res = []
        cur_str = []

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str[:])
                return
            if right < left:
                return
            if left > 0:
                cur_str.append('(')
                dfs(cur_str, left - 1, right)
                cur_str.pop()

            if right > left:
                cur_str.append(')')
                dfs(cur_str, left, right - 1)
                cur_str.pop()

        dfs(cur_str, n, n)
        return [''.join(tmpStr) for tmpStr in res]
