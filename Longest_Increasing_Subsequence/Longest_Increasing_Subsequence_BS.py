#Time_Complexity: O(Nlogn)
#Space_Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        dp[0] = nums[0]
        dpLength = 0
        for i in range(n):
            if (nums[i] > dp[dpLength]):
                dp[dpLength+1] = nums[i]
                dpLength+=1

            else:
                nextI = self.binarySearch(dp, dpLength, nums[i])
                dp[nextI] = nums[i]

        return dpLength+1


    def binarySearch(self, nums, high, target):
        low = 0
        high = high

        while low <= high:
            mid = low+(high-low)//2
            if (nums[mid] == target):
                return mid
            if nums[mid] < target:
                low = mid+1

            else:
                high = mid-1

        return low
