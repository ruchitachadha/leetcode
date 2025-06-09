class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        int_arr = []
        for n in nums1:
            if n in nums2 and n not in int_arr:
                int_arr.append(n)
        return int_arr
