class Solution(object):
    def twoSum(self, nums, target):
        list={}

        for i in range(len(nums)):
            if nums[i] not in list:
                list[target-nums[i]]=i
            else:
                return [i,list[nums[i]]]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
