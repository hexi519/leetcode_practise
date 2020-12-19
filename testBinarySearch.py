from typing import Dict, List


class Solution:
    # 找target, 如果存在多个，返回最左边的，否则返回-1。 左闭右开的写法
    def testBinarySearch_LeftNoBigger1(self, nums: List, target: int) -> int:
        """
        >>> s = Solution()
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,5],3)
        1
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,5],1)
        0
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,5],0)
        -1
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,7],9)
        -1
        """
        # [left,right)
        length = len(nums)
        left, right = 0, length
        mid = left + (right - left) // 2
        while left < right:  # 退出条件是left==right,因为right是已经搜过/不可取到的值，所以此时就意味着可以全部搜完了
            if nums[mid] == target:
                right = mid  # 先不急着返回，范围向左缩紧。如果只有一个target，最后退出的时候left==right，然后还返回left，还是相当于找到了
            else:
                left, right = (mid + 1, right) if nums[mid] < target else (left, mid)
            mid = left + (right - left) // 2
        """ 考虑不存在target出界的情况
            1. target>all ：此时left==len
            2. target<all : 此时nums[target]==left,因为left取值就只有[0,length],所以target<all、没找到target，也还是会返回一个0
        """
        if left == length or target != nums[left]: return -1

        return left

    # 找target, 如果存在多个，返回最左边的，否则返回-1。 左闭右闭的写法
    def testBinarySearch_LeftNoBigger2(self, nums: List, target: int) -> int:
        """
        >>> s = Solution()  
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,5],3)
        1
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,5],1)
        0
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,5],0)
        -1
        >>> s.testBinarySearch_LeftNoBigger1([1,3,3,3,7],9)
        -1
        """
        # [left,right]
        length = len(nums)
        left, right = 0, length - 1
        mid = left + (right - left) // 2
        while left <= right:  # 退出条件就是left=right+1,此时能确保所有的元素都被搜到了。如果是left<right，当只剩一个元素，也就是left==right的时候，那个元素就会被漏掉了。
            if nums[mid] == target:
                right = mid - 1  # 先不急着返回，范围向左缩紧。如果只有一个target，最后退出的时候left==right，然后还返回left，还是相当于找到了
            else:
                left, right = (mid + 1, right) if nums[mid] < target else (left, mid - 1)
            mid = left + (right - left) // 2
        """ 考虑不存在target出界的情况
            1. target>all ：此时left==len
            2. target<all : 此时nums[target]==left,因为left取值就只有[0,length],所以target<all、没找到target，也还是会返回一个0
        """
        #* 可以看到左开右闭还是左闭右开，最后这个越界的判断条件都是一样的
        if left == length or target != nums[left]: return -1

        return left

    # 找target, 如果存在多个，返回最左边的，否则返回-1。 左闭右开的写法。【这种写法确实比较难】
    def testBinarySearch_RightNoSmaller1(self, nums: List, target: int) -> int:
        """
        >>> s = Solution()
        >>> s.testBinarySearch_RightNoSmaller1([1,3,3,3,5],3)
        3
        >>> s.testBinarySearch_RightNoSmaller1([1,3,3,3,5],1)
        0
        >>> s.testBinarySearch_RightNoSmaller1([1,3,3,3,5],0)
        -1
        >>> s.testBinarySearch_RightNoSmaller1([1,3,3,3,7],7)
        4
        >>> s.testBinarySearch_RightNoSmaller1([1,3,3,3,7],9)
        -1
        """
        # [left,right)
        length = len(nums)
        left, right = 0, length
        mid = left + (right - left) // 2
        while left < right:  # 退出条件是left==right,因为right是已经搜过/不可取到的值，所以此时就意味着可以全部搜完了
            if nums[mid] == target: left = mid + 1  # mid搜过了，左闭，所以应该是left=mid+1
            else:
                left, right = (mid + 1, right) if nums[mid] < target else (left, mid)
            mid = left + (right - left) // 2
        """ 考虑不存在target出界的情况
            1. target>all ：此时left==len
            2. target<all : 此时nums[target]==left,因为left取值就只有[0,length],所以target<all、没找到target，也还是会返回一个0
        """
        if left == length: return left - 1 if target == nums[left - 1] else -1

        return left - 1

    # 找target, 如果存在多个，返回最左边的，否则返回-1。 左闭右闭的写法。
    def testBinarySearch_RightNoSmaller2(self, nums: List, target: int) -> int:
        """
        >>> s = Solution()
        >>> s.testBinarySearch_RightNoSmaller2([1,3,3,3,5],3)
        3
        >>> s.testBinarySearch_RightNoSmaller2([1,3,3,3,5],1)
        0
        >>> s.testBinarySearch_RightNoSmaller2([1,3,3,3,5],0)
        -1
        >>> s.testBinarySearch_RightNoSmaller2([1,3,3,3,7],7)
        4
        >>> s.testBinarySearch_RightNoSmaller2([1,3,3,3,7],9)
        -1
        """
        # [left,right]
        length = len(nums)
        left, right = 0, length - 1
        mid = left + (right - left) // 2
        while left <= right:  # 退出条件是left==right,因为right是已经搜过/不可取到的值，所以此时就意味着可以全部搜完了
            if nums[mid] == target: left = mid + 1  # mid搜过了，左闭，所以应该是left=mid+1
            else:
                left, right = (mid + 1, right) if nums[mid] < target else (left, mid - 1)
            mid = left + (right - left) // 2
        """ 考虑不存在target出界的情况
            1. target>all ：此时right==length，left出界。需要和target==max(all)，也就是target正好在最右边的情况作区分.
            2. target<all : 此时由于mid一直大于target，所以一直是right向左边缩减，所以只可能是right出界
        """
        if right < 0 or nums[right]!=target: return -1

        return left - 1
