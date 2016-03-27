import ast

import python

def make_function_node(src):
    """Constructs python AST function node.

    Args:
        src (str): function body.

    Returns:
        ast.FunctionDef: function AST node.
    """
    return python.function_nodes(ast.parse(src))[0]
