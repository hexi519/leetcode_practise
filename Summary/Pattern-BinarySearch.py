"""
* refer:[labuladong的算法](https://labuladong.gitbook.io/algo/bi-du-wen-zhang/er-fen-cha-zhao-xiang-jie)
* 查找边界的模板分两种 -- 上边界和下边界 
    * 左闭右开的模板比较好记，所以这里采用左闭右开
    * python也有自带的二分查找函数 bisect库
* 查找某个数 和 查找边界 的模板任意一个 是可以并在一起的 (下文中的bisect是和bisect_right合并的)
* 采用左闭右开的形式和采用left<right不是绑定起来的 [可以看下153题，left<right和左闭右闭绑定起来的] 。left<right和left<=right的区别主要在于后者在循环内部的判断会更多，且会从循环内部判断后直接返回结果。前者是退出后返回结果。虽然前者early stop，但是结束的会更慢，因为判断更多了。
"""


class Solution():
    def bisect_left(self, nums, target):
        """
        查找下边界: 寻找尽量靠前的可以插入的地方  0<=res<=len(nums)
            1. 如果nums中有target，那么就应该返回(插入到)多个相同的target中的最左侧的位置
            2. 如果nums中没有target，那么就应该返回(插入到)第一个比target大的元素的位置
            综上，返回第一个不比target小的元素的位置以供插入
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
        if right == 0:
            return -1  # 数组为空的时候返回-1
        while (left < right):  # 其实下面的三种情况可以合并成两种，但是为了思路清晰
            # C++需要这么写：mid = left + (right - left) // 2, 但是python的int无限大就不需要
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:  # target == nums[mid]
                right = mid
        return left  # 返回left还是right都一样，反正退出条件就是二者相等

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
        if right == 0:
            return -1  # 数组为空的时候返回-1
        while (left < right):  # 其实下面的三种情况可以合并成两种，但是为了思路清晰
            # C++需要这么写：mid = left + (right - left) // 2, 但是python的int无限大就不需要
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:  # target == nums[mid]
                left = mid + 1

        return left  # 返回left还是right都一样，反正退出条件就是二者相等

    def bisect(self, nums, target):
        """
        查找上边界: 最小的大于target的数的下标。 0<=res<=len(nums)
            无论nums中是否有target这个元素，都返回第一个比target大的元素的位置
        >>> s = Solution()
        >>> s.bisect([1,2,2,2,4,4,5],2)
        4
        >>> s.bisect([1,2,2,2,4,4,5],3)
        -1
        >>> s.bisect([1,2,2,2,4,4,5],0)
        -1
        """
        left, right = 0, len(nums)
        if right == 0:
            return -1  # 数组为空的时候返回-1
        while (left < right):  # 其实下面的三种情况可以合并成两种，但是为了思路清晰
            # C++需要这么写：mid = left + (right - left) // 2, 但是python的int无限大就不需要
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:  # target == nums[mid]
                left = mid + 1

        # * 查找边界和查找具体某个数 只要对结果加一个判断即可
        # 之所以是left-1是因为默认找的是右边界. 前面left==0说明第一个比target大的居然是头一个元素，也就是说没找到呗
        if left == 0 or nums[left-1] != target:
            return -1

        return left  # 返回left还是right都一样，反正退出条件就是二者相等


"""
小总结：
* 对比binarySerach_left 和 binarySerach_right, 记忆的方式就是：
    * 区别
        找lower-bound，那么即使nums[mid]和target相等，也要向左缩紧区间(移动right向左)；
        找upper-bound，那么即使nums[mid]和target相等，也要向右缩紧区间(移动left向左)
    * 相同，但需要注意的细节点
        缩紧区间的时候分别是right=mid 和 left=mid+1,这样是因为mid已经搜寻过了，且我们是左闭右凯，所以新的搜索范围要剔除mid
        但是由于即使相等，我们还是会缩紧区间(同时会剔除掉mid)
"""
