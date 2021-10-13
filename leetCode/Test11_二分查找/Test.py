
# 1. (二分查找)给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i

    # return -1
    low,high = 0,len(nums)-1
    while low <= high:
        middle = (high - low) // 2 + low
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            high = middle -1
        else:
            low = middle + 1

    return -1


# 2.搜索插入位置
def searchInsert(nums, target):
    low,high,res = 0,len(nums)-1,len(nums)
    while(low <= high):
        middle = (high - low)//2 + low
        if(target <= nums[middle]):
            res = middle
            high = middle-1
        else:
            low = middle + 1;
    return res

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(searchInsert(nums, target))




























