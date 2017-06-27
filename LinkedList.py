#!/usr/bin/env python3


class Node:
    def __init__(self, key=None, nextNode=None, previousNode=None):
        self.key = key
        self.next = nextNode
        self.prev = previousNode


class SinglyLinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self._size = size

    def circularLeftShift(self, shift):
        shift = shift % len(self)
        if self.head is None or shift == 0:
            return
        index = 0
        currentNode = self.head
        while currentNode:
            if index == shift - 1:
                lastNodeToBe = currentNode
            if index == shift:
                firstNodeToBe = currentNode
            if currentNode.next is None:
                currentLastNode = currentNode
            index += 1
            currentNode = currentNode.next
        lastNodeToBe.next = None
        currentLastNode.next = self.head
        self.head = firstNodeToBe

    def deleteAtBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        self._size -= 1

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
        self._size -= 1

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
            self._size -= 1

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
        self._size -= 1

    def getDuplicateList(self):
        duplicateList = SinglyLinkedList()
        currentNode = self.head
        while currentNode:
            duplicateList.insertAtEnd(currentNode.key)
            currentNode = currentNode.next
        return duplicateList

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

    def getReverseList(self):
        currentNode = self.head
        revList = SinglyLinkedList()
        while currentNode:
            revList.insertAtBeginning(currentNode.key)
            currentNode = currentNode.next
        return revList

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

    def insertAtBeginning(self, key):
        newNode = Node(key, self.head)
        self.head = newNode
        self._size += 1

    def insertAtEnd(self, key):
        if self.head is None:
            self.insertAtBeginning(key)
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        newNode = Node(key, None)
        currentNode.next = newNode
        self._size += 1

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
            self._size += 1

    def isEmpty(self):
        return not self.head

    def isEqual(self, otherList):
        firstListNode = self.head
        secondListNode = otherList.head
        while firstListNode and secondListNode:
            if firstListNode.key != secondListNode.key:
                return False
            firstListNode = firstListNode.next
            secondListNode = secondListNode.next
        if firstListNode or secondListNode:
            return False
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
            self._size += 1
        else:
            currentNode = self.head
            while currentNode.next and currentNode.next.key < key:
                currentNode = currentNode.next
            newNode = Node(key, currentNode.next)
            currentNode.next = newNode
            self._size += 1

    def swapNodes(self, x, y):
        if self.head is None or x == y:
            return
        currentNode = self.head
        previousNode = None
        xNode = yNode = None
        previousX = previousY = None
        xIndex = yIndex = index = 0
        while currentNode:
            if xNode and yNode:
                break
            if currentNode.key == x:
                previousX = previousNode
                xNode = currentNode
                xIndex = index
            if currentNode.key == y:
                previousY = previousNode
                yNode = currentNode
                yIndex = index
            previousNode = currentNode
            currentNode = currentNode.next
            index += 1
        if xNode is None:
            raise ValueError("'{}' does not exit in the list.".format(x))
        if yNode is None:
            raise ValueError("'{}' does not exit in the list.".format(y))
        if xIndex > yIndex:
            xNode, yNode = yNode, xNode
            previousX, previousY = previousY, previousX
        if previousX is None:  # is xNode the first node?
            self.head = yNode
        else:
            previousX.next = yNode
        previousY.next = xNode
        xNode.next, yNode.next = yNode.next, xNode.next

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
        return self._size
        # currentNode = self.head
        # size = 0
        # while currentNode:
        #     size += 1
        #     currentNode = currentNode.next
        # return size


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, head=None, size=0):
        self.head = head
        self._size = size

    def circularLeftShift(self, shift):
        shift = shift % len(self)
        if self.head is None or shift == 0:
            return
        index = 0
        currentNode = self.head
        while currentNode:
            if index == shift - 1:
                lastNodeToBe = currentNode
            if index == shift:
                firstNodeToBe = currentNode
            if currentNode.next is None:
                currentLastNode = currentNode
            index += 1
            currentNode = currentNode.next
        print(lastNodeToBe.key, firstNodeToBe.key, currentLastNode.key)
        lastNodeToBe.next = None
        lastNodeToBe.prev = currentLastNode
        currentLastNode.next = self.head
        self.head = firstNodeToBe
        firstNodeToBe.prev = None

    def deleteAtBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self._size -= 1

    def deleteAtEnd(self):
        if self.head is None:
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        if currentNode.prev is None:
            self.head = currentNode.next
        else:
            currentNode.prev.next = currentNode.next
        self._size -= 1

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
                currentNode = currentNode.next
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            self._size -= 1

    def deleteKey(self, key):
        if self.head is None:
            return
        found, previousNode, currentNode = self._getPreviousAndCurrentNode(key)
        if not found:
            raise ValueError("'{}' does not exit in the list.".format(key))
        if previousNode is None:
            self.head = currentNode.next
            currentNode.next.prev = None
        else:
            previousNode.next = currentNode.next
            if currentNode.next:
                currentNode.next.prev = previousNode
        self._size -= 1

    def getDuplicateList(self):
        duplicateList = DoublyLinkedList()
        currentNode = self.head
        while currentNode:
            duplicateList.insertAtEnd(currentNode.key)
            currentNode = currentNode.next
        return duplicateList

    def getReverseList(self):
        currentNode = self.head
        revList = DoublyLinkedList()
        while currentNode:
            revList.insertAtBeginning(currentNode.key)
            currentNode = currentNode.next
        return revList

    def insertAtBeginning(self, key):
        newNode = Node(key, self.head, None)
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        self._size += 1

    def insertAtEnd(self, key):
        if self.head is None:
            self.insertAtBeginning(key)
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        newNode = Node(key, None, currentNode)
        currentNode.next = newNode
        self._size += 1

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
                currentNode = currentNode.next
            newNode = Node(key, currentNode, currentNode.prev)
            currentNode.prev.next = newNode
            currentNode.prev = newNode
            self._size += 1

    def printReverseList(self):
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        while currentNode:
            if currentNode.next is None:
                print(currentNode.key, end='')
            else:
                print(' -> ', currentNode.key, end='')
            currentNode = currentNode.prev
        print()

    def reverseList(self):
        if self.head is None or self.head.next is None:
            return
        tempNode = None
        currentNode = self.head
        while currentNode:
            if currentNode.next is None:
                self.head = currentNode
            currentNode.prev, currentNode.next = currentNode.next, currentNode.prev
            currentNode = currentNode.prev

    def sortedInsertion(self, key):
        if self.head is None:
            self.insertAtBeginning(key)
        elif self.head.key >= key:
            newNode = Node(key, self.head, None)
            self.head.prev = newNode
            self.head = newNode
            self._size += 1
        else:
            currentNode = self.head
            while currentNode.next and currentNode.next.key < key:
                currentNode = currentNode.next
            newNode = Node(key, currentNode.next, currentNode)
            currentNode.next.prev =  newNode
            currentNode.next = newNode
            self._size += 1

    def swapNodes(self, x, y):
        if self.head is None or x == y:
            return
        currentNode = self.head
        xNode = yNode = None
        xIndex = yIndex = index = 0
        while currentNode:
            if xNode and yNode:
                break
            if currentNode.key == x:
                xNode = currentNode
                xIndex = index
            if currentNode.key == y:
                yNode = currentNode
                yIndex = index
            currentNode = currentNode.next
            index += 1
        if xNode is None:
            raise ValueError("'{}' does not exit in the list.".format(x))
        if yNode is None:
            raise ValueError("'{}' does not exit in the list.".format(y))
        if xIndex > yIndex:
            xNode, yNode = yNode, xNode
        if xNode.prev is None: # is xNode the first node?
            self.head = yNode
        else:
            xNode.prev.next = yNode
        if yNode.next is not None: # is yNode the last node?
            yNode.next.prev = xNode
        if xNode.next == yNode: # are the nodes adjacent?
            xNode.next, yNode.next  = yNode.next, xNode
            xNode.prev, yNode.prev = yNode, xNode.prev
        else:
            yNode.prev.next = xNode
            xNode.next.prev = yNode
            xNode.prev, yNode.prev = yNode.prev, xNode.prev
            xNode.next, yNode.next = yNode.next, xNode.next

    def _getPreviousAndCurrentNode(self, key):
        currentNode = self.head
        previousNode = None
        found = False
        while currentNode:
            if currentNode.key == key:
                found = True
                break
            currentNode = currentNode.next
        if currentNode is not None:
            previousNode = currentNode.prev
        return found, previousNode, currentNode

    def _merge(self, otherList):
        firstListNode = self.head
        secondListNode = otherList.head
        mergedList = DoublyLinkedList()
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
            left = DoublyLinkedList(self.head)
            right = DoublyLinkedList()
        else:
            middleNode = self.getMiddleNode()
            left = DoublyLinkedList(self.head)
            right = DoublyLinkedList(middleNode.next)
            middleNode.next.prev = None
            middleNode.next = None
        return left, right


def main():
    pass


if __name__ == '__main__':
    main()
    
