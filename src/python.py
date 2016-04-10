import ast

import filesys

def last_node(tree):
    """Finds last tree node.

    Adds parent field to every visited node.
    """
    if not tree:
        return

    node = None
    for node in ast.iter_child_nodes(tree):
        node.parent = tree

    return last_node(node) or node

def children_of_type(tree, children_type):
    children = []
    for node in ast.iter_child_nodes(tree):
        if type(node) is children_type:
            children.append(node)

    return children

def function_nodes(tree):
    return children_of_type(tree, ast.FunctionDef)

def argument_nodes(tree):
    """Extracts function argument nodes.

    Args:
        tree: python AST object.

    Returns:
        list(ast.Name): function arguments
    """
    args_node = children_of_type(tree, ast.arguments)[0]
    return [arg for arg in ast.iter_child_nodes(args_node)]

def try_get_line(node):
    try:
        return node.lineno
    except AttributeError:
        return None

def last_line(tree):
    node = last_node(tree)

    line = try_get_line(node)
    while not line and node.parent:
        node = node.parent
        line = try_get_line(node)

    return line

def code_length(node):
    return last_line(node) - node.lineno + 1

def method_count(class_node):
    return len(function_nodes(class_node))

def argument_count(function_node):
    """
    Args:
        function_node (Ast.FunctionDef)

    Returns:
        int: number of arguments within the specified function node.
    """
    return len(argument_nodes(function_node))


class AstTree(object):
    """Abstratc Python Syntax Tree."""

    def __init__(self, ast_tree):
        """
        Args:
            ast_tree: object returned by ast.parse().
        """
        self.ast_tree = ast_tree


    def class_nodes(self):
        """
        Returns:
            list: child nodes of type ast.ClassDef.
        """
        return children_of_type(self.ast_tree, ast.ClassDef)


def parse_module(fname):
    """Parses python module.

    Args:
        fname (str): python file name to parse.

    Returns:
        AstTree: abstract syntax tree object
    """
    return AstTree(ast.parse(filesys.read_file(fname)))
