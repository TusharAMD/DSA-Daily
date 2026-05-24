class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                pivot=i-1
                break
        print(pivot)

        if pivot==-1:
            nums.sort()
        else:

            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[pivot]:
                    tmp = nums[i]
                    nums[i] = nums[pivot]
                    nums[pivot] = tmp
                    break
            left = pivot+1
            right = len(nums)-1
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1