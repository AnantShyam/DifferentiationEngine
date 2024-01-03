class Node:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print(self):
        return f"{self.name} = {self.value}"


def print_graph(graph):
    result = {}

    for node in graph:
        node_printed = node.print()
        # print(node_printed)
        result[node_printed] = []
        for neighbor in graph[node]:
            neighbor_printed = neighbor.print()
            result[node_printed].append(neighbor_printed)

    print(result)
