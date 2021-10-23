# O(n) time | O(1) space
# Assume the LinkedList is sorted
# Sample Input: linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
# Sample Output: 1 -> 3 -> 4 -> 5 -> 6
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
    return linkedList



