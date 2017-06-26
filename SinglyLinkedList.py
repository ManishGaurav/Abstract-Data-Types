#!/usr/bin/env python3


class Node:
    def __init__(self, key=None, nextNode=None, previousNode=None):
        self.key = key
        self.next = nextNode
        self.prev = previousNode


class SinglyLinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def deleteAtBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1

    def deleteAtEnd(self):
        if self.head is None:
            return
        currentNode = self.head
        previousNode = None
        while currentNode.next:
            previousNode = currentNode
            currentNode = currentNode.next
        if previousNode is None:
            self.head = currentNode.next
        else:
            previousNode.next = currentNode.next
        self.size -= 1

    def deleteAtIndex(self, index):
        if index not in range(len(self)):
            raise IndexError("Index must be in range [0, {}].".format(len(self) - 1))
        if index == 0:
            self.deleteAtBeginning()
        elif index == len(self) - 1:
            self.deleteAtEnd()
        else:
            currentNode = self.head
            for i in range(index):
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = currentNode.next
            self.size -= 1

    def deleteKey(self, key):
        if self.head is None:
            return
        found, previousNode, currentNode = self._getPreviousAndCurrentNode(key)
        if not found:
            raise ValueError("'{}' does not exit in the list.".format(key))
        if previousNode is None:
            self.head = currentNode.next
        else:
            previousNode.next = currentNode.next
        self.size -= 1

    def getReverseList(self):
        currentNode = self.head
        revList = SinglyLinkedList()
        while currentNode:
            revList.insertAtBeginning(currentNode.key)
            currentNode = currentNode.next
        return revList

    def insertAtBeginning(self, key):
        newNode = Node(key, self.head)
        self.head = newNode
        self.size += 1

    def insertAtEnd(self, key):
        if self.head is None:
            self.insertAtBeginning(key)
            return
        newNode = Node(key, None)
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode
        self.size += 1

    def insertAtIndex(self, key, index):
        if index not in range(len(self) + 1):
            raise IndexError("Index must be in range [0, {}].".format(len(self)))
        if index == 0:
            self.insertAtBeginning(key)
        elif index == len(self):
            self.insertAtEnd(key)
        else:
            currentNode = self.head
            for i in range(index):
                previousNode = currentNode
                currentNode = currentNode.next
            newNode = Node(key, currentNode)
            previousNode.next = newNode
            self.size += 1

    def isEmpty(self):
        return not self.head

    def isEqual(self, otherList):
        if len(self) != len(otherList):
            return False
        else:
            firstListNode = self.head
            secondListNode = otherList.head
            while firstListNode and secondListNode:
                if firstListNode.key != secondListNode.key:
                    return False
                firstListNode = firstListNode.next
                secondListNode = secondListNode.next
            return True

    def isSorted(self):
        if self.head is None or self.head.next is None:
            return True
        currentNode = self.head
        while currentNode and currentNode.next:
            if currentNode.key > currentNode.next.key:
                return False
            currentNode = currentNode.next
        return True

    def getIndex(self, key):
        currentNode = self.head
        count = 0
        index = -1
        while currentNode:
            if currentNode.key == key:
                index = count
                break
            currentNode = currentNode.next
            count += 1
        return index

    def getMiddleNode(self):
        if self.head is None or self.head.next is None:
            return self.head
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def hasCycle(self):
        if self.head is None or self.head.next is None:
            return False
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def makeList(self, iterable):
        for i in iterable:
            self.insertAtEnd(i)

    def mergeSort(self):
        if self.head is None or self.head.next is None:
            return self
        left, right = self._splitList()
        left = left.mergeSort()
        right = right.mergeSort()
        return left._merge(right)

    def printList(self):
        currentNode = self.head
        while currentNode:
            if currentNode == self.head:
                print(currentNode.key, end='')
            else:
                print(' -> ', currentNode.key, end='')
            currentNode = currentNode.next
        print()

    def sortedInsertion(self, key):
        if self.head is None:
            self.insertAtBeginning(key)
        elif self.head.key >= key:
            newNode = Node(key, self.head)
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next and currentNode.next.key < key:
                currentNode = currentNode.next
            newNode = Node(key, currentNode.next)
            currentNode.next = newNode

    def swapNodes(self, x, y):
        if self.head is None or x == y:
            return
        foundX, previousX, currentX = self._getPreviousAndCurrentNode(x)
        if not foundX:
            raise ValueError("'{}' does not exit in the list.".format(x))
        foundY, previousY, currentY = self._getPreviousAndCurrentNode(y)
        if not foundY:
            raise ValueError("'{}' does not exit in the list.".format(y))
        if previousX is None:
            self.head = currentY
        else:
            previousX.next = currentY
        if previousY is None:
            self.head = currentX
        else:
            previousY.next = currentX
        currentX.next, currentY.next = currentY.next, currentX.next

    def updateAtIndex(self, index, key):
        if index not in range(len(self)):
            raise IndexError("Index must be in range [0, {}].".format(len(self) - 1))
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        currentNode.key = key

    def updateKey(self, oldKey, newKey):
        if self.head is None:
            return
        found, previousNode, currentNode = self._getPreviousAndCurrentNode(oldKey)
        if not found:
            raise ValueError("'{}' does not exit in the list.".format(oldKey))
        currentNode.key = newKey

    def _getPreviousAndCurrentNode(self, key):
        currentNode = self.head
        previousNode = None
        found = False
        while currentNode:
            if currentNode.key == key:
                found = True
                break
            previousNode = currentNode
            currentNode = currentNode.next
        return found, previousNode, currentNode

    def _merge(self, otherList):
        firstListNode = self.head
        secondListNode = otherList.head
        mergedList = SinglyLinkedList()
        while firstListNode and secondListNode:
            if firstListNode.key <= secondListNode.key:
                mergedList.insertAtEnd(firstListNode.key)
                firstListNode = firstListNode.next
            else:
                mergedList.insertAtEnd(secondListNode.key)
                secondListNode = secondListNode.next
        while firstListNode:
            mergedList.insertAtEnd(firstListNode.key)
            firstListNode = firstListNode.next
        while secondListNode:
            mergedList.insertAtEnd(secondListNode.key)
            secondListNode = secondListNode.next
        return mergedList

    def _splitList(self):
        if self.head is None or self.head.next is None:
            left = SinglyLinkedList(self.head)
            right = SinglyLinkedList()
        else:
            middleNode = self.getMiddleNode()
            left = SinglyLinkedList(self.head)
            right = SinglyLinkedList(middleNode.next)
            middleNode.next = None
        return left, right

    def __len__(self):
        return self.size
        # currentNode = self.head
        # size = 0
        # while currentNode:
        #     size += 1
        #     currentNode = currentNode.next
        # return size



def main():
    pass


if __name__ == '__main__':
    main()
