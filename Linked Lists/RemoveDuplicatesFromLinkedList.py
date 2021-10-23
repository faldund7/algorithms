# O(n) time | O(1) space
# Assume the LinkedList is sorted
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
    return linkedList



