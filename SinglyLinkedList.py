#!/usr/bin/env python3


class Node:
    def __init__(self, data=None, nextNode=None, previousNode=None):
        self.data = data
        self.next = nextNode
        self.prev = previousNode


class SinglyLinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def deleteAtBeginning(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1

    def deleteAtEnd(self):
        if self.head:
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
            raise IndexError()
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

    def deleteWithValue(self, data):
        if self.head:
            currentNode = self.head
            previousNode = None
            found = False
            while currentNode:
                if currentNode.data == data:
                    found = True
                    break
                previousNode = currentNode
                currentNode = currentNode.next
            if not found:
                raise ValueError("'{}' does not exit in the list.".format(data))
            else:
                if previousNode is None:
                    self.head = currentNode.next
                else:
                    previousNode.next = currentNode.next
                self.size -= 1

    def getReverseList(self):
        currentNode = self.head
        revList = SinglyLinkedList()
        while currentNode:
            revList.insertAtBeginning(currentNode.data)
            currentNode = currentNode.next
        return revList

    def index(self, data):
        currentNode = self.head
        count = 0
        idx = -1
        while currentNode:
            if currentNode.data == data:
                idx = count
                break
            currentNode = currentNode.next
            count += 1
        return idx

    def insertAtBeginning(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1

    def insertAtEnd(self, data):
        if self.head:
            newNode = Node(data, None)
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
            self.size += 1
        else:
            self.insertAtBeginning(data)

    def insertAtIndex(self, data, index):
        if index not in range(len(self) + 1):
            raise IndexError()
        if index == 0:
            self.insertAtBeginning(data)
        elif index == len(self):
            self.insertAtEnd(data)
        else:
            currentNode = self.head
            for i in range(index):
                previousNode = currentNode
                currentNode = currentNode.next
            newNode = Node(data, currentNode)
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
                if firstListNode.data != secondListNode.data:
                    return False
                firstListNode = firstListNode.next
                secondListNode = secondListNode.next
            return True

    def isSorted(self):
        if not self.head or not self.head.next:
            return True
        currentNode = self.head
        while currentNode and currentNode.next:
            if currentNode.data > currentNode.next.data:
                return False
            currentNode = currentNode.next
        return True

    def getMergedSortedList(self, otherList):
        firstListNode = self.head
        secondListNode = otherList.head
        mergedList = SinglyLinkedList()
        while firstListNode and secondListNode:
            if firstListNode.data <= secondListNode.data:
                mergedList.insertAtEnd(firstListNode.data)
                firstListNode = firstListNode.next
            else:
                mergedList.insertAtEnd(secondListNode.data)
                secondListNode = secondListNode.next
        while firstListNode:
            mergedList.insertAtEnd(firstListNode.data)
            firstListNode = firstListNode.next
        while secondListNode:
            mergedList.insertAtEnd(secondListNode.data)
            secondListNode = secondListNode.next
        return mergedList

    def getMiddle(self):
        if self.head:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.data

    def makeList(self, iterable):
        for i in iterable:
            self.insertAtEnd(i)

    def printList(self):
        currentNode = self.head
        while currentNode:
            if currentNode == self.head:
                print(currentNode.data, end='')
            else:
                print(' -> ', currentNode.data, end='')
            currentNode = currentNode.next
        print()

    def __len__(self):
        return self.size


def main():
    pass


if __name__ == '__main__':
    main()
