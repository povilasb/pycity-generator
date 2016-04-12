import ast

import python


def make_function_ast(src):
    """Constructs python AST function node.

    Args:
        src (str): function body.

    Returns:
        python.FunctionAst: function AST node.
    """
    return python.AstTree(ast.parse(src)).functions()[0]


def make_class_ast(src):
    """Constructs python AST class node.

    Args:
        src (str): class body.

    Returns:
        python.ClassAst: class AST node.
    """
    return python.AstTree(ast.parse(src)).classes()[0]
