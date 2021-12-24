# O(nlogn) time | O(1) space
# Sample Input: array = [5, 7, 1, 1, 2, 3, 22]
# Sample Output: 20

def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for value in coins:
        if value > currentChange + 1:
            return currentChange + 1
        else:
            currentChange += value
    return currentChange + 1