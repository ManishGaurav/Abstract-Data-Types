#!/usr/bin/env python3


class Vertex:
    def __init__(self, vertexName):
        self.name = str(vertexName)
        self._adjDict = dict()
        self._adjSet = set()

    def addNeighbour(self, vertexObject, weight=0):
        self._adjDict[vertexObject] = weight
        self._adjSet.add(vertexObject)

    @property
    def adjacencyDictionary(self):
        return list(self._adjDict.items())

    @property
    def adjacencyList(self):
        return list(self._adjDict.keys())

    @property
    def adjacencySet(self):
        return self._adjSet

    @property
    def degree(self):
        return len(self._adjSet)

    def getWeight(self, vertexObject):
        return self._adjDict[vertexObject]

    @property
    def printAdjacencyList(self):
        print("{}: ".format(self.name), end='')
        print([vobj.name for vobj in self.adjacencyList])

    @property
    def printAdjacencyDictionary(self):
        print("{}: ".format(self.name), end='')
        print([(vobj.name, wt) for vobj, wt in self.adjacencyDictionary])


class SimpleGraph:
    def __init__(self, directed=False):
        self._directed = directed
        self._vertexDict = dict()
        self._vertexSet = set()

    def addEdge(self, edge):
        if not isinstance(edge, tuple):
            print("An edge must a tuple: ", edge)
            exit(1)
        if len(edge) == 2 and not self._directed:
            uname, vname = str(edge[0]), str(edge[1])
            wt = 0
        elif len(edge) == 3 and self._directed:
            uname, vname, wt = str(t[0]), str(t[1]), float(t[2])
        else:
            print("An edge must a tuple of length 2 (undirected) or 3 (directed): ", edge)
            exit(1)
        uobj = self.addVertex(uname)
        vobj = self.addVertex(vname)
        uobj.addNeighbour(vobj, wt)
        if not self._directed:
            vobj.addNeighbour(uobj, wt)

    def addVertex(self, vertexName):
        vertexName = str(vertexName)
        if vertexName in self._vertexSet:
            vertexObject = self._vertexDict[vertexName]
        else:
            vertexObject = Vertex(vertexName)
            self._vertexDict[vertexName] = vertexObject
            self._vertexSet.add(vertexName)
        return vertexObject

    def bfs(self, srcName):
        visited = set()
        visitSeq = list()
        queue = list()
        queue.append(self._vertexDict[srcName])
        while queue:
            vertexObject = queue.pop(0)
            if vertexObject.name not in visited:
                visited.add(vertexObject.name)
                visitSeq.append(vertexObject.name)
                queue.extend(list(vertexObject.adjacencySet - visited))
        return visitSeq, visited

    @property
    def connectedComponents(self):
        components = list()
        visited = set()
        unvisited = (
            vertexName for vertexName in self.vertexSet if vertexName not in visited)
        for vertexName in unvisited:
            visitSeq, component = self.dfs(vertexName)
            visited |= component
            components.append(component)
        return components

    def dfs(self, srcName):
        visited = set()
        visitSeq = list()
        stack = list()
        stack.append(self._vertexDict[srcName])
        while stack:
            vertexObject = stack.pop()
            if vertexObject.name not in visited:
                visited.add(vertexObject.name)
                visitSeq.append(vertexObject.name)
                stack.extend(list(vertexObject.adjacencySet - visited))
        return visitSeq, visited

    def fromEdgeList(self, edgeList):
        for edge in edgeList:
            edge = tuple(edge)
            self.addEdge(edge)

    def fromFile(self, filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = str(line.strip('\r').strip('\n'))
                if self.directed:
                    u, v, wt = line.split()
                    edge = (u, v, wt)
                else:
                    u, v = line.split()
                    edge = (u, v)
                self.addEdge(edge)

    @property
    def printGraph(self):
        print("The adjacency list representation of the graph is:")
        for vname, vobj in self.vertexDictionary:
            vobj.printAdjacencyList

    @property
    def printGraphWithWeights(self):
        print("The adjacency list representation of the weighted graph is:")
        for vname in self._vertexDict:
            self._vertexDict[vname].printAdjacencyDictionary

    def printAdjacencyList(self, vertexName):
        self._vertexDict[vertexName].printAdjacencyList

    def printAdjacencyDictionary(self, vertexName):
        self._vertexDict[vertexName].printAdjacencyDictionary

    @property
    def vertexDictionary(self):
        return list(self._vertexDict.items())

    @property
    def vertexList(self):
        return list(self._vertexDict.keys())

    @property
    def vertexSet(self):
        return self._vertexSet


def main():
    edgeList = [('A', 'B'), ('A', 'C'), ('B', 'D'),
                ('B', 'E'), ('C', 'F'), ('E', 'F')]
    ug = SimpleGraph()
    ug.fromEdgeList(edgeList)
    ug.printGraph
    ug.printGraphWithWeights
    print("\nThe bfs traversal from source 'A' is:")
    visitSeq, visited = ug.bfs('A')
    print(visitSeq)
    print("\nThe dfs traversal from source 'A' is:")
    visitSeq, visited = ug.dfs('A')
    print(visitSeq)
    components = ug.connectedComponents
    print("\nThe number of connected components of the graph is: ", len(components))
    print("The components of the graph are: ")
    print(*components, sep='\n')


if __name__ == '__main__':
    main()
