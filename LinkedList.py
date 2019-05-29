class LinkedList():
    """linked list implementation in python"""

    def __init__(self):
        self.headerNode = None
        self.endNode = None
        self.size = 0

    def addNode(self, node):
        if isinstance(node, Node):
            if not self.search(node):
                if not self.headerNode:
                    self.headerNode = node
                else:
                    self.endNode.next = node
                self.endNode = node
                self.size += 1
            else:
                print("Node already exists!")
        else:
            print("Invalid Node to add")

    def removeNode(self, node):
        if isinstance(node, Node):
            if self.search(node):
                parentNode, node = self.search(node)
                nextNode = node.next
                if not nextNode:
                    self.endNode = parentNode
                if parentNode:
                    parentNode.next = nextNode
                else:
                    self.headerNode = nextNode
                node.next = None
                self.size -= 1
            else:
                print("Node not present in Linked List")
        else:
            print("Invalid node to delete")

    def printList(self):
        print("Linked List: ")
        currentNode = self.headerNode
        while currentNode:
            end = " -> " if currentNode.next else "\n"
            print(currentNode.val, end=end)
            currentNode = currentNode.next

    def search(self, node):
        currentNode = self.headerNode
        parentNode = None
        while currentNode:
            if currentNode is not node:
                parentNode = currentNode
                currentNode = currentNode.next
            else:
                return parentNode, node
        return False


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == "__main__":
    linkList = LinkedList()
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    linkList.addNode(node1)
    linkList.addNode(node2)
    linkList.addNode(node3)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.removeNode(node1)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.removeNode(node2)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.removeNode(node3)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.removeNode(node1)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.addNode(node1)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.removeNode(node1)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    linkList.addNode(node2)
    linkList.printList()
    print(f"Size of the Linked List is {linkList.size}")

    print(dir())
