# O(nlogn) time | O(1) space
# Sample Input: array = [2, 3, 1, -4, -4, 2]
# Sample Output: True

def hasSingleCycle(array):
	numElementsVisited = 0
	currentIdx = 0
	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		numElementsVisited += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == 0

def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)

# Note: Conditions: 
# 1. The element at index 0 cannot be jumped through more than once in one 
# pass
# 2. (n + 1)th element you jump through should be the first element