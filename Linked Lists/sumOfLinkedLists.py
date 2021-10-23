# O(max(m, n)) time | O(max(m, n)) space
# Assume the LinkedList is sorted
# Sample Input: linkedListOne = 2 -> 4 -> 7 -> 1 | linkedListTwo = 9 -> 4 -> 5 (1742 + 549)
# Sample Output: 1 -> 9 -> 2 -> 2 (2291) (This has to be a new LinkedList)
# (Note: 2, 9, 1 are called the Least Significant Digit of the Integer)

class LinkedList:
    def __init__(self):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    NewLinkedList = LinkedList(0)
    currentNode = NewLinkedList
    carry = 0

    nodeOne, nodeTwo = linkedListOne, linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry

        newNode = LinkedList(sumOfValues % 10)
        currentNode.next = newNode
        currentNode = currentNode.next

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None 
    
    return NewLinkedList.next
