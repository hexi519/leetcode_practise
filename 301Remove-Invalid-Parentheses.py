# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

# 我自己下面写的那个版本太suck了。虽然大家都是BFS,但是我的时空分别是5%和5%
# 这个思想更优的原因是，真正理解了BFS的精髓-->找准什么是实在的递归依据(要删除的符号个数，而我的是curIndex，所以我的层数就会比他多好多...)
class Solution:
    def removeInvalidParentheses(self, chars: str) -> List[str]:
        """
        >>> sol = Solution()
        >>> sol.removeInvalidParentheses('))()((')
        ['()']
        >>> sol.removeInvalidParentheses("(a)())()")
        ['(a())()', '(a)()()']
        """
        def isValid(s:str)->bool:
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level

class Solution:
    def removeInvalidParentheses(self, chars: str) -> List[str]:
        self.ans = set()

        def unvalid(curStr,test = True):
            left, right = 0, 0
            for char in curStr:
                if char == '(':
                    left += 1  # 不合法的left
                if char == ')':
                    if left > 0:
                        left -= 1
                    else:  # 不合法的right
                        right += 1
                        if test:
                            return 1, 1
            return left, right  # 递归的时候

        def helpRemove(proQueue):  # processQueue # 当前剩的，下一个要处理的位置，还剩删除的
            tmpQueue = []
            for curStr, curIndex, left, right in proQueue:
                if left == right == 0:
                    if sum(unvalid(curStr)) == 0:
                        self.ans.add(curStr[:])
                        # log.info(f"add {curStr}")
                    continue

                if curIndex >= len(curStr) or left + right > len(curStr):  # 两种剪纸情况
                    continue

                if left + right <= len(curStr):
                    tmpQueue.append((curStr, curIndex + 1, left, right))
                if curStr[curIndex] == "(":
                    tmpQueue.append((curStr[:curIndex] + curStr[curIndex + 1:], curIndex, left - 1, right))
                elif curStr[curIndex] == ")":
                    tmpQueue.append((curStr[:curIndex] + curStr[curIndex + 1:], curIndex, left, right - 1))

            if len(tmpQueue):
                helpRemove(tmpQueue)

        left, right = unvalid(chars,False)
        helpRemove([(chars, 0, left, right)])

        return list(self.ans)
