from graph import *


def forward_pass(forward_adj, adj, graph):
    # do a Breadth First Search through the graph and fill in values
    visited = []
    q = []
    # add variable nodes to queue
    for node in adj:
        if node.name.is_alpha():
            q.append(node)

    while q:
        current_node = q.pop(0)
        visited.append(current_node)

        # check if value of that node has been updated
        pass

        



    return graph
