# O(V + E) time | O(V) space, where V = vertices and E = edges
# Sample Input: 
#   "nodes": [
#     {"children": ["B", "C", "D"], "id": "A", "value": "A"},
#     {"children": ["E", "F"], "id": "B", "value": "B"},
#     {"children": [], "id": "C", "value": "C"},
#     {"children": ["G", "H"], "id": "D", "value": "D"},
#     {"children": [], "id": "E", "value": "E"},
#     {"children": ["I", "J"], "id": "F", "value": "F"},
#     {"children": ["K"], "id": "G", "value": "G"},
#     {"children": [], "id": "H", "value": "H"},
#     {"children": [], "id": "I", "value": "I"},
#     {"children": [], "id": "J", "value": "J"},
#     {"children": [], "id": "K", "value": "K"}
#   ],
#   "startNode": "A"
# }
# Sample Output: ["A","B","C","D","E","F","G","H","I","J","K"]

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        return array

# Note: Storing V nodes; Queue holds nodes where worst case can be all the nodes are in Queue