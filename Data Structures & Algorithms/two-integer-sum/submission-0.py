class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            k = i + 1
            for j in range(k, len(nums)):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i, k]
                else:
                    k += 1
                    continue


        