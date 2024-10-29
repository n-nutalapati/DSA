class Node():
    def __init__(self, value):
        self.value = value
        self.adjacent_lst = []
        self.visited = False

class Graph():
    def BFS(self, node):
        queue = []
        queue.append(node)
        node.visited = True

        traversal = []

        while queue:
            actualNode = queue.pop(0)
            traversal.append(actualNode.value)

            for element in actualNode.adjacent_lst:
                if element.visited  is False:
                    queue.append(element)
                    element.visited = True

        return traversal
    
    def DFS(self, node, traversal):
        node.visited = True
        traversal.append(node.value)

        for element in node.adjacent_lst:
            if element.visited is False:
                self.DFS(element, traversal)

        return traversal


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjacent_lst.append(node2)
node1.adjacent_lst.append(node3)
node1.adjacent_lst.append(node4)
node2.adjacent_lst.append(node5)
node2.adjacent_lst.append(node6)
node4.adjacent_lst.append(node7)

graph = Graph()
# print(graph.BFS(node1))
print(graph.DFS(node1, []))