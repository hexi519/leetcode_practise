# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [dp] 01
'''

from typing import Dict, List
from util import *



# state number,good number [sn,gn] 


def Solution(sn,gn,info):
    """
    >>> info = [[71,100],[69,1],[1,2]]
    >>> Solution(70,3,info)
    3
    >>> info = [[79,83],[58,14],[86,54],[11,79],[28,72],[62,52],[15,48],[68,62]]
    >>> Solution(200,8,info)
    334
    """
    # process input
    v,w =[ [None]*(gn+1) for _ in range(2) ]
    for index in range(1,gn+1):
        w[index],v[index] = info[index-1]
    
    # dp initialize  
    # dp = [ [0]*(sn+1) for _ in range(gn+1) ]
    dp = [0]*(sn+1 ) # 滚动数组优化空间 【优化1】
    
    # Format1 
    """
    def ZeroPack( value ,weight ,dp):
        # 其实应该是max(weight,1),但是考虑到range左开右闭的特性，就得在这个基础上全部减1
        for state in range(max( weight,1),sn+1)[::-1]:  
            dp[state] = max(dp[state],dp[state-weight]+value)

    for good in range( 1, gn+1 ):
        ZeroPack(v[good],w[good],dp)
    """

    # Format2【优化2】可以参照[这个解析](https://nmslqwq.blog.luogu.org/solution-p1048)里面的优化2，解释得很好
    # 但是考虑到优化2的话，就不能采用子函数的形式了，不然要传递的参数就更多了
    # 其实应该是max(weight,1),但是考虑到range左开右闭的特性，就得在这个基础上全部减1
    for good in range( 1, gn+1 ):
        weight,value = w[good] ,v[good]
        for state in range(max( weight,1,sn-sum(w[good:])),sn+1)[::-1]:
            dp[state] = max(dp[state],dp[state-weight]+value)

    return max(dp)


""" luogu version

def Solution(): 
    # process input
    sn,gn= map(int,input().split())
    v,w =[ [None]*(gn+1) for _ in range(2) ]
    for index in range(1,gn+1):
        w[index],v[index] = map(int,input().split())
    
    # dp process
    ## initialize  
    # dp = [ [0]*(sn+1) for _ in range(gn+1) ]
    dp = [0]*(sn+1 ) # 滚动数组优化空间 【优化1】
    
    # Format1 
    def ZeroPack( value ,weight ,dp):
        # 其实应该是max(weight,1),但是考虑到range左开右闭的特性，就得在这个基础上全部减1
        for state in range(max( weight,1),sn+1)[::-1]:  
            dp[state] = max(dp[state],dp[state-weight]+value)

    for good in range( 1, gn+1 ):
        ZeroPack(v[good],w[good],dp)

    # Format2【优化2】可以参照[这个解析](https://nmslqwq.blog.luogu.org/solution-p1048)里面的优化2，解释得很好
    # 但是考虑到优化2的话，就不能采用子函数的形式了，不然要传递的参数就更多了
    for good in range( 1, gn+1 ):
        weight,value = w[good] ,v[good]
        for state in range(max( weight,1,sn-sum(w[good:])),sn+1)[::-1]:
            dp[state] = max(dp[state],dp[state-weight]+value)

    return max(dp)


if __name__ == "__main__":
    info = [[71,100],[69,1],[1,2]]
    # print(Solution(70,3,info))
    print(Solution())
"""