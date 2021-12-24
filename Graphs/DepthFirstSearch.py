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
# Sample Output: 20

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# Note: O(V + E) time | O(V) space --> Where V = nodes/vertices, E = edges
# Depth First Search of parent node/vertex will not be resolved before 
# its child node and so on (so you will have V nodes/vertices) on the 
# call stack --> that's why O(V) --> This is the reason without counting
# the elements in array
# for the depthFirstSearch method.
# Feel free to add new properties