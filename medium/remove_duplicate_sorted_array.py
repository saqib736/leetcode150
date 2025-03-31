class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[p-2]:
                nums[p] = nums[i]
                p += 1
        return p 