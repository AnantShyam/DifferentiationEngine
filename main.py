import argparse
import collections
from graph import *


def print_helper(edges):
    res = []
    for edge in edges:
        start, end = edge.get_start_node(), edge.get_end_node()
        edge = ""
        for node in [start, end]:
            if type(node) == OperationNode:
                edge = edge + str(node.get_op())
            else:
                edge = edge + str(node.get_val())
        # print(edge)
        # res.append(f"{edge.get_start_node()}, {edge.get_end_node()}")
    # print(res)


def process_user_input(function):

    # interpret function
    variables_degrees = {}
    operation_sequence = []
    operations = ["+", "-", "/", "*"]

    acc = ""
    for i in function:
        if i != " ":
            if i in operations:
                operation_sequence.append(i)
            acc = acc + i
        else:
            # now we reach a whitespace, meaning that we've encountered one polynomial term
            # get variable and degree
            potential_variables = [i for i in acc if i.isalpha()]
            variable = potential_variables[0] if potential_variables else None

            potential_degrees = [acc[i] for i in range(len(acc)) if (acc[i].isdigit() and i != 0 and acc[i - 1] == "^")]

            degree = int(potential_degrees[0]) if potential_degrees else None

            if variable not in variables_degrees and variable is not None and degree is not None:
                variables_degrees[variable] = [degree]
            elif variable in variables_degrees and variable is not None and degree is not None:
                variables_degrees[variable].append(degree)

            if (variable, degree) != (None, None):
                operation_sequence.append((variable, degree))

            acc = ""

    # create graph

    edges = []
    for variable in variables_degrees:
        degrees = variables_degrees[variable]
        for degree in degrees:
            var_nodes = []
            for _ in range(degree):
                var_nodes.append(DataNode(0, variable))

            # construct multiple copies of the variable node v if there exists a term v^a, a > 1
            multiplication_node = OperationNode("*")
            if degree > 1:
                for var_node in var_nodes:
                    edges.append(Edge(var_node, multiplication_node))

            # now add an edge from the multiplication_node to the output node (for instance, x^3)
            output_node = DataNode(0, f"{variable}^{degree}")
            edges.append(Edge(multiplication_node, output_node))

    print_helper(edges)


if __name__ == "__main__":
    # assuming user input is passed into the argument parser in the following manner:
    # for now, only supporting polynomial functions
    # python main.py "function" "variable" "value"
    parser = argparse.ArgumentParser(description="Process User Command Line Arguments")
    parser.add_argument("function")
    parser.add_argument("variable")
    parser.add_argument("value")

    arguments = parser.parse_args()
    # print(arguments.function)
    print(process_user_input(arguments.function + " "))


