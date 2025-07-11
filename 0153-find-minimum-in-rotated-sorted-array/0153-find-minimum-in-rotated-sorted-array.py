class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        Min=float("inf")
        while(low<=high):
            mid=(low+high)//2
            if(nums[low]<=nums[mid]):
                if(nums[low]<Min):
                    Min=nums[low]
                low=mid+1
            if(nums[mid]<=nums[high]):
                if(nums[mid]<Min):
                    Min=nums[mid]
                high=mid-1
        return Min
        