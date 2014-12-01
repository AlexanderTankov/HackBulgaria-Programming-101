class DirectedGraph():

    def __init__(self):
        self.graph = {}

    def addEdge(self, nodeA, nodeB):
        if nodeA not in self.graph:
            self.graph[nodeA] = [nodeB]
        elif (nodeA in self.graph) and (nodeB not in self.graph[nodeA]):
            self.graph[nodeA].append(nodeB)

    def getNeighborsFor(self, node):
        return self.graph[node]

    def pathBetween(self, nodeA, nodeB):
        for neighbors in self.graph[nodeA]:
            if neighbors in self.graph:
                if nodeB in self.graph[neighbors]:
                    return True
        return False

    def toString(self):
        for elem in self.graph:
            return "{} --> {}".format(elem, self.getNeighborsFor(elem))
