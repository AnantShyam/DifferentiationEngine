import argparse
import collections
from graph import *


def process_user_input(function):

    # interpret function
    variables_degrees = {}

    acc = ""
    for i in function:
        if i != " ":
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

            acc = ""

    # analyze +, - etc operations too
    # create graph

    for variable in variables_degrees:
        degrees = variables_degrees[variable]

        for degree in degrees:
            var_nodes = []
            for _ in range(degree):
                var_nodes.append(DataNode(None, variable))



if __name__ == "__main__":
    # assuming user input is passed into the argument parser in the following manner:
    # for now, only supporting polynomial functions
    # python main.py "function" "variable" "value"
    parser = argparse.ArgumentParser(description="Process User Command Line Arguments")
    parser.add_argument("function")
    parser.add_argument("variable")
    parser.add_argument("value")

    arguments = parser.parse_args()
    print(arguments.function)
    print(process_user_input(arguments.function + " "))


