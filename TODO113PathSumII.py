# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]113PathSumII: find all paths from root to leaf whose sum is equal to a given number and return
'''

from typing import Dict, List
from util import *

"""
跟112不一样的是，这里要返回所有的路径，所以iteration能够早停的优势就没有了。
"""
class Solution:
    """
    >>> sol = Solution()
    >>> sol.pathSum(s,8)
    [[3, 4, 1], [3, 5]]
    >>> sol.pathSum(s,7)
    []
    >>> sol.pathSum(s,15)
    []
    """
    # iteration
    """
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # TODO recursive函数中的参数，全部要声明参数在循环中改变（废话，参数是必须的，只不过是传递方式不同，一个用局部变量，一个当作函数参数）
        res,pathAlong,allSum = [],[],0
        status = [ (root , pathAlong ,0) ]  # curNode
        while len(status):
            #* 1) pop(get current node) and boundary conditions (NULL)
            curNode , path , pathSum =  status.pop()
            if curNode :
                #* 2) change parameters
                path_ = path.copy()
                path_.append(curNode.val)
                pathSum += curNode.val
                
                #* 3) 每一步都要做的判断 
                if pathSum==sum and (not curNode.left ) and (not curNode.right ):
                    res.append( path_ )

                #* 4) push for iterasive 
                status.append( ( curNode.left ,path_ ,pathSum )   )    
                status.append( ( curNode.right ,path_ ,pathSum )   )    

        return res
    
    #! iteration 我的方法的优化
    # 优化点：传引用的破解 与 避免
    # 下面的分析中我们会看到，arr+[node.val]其实会增大空间开销(每次都在create a new list),但是我们的方法比使用pop()的递归方法的空间开销还是小，循环的优越性！

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
	if not root:
		return []
	arr = []
	stack = [(root, sum, arr)]
	res = []
	while stack:
		node, s, arr = stack.pop()
		if not node:
			continue
		elif node.val==s and not node.left and not node.right:
            #TODO 这里用arr+[node.val]的方法，完美避开了python传引用的问题 --> 自动复制
			res.append(arr+[node.val])
		else:
            #* 这里用arr+[node.val]的方法，完美避开了python传引用的问题 --> 自动复制
			stack.append((node.left, s-node.val, arr+[node.val]))
			stack.append((node.right, s-node.val, arr+[node.val]))
		
	return res
    """

    # TODO 这里写了paradigm
    """
    * 其实从这里也可以看出来，recursion和iteration的一个区别就是，前者一般还需要一个助手函数(除非不需要传递额外参数)，后者不需要
    * 写recursive之前想清楚1.返回值是否需要Bool，不需要的话就用void，这点想清楚之后就直接按照四个步骤来就行 （不需要bool返回值的情况也可以强行写成bool，但是你发现这个返回值没有用的时候就可以修改为void了）
    """
    # recursive
    """
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res,pathAlong = [],[]

        def preTraverse(root,sum,pathAlong,pathSum,res):
            #* 0) 考虑 a. 返回值(是否为bool) b. 要传递和修改什么参数
            #* 1) Boundary conditions(NULL)
            if not root:
                return
            #* 2) change parameters 对要传递的参数进行修改，所有在参数列表中的都要变动(除了标杆sum)
            pathSum +=root.val
            pathAlong.append(root.val)

            #* 3) 每一步都要做的判断 
            if pathSum==sum and (not root.left) and (not root.right) :
                # TODO python的引用和传递真的要小心...
                # TODO 另一种方式就是res.append( list(pathAlong) )
                res.append(pathAlong.copy())
            
            #* 4) recursive and 善后工作 for backtrack
            preTraverse( root.left ,sum ,pathAlong,pathSum,res)            
            preTraverse( root.right,sum ,pathAlong,pathSum,res)    
            
            pathAlong.pop() 

        preTraverse( root ,sum ,pathAlong,0,res )
        return res
        """        
    
    #! recursive 我的方法的优化
    # 代码改进点:   1. 使用sum-node.val的方式，节省了一个参数的传递
    #           2. pathAlong + [root.val]的方式避免了python参数传引用的问题
    # 但是整体空间变大了，估计是pathAlong + [root.val]需要更多内存？
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = [ ] 
        # 0) 考虑传递的参数 & 返回值的形势（函数的外观）
        
        def preTraverse(root,sum,pathAlong,res):
            # 1） 边界条件
            if not root:
                return
            # 3) 判断条件
            if root.val == sum and (not root.left ) and (not root.right ):
                res.append( pathAlong + [root.val] ) 
            
            # 2) 4)  修改参数 & recursive融为一体了
            preTraverse(root.left,sum-root.val,pathAlong + [root.val],res)
            preTraverse(root.right,sum-root.val,pathAlong + [root.val],res)
            

        preTraverse(root,sum,[],res)
        return res
    
    #! recursive 最优化
    # 代码改进点:   结合了第一版和第二版，仅仅在res.append的时候进行浅拷贝，其余的时候都不用浅拷贝 ( 空间开销介于第一版和第二版之间 )
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = [ ] 
        # 0) 考虑传递的参数 & 返回值的形势（函数的外观）
        
        def preTraverse(root,sum,pathAlong,res):
            # 1） 边界条件
            if not root:
                return
            
            # 2) 修改参数
            pathAlong.append(root.val)
            # 3) 判断条件
            if root.val == sum and (not root.left ) and (not root.right ):
                # TODO pathAlong[:] , list(pathAlong) , pathAlong.copy() 都能实现浅拷贝
                res.append( pathAlong[:] ) 
            
            # 2) 4)  修改参数 & recursive
            preTraverse(root.left,sum-root.val,pathAlong ,res)
            preTraverse(root.right,sum-root.val,pathAlong,res)
            
            # for backtrack
            pathAlong.pop()
            

        preTraverse(root,sum,[],res)
        return res


    """
    TODO: 请注意，我这里其实都是DFS(无论是iteration还是recursion)，只不过我都是 前-右-左 的顺序在访问，如果想要 前-左-中 的顺序当然可以，就是入栈的时候先压入右边再压入左边。
    
    另一方面，BFS做当然也可以，但是得用iterative & queue 实现 （为什么可以--》因为在queue中我们会把当前的所有情况都一起传递进去）
    """
    
    # 这个总结的最好，所有的都写了，包括我上面提到的几个优化：https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack
