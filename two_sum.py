class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in num_map.keys() and num_map[temp]!=i:
                return [i,num_map[temp]]
        return []
