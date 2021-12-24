# O(n) time | O(1) space
# Sample Input: n = 6
# Sample Output: 5 // 0, 1, 1, 2, 3, 5

def getNthFib(n):
    firstNum = 0
    secondNum = 1
    nextSum = 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(n-2):
        nextNum = firstNum + secondNum
        firstNum = secondNum 
        secondNum = nextNum
    return nextNum