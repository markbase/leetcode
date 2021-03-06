class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data_map = {}
        for k, v in enumerate(nums):
            data_map[target - v] = k
        for i in range(len(nums)):
            if (nums[i] in data_map.keys()) and data_map[nums[i]] != i:
                return [i, data_map[nums[i]]]
                