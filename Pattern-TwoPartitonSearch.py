"""
* refer:[labuladong的算法](https://labuladong.gitbook.io/algo/bi-du-wen-zhang/er-fen-cha-zhao-xiang-jie)
* 查找边界的模板分两种 -- 上边界和下边界 
    * 左闭右闭的模板比较好记，所以这里采用左闭右闭上
    * python也有自带的二分查找函数 bisect库
* 查找某个数 和 查找边界 的模板任意一个 是可以并在一起的
"""

class Solution():
    def bisect_left(self, nums, target):
        """
        查找下边界: 寻找尽量靠前的可以插入的地方  0<=res<=len(nums)
            1. 如果nums中有target，那么就应该返回(插入到)多个相同的target中的最左侧的位置
            2. 如果nums中没有target，那么就应该返回(插入到)第一个比target大的元素的位置
        >>> s = Solution()
        >>> s.bisect_left([1,2,2,2,4,4,5],2)
        1
        >>> s.bisect_left([1,2,2,2,4,4,5],3)
        4
        >>> s.bisect_left([1,2,2,2,4,4,5],7)
        7
        >>> s.bisect_left([1,2,2,2,4,4,5],0)
        0
        """
        left, right = 0, len(nums)
        if right == 0: return -1  # 数组为空的时候返回-1
        while (left < right):  # 其实下面的三种情况可以合并成两种，但是为了思路清晰
            mid = (left + right) // 2  # C++需要这么写：mid = left + (right - left) // 2, 但是python的int无限大就不需要
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:  # target == nums[mid]
                right = mid
        return left # 返回left还是right都一样，反正退出条件就是二者相等

    def bisect_right(self, nums, target):
        """
        查找上边界: 最小的大于target的数的下标。 0<=res<=len(nums)
            无论nums中是否有target这个元素，都返回第一个比target大的元素的位置
        >>> s = Solution()
        >>> s.bisect_right([1,2,2,2,4,4,5],2)
        4
        >>> s.bisect_right([1,2,2,2,4,4,5],3)
        4
        >>> s.bisect_right([1,2,2,2,4,4,5],0)
        0
        """
        left, right = 0, len(nums)
        if right == 0: return -1  # 数组为空的时候返回-1
        while (left < right):  # 其实下面的三种情况可以合并成两种，但是为了思路清晰
            mid = (left + right) // 2  # C++需要这么写：mid = left + (right - left) // 2, 但是python的int无限大就不需要
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:  # target == nums[mid]
                left = mid + 1

        return left # 返回left还是right都一样，反正退出条件就是二者相等


"""
小总结：
* 对比binarySerach_left 和 binarySerach_right, 记忆的方式就是：
    * 区别
        找lower-bound，那么即使nums[mid]和target相等，也要向左缩紧区间(移动right向左)；
        找upper-bound，那么即使nums[mid]和target相等，也要向右缩紧区间(移动left向左)
    * 相同，但需要注意的细节点
        缩紧区间的时候分别是right=mid-1 和 left=mid+1,这样是因为mid已经搜寻过了，且我们是左闭右闭，所以新的搜索范围要剔除mid
        但是由于即使相等，我们还是会缩紧区间(同时会剔除掉mid)
"""