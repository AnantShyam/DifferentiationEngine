import argparse
import collections
import random
from graph import *


def construct_graph(function, variable_names, variable_values, variable):
    v, values = [], []
    # parse variable_names and get all distinct variables
    for i in variable_names:
        if i.isalpha() and i not in v:
            v.append(i)
    for i in variable_values:
        if i.isdigit():
            values.append(i)
    num_vars, num_vals = len(v), len(values)
    assert num_vars == num_vals
    variables = {v[i]: values[i] for i in range(num_vars)}

    adj = {}

    forward_adj = {}

    for variable in variables:
        adj[variable] = []
        forward_adj[variable] = []


    n = len(function)

    operators = ['+', "*"]

    variable_groups = []
    group = ""
    for i in range(n):
        if function[i] == '(':  # start of a new group
            group = ""
        elif function[i] == ')':  # end of group
            variable_groups.append(group)
            group = ""
        elif function[i] not in [' ', ',']:
            group = group + function[i]

    for idx, group in enumerate(variable_groups):
        v, operator = [], []
        for i in group:
            if i in variables:
                v.append(i)
            elif i in operators:
                operator.append(f"{i}{idx}")

        for i in range(0, len(v), 2):
            operator_idx = i//2
            adj[v[i]].append(operator[operator_idx])
            forward_adj[v[i]].append(operator[operator_idx])

            if operator[operator_idx] not in adj:
                adj[operator[operator_idx]] = [v[i]]
            else:
                adj[operator[operator_idx]].append(v[i])

            # variables[operator[operator_idx]] = 1

            adj[v[i + 1]].append(operator[operator_idx])
            forward_adj[v[i + 1]].append(operator[operator_idx])
            if operator[operator_idx] not in adj:
                adj[operator[operator_idx]] = [v[i + 1]]
            else:
                adj[operator[operator_idx]].append(v[i + 1])

            forward_adj[operator[operator_idx]] = []

    final_node = "l1"
    for key in forward_adj:
        if not forward_adj[key]:
            forward_adj[key].append(final_node)

    graph = {}
    for variable in adj:
        variable_value = variables[variable] if variable in variables else 1
        new_key = f"{variable},{variable_value}"
        neighbors = []
        for neighbor in adj[variable]:
            neighbor_value = variables[neighbor] if neighbor in variables else 1
            neighbors.append(f"{neighbor},{neighbor_value}")
        graph[new_key] = neighbors

    revised_graph = {}
    for variable in graph:
        comma_idx = variable.find(',')
        name, val = variable[:comma_idx], variable[comma_idx + 1:]
        variable_node = Node(name, val)
        revised_graph[variable_node] = []
        for neighbor in graph[variable]:
            comma_idx = neighbor.find(',')
            name, val = neighbor[:comma_idx], neighbor[comma_idx + 1:]
            revised_graph[variable_node].append(Node(name, val))

    return revised_graph


if __name__ == "__main__":
    # assuming user input is passed into the argument parser in the following manner:
    # for now, only supporting polynomial functions
    # python main.py "function" "variable" "value"
    parser = argparse.ArgumentParser(description="Process User Command Line Arguments")
    parser.add_argument("function")
    parser.add_argument("names")
    parser.add_argument("values")
    parser.add_argument("variable")

    arguments = parser.parse_args()
    # print(arguments.function)
    # print(process_user_input(arguments.function + " "))
    g = construct_graph(arguments.function, arguments.names, arguments.values, arguments.variable)
    print_graph(g)

