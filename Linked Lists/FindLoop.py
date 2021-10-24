# O(n) time | O(1) space
# Sample Input: head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 
                                                   # ^    |
                                                    #|    v
                                                #    0 <- 9  
# Sample Output:  7 -> 8 
                # ^    |
                # |    v
                # 0 <- 9
# Note: (The head does not have 1)                                    
def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first