def minSubArrayLen(target, nums):
    nums.sort(reverse = True)
    subtotal = 0
    for i in range(len(nums)):
        subtotal += nums[i]
        if subtotal >= target:
            return i+1
        
    return 0

# Example 1:
# Input: 
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: 
target = 4
nums = [1,4,4]
print(minSubArrayLen(target, nums))
# Output: 1

# Example 3:
# Input: 
target = 11
nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(target, nums))
# Output: 0

