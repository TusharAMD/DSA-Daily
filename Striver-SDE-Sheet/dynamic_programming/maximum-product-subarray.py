class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin=1
        currMax=1

        for ele in nums:

            tmp = currMax
            currMax = max(ele*currMax,ele*currMin,ele)
            currMin = min(ele*tmp,ele*currMin,ele)

            res = max(currMax,res)
        return max(currMax,res)