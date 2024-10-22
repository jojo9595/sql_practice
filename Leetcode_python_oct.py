# LC66. Plus One [Easy]
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range (len(digits)-1, -1, -1): 
            #range(len(digits)-1, -1, -1) = 反向遍历列表 
            #range() 函数生成一个序列，指定从哪里开始、在哪里结束以及步长是多少
            #len(digits)-1：从列表的最后一个元素的索引（即列表长度减 1）开始
            #-1：结束于 -1，但不包括 -1，实际上会遍历到索引 0
            #-1：步长为 -1，表示每次索引递减，即反向遍历
            if digits[i] < 9:
                digits[i] += 1
                # 如果当前数字小于9，直接加1并返回结果

                return digits
            # 如果当前是9，设置为0，继续处理前一位
            digits[i] = 0
            # 如果所有位都为9，那么处理完后会是[0,0,...,0]
            # 返回时需要在最前面加一个1
        return [1] + digits
    

# LC.724 Find Pivot Index [Easy]
def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum, rightSum = 0, sum(nums)
        for index, element in enumerate(nums):
            #每次遍历时，当前元素会被移出右边部分的和
            #因为 ele 会被放在中间的中心索引位置，不属于左边或右边的部分
            rightSum -= element
            if leftSum == rightSum:
                return index
            leftSum += element
            #如果左右两边的和不相等，将当前元素加到 leftSum 中
            #表示它现在属于左边部分，然后继续遍历下一个元素
        return -1

# LC.485 Max Consecutive Ones [Easy]
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCon = result = 0

        for number in nums:

            if number == 1:
                result += 1
                maxCon = max(maxCon, result)
            else:
                result = 0
        return maxCon
