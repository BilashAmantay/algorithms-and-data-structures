def findFromRotatedTree(nums,target):
    n = len(nums)
    if n==0:
        return -1
    if n==1 and nums[0]==target:
        return 0
    
    low, high = 0, n-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        else:
            if nums[mid]<nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high = mid-1
            else:
                if nums[low]<=target<nums[mid]:
                    high = mid - 1
                else:
                    low = mid+1
    return -1

nums=[1]
target=0
idx = findFromRotatedTree(nums,target)
print("idx=",idx)
print(nums[idx])

nums = [2,5,6,0,0,1,2]
target = 3
idx = findFromRotatedTree(nums,target)
print("idx=",idx)
print(nums[idx])
