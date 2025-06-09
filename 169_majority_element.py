class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        max_count = 0
        max_key = None
        for key,value in counter.items():
            if value > max_count:
                max_key = key
                max_count = value
        return max_key 

