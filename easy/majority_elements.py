class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        count = 0
        for i in nums:
            if count == 0:
                p = i
            if i == p:
                count += 1
            else:
                count -= 1
        return p 