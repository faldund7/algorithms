# O(n) time | O(n) space
# Sample Input: array = [3, 5, -4, 8, 11, 1, -1, 6]
# Sample Output: [-1, 11]

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        requiredNum = targetSum - num
        if requiredNum in nums:
            return [requiredNum, nums]
        else:
            nums[num] = True
    return []