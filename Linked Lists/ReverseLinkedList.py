# O(n) time | O(1) space
# Sample Input: head = 1 -> 2 -> 3 -> 4 -> 5
# Sample Output: 5 -> 4 -> 3 -> 2 -> 1
def reverseLinkedList(head):
    currentNode, previousNode = head, None
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
