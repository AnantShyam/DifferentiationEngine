import collections


class DataNode:

    def __init__(self, val, var_name):
        self._val = val
        self.var_name = var_name

    def set_val(self, data):
        self._val = data

    def get_val(self):
        return self._val


class OperationNode:

    def __init__(self, op):
        self._op = op

    def get_op(self):
        return self._op

    def set_op(self, data):
        self._op = data


class Edge:

    def __init__(self, node1, node2):
        self._start_node = node1
        self._end_node = node2

    def get_start_node(self):
        return self._start_node

    def get_end_node(self):
        return self._end_node

    def set_start_node(self, node):
        assert isinstance(node, DataNode) or isinstance(node, OperationNode)
        self._start_node = node

    def set_end_node(self, node):
        assert isinstance(node, DataNode) or isinstance(node, OperationNode)
        self._end_node = node


class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.adjacency_list = self.create_adjacency_list()

    def create_adjacency_list(self):
        adjacency_list = collections.defaultdict(list)

        for edge in self.edges:
            start, end = edge.get_end_node(), edge.get_end_node
            adjacency_list[start].append(end)

        return adjacency_list
