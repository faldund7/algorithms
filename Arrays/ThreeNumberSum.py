# O(n^2) time | O(n) space
# Sample Input: array = [12, 3, 1, 2, -6, 5, -8, 6]
# Sample Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

def threeNumberSum(array, targetSum):
    array.sort()
    triples = []
    for idx in range(len(array) - 2):
        currentNum = array[idx]
        left = idx + 1
        right = len(array) - 1

        while left < right:
            currentSum = currentNum + array[left] + array[right]
            if currentSum == targetSum:
                triples.append([currentNum, array[left], array[right]])
            elif currentSum < targetSum:
                left += 1 
            elif currentSum > targetSum:
                right -= 1
    return triples
            