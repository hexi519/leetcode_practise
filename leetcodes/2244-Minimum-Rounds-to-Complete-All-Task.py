# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
# from loguru import logger as log


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.minimumRounds([2,2,3,3,2,4,4,4,4,4])
        4
        >>> s.minimumRounds([2,3,3])
        -1
        """
        # tasks.sort()
        """
        from collections import Counter
        cnt = Counter(tasks)
        """
        from collections import defaultdict
        cnt = defaultdict(int)
        for num in tasks:  # build hash map
            cnt[num] += 1

        res = 0
        for val in cnt.values():
            if val == 1:
                return -1
            res += val // 3 + (0 if val % 3 == 0 else 1)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
    print(s.minimumRounds([2, 3, 3]))


def getMinimal(num):
    if num % 3 == 0:
        return num / 3
    else:
        return num / 3 + 1
