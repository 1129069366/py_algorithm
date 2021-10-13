# 1：给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 方法1 额外空间
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    result_nums = []
    for i in nums:
        if i != 0:
            result_nums.append(i)
    while(len(result_nums)<len(nums)):
        result_nums.append(0)
    return result_nums

# 方法2 快慢指针
def moveZeroes_2(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    left,right = 0,0
    while right < len(nums):
        if nums[right] != 0:
            nums[left] = nums[right]
            nums[right] = 0;
            left += 1;
        right += 1;




# 2. 盛最多水的容器 (1)暴力解法
def maxArea(height):

    """
    :type height: List[int]
    :rtype: int
    """
    max= 0
    left = 0
    while left < len(height)-1:
        right = left +1
        while right < len(height):
            minh = height[left] if height[left]<height[right] else height[right]
            max = max if max > minh*(right-left) else minh*(right-left)
            right +=  1
        left += 1
    print(max)

# 2. 盛最多水的容器 (2)快慢指针
def maxArea_2(height):

    """
    :type height: List[int]
    :rtype: int
    """
    ans= 0
    left = 0
    right = len(height)-1
    while(left < right):
        area = min(height[left],height[right])*(right-left)
        ans = max(ans,area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    print(ans)

# 3. 爬楼梯   方法1 递归
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return n
    else:
        return climbStairs(n-1)+climbStairs(n-2)


# 3. 爬楼梯   方法2 使用一个列表记录之前的值  也就是缓存思想
def climbStairs_2(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0 for i in range(n)]
    for i in range(n):
        if i<= 2:
            dp[i] = i+1
        else:
            dp[i] = dp[i-1]+dp[i-2]

    return dp[i]


print(climbStairs_2(4))









