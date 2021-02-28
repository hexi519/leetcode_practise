<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

class Solution:
    def numberOfArithmeticSlices(self, A):
        size_ = len(A)
        if size_ <3 :return 0
        ans,cur_substring  = 0,0
        for i in range(2,size_):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                cur_substring+=1      # 在前面的基础上+1。为何是+1，可以简单想一下
            else:
                cur_substring=0
            ans+=cur_substring
        return ans
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

class Solution:
    def numberOfArithmeticSlices(self, A):
        size_ = len(A)
        if size_ <3 :return 0
        ans,cur_substring  = 0,0
        for i in range(2,size_):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                cur_substring+=1      # 在前面的基础上+1。为何是+1，可以简单想一下
            else:
                cur_substring=0
            ans+=cur_substring
        return ans
>>>>>>> hesy/master
