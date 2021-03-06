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


class AstTree(object):
    """Abstratc Python Syntax Tree."""

    def __init__(self, ast_tree):
        """
        Args:
            ast_tree: object returned by ast.parse().
        """
        self.ast_tree = ast_tree


    def classes(self):
        """
        Returns:
            list: child nodes of type ClassAst.
        """
        return [ClassAst(child) for child \
            in children_of_type(self.ast_tree, ast.ClassDef)]


    def functions(self):
        """
        Returns:
            list: function child nodes wrapped in FunctionAst.
        """
        return [FunctionAst(child) for child \
                in children_of_type(self.ast_tree, ast.FunctionDef)]


    def loc(self):
        """
        Returns:
            int: function lines of code.
        """
        return last_line(self.ast_tree) - self.ast_tree.lineno + 1


    @property
    def name(self):
        """
        Returns:
            str: function or class name.
        """
        return self.ast_tree.name


class FunctionAst(AstTree):
    """ast.FunctionDef wrapper.

    Provides higher level functions.
    """

    def __init__(self, ast_tree):
        """
        Args:
            ast_tree: object returned by ast.parse().
        """
        super(FunctionAst, self).__init__(ast_tree)

        self._assert_function_def()


    def argument_count(self):
        """
        Returns:
            int: number of arguments within the function node.
        """
        return len(argument_nodes(self.ast_tree))


    def _assert_function_def(self):
        """Ensure that the wrapped AST node is FunctionDef."""
        if (type(self.ast_tree) != ast.FunctionDef):
            raise ValueError(
                'Invalid ast object type. Expected FunctionDef.')


class ClassAst(AstTree):
    """ast.ClassDef wrapper.

    Provides higher level functions.
    """

    def __init__(self, ast_tree):
        """
        Args:
            ast_tree: object returned by ast.parse().
        """
        super(ClassAst, self).__init__(ast_tree)

        self._assert_class_def()


    def method_count(self):
        """
        Returns:
            int: class method count.
        """
        return len(self.functions())


    def _assert_class_def(self):
        """Ensure that the wrapped AST node is ClassDef."""
        if (type(self.ast_tree) != ast.ClassDef):
            raise ValueError(
                'Invalid ast object type. Expected ClassDef.')


def parse_module(fname):
    """Parses python module.

    Args:
        fname (str): python file name to parse.

    Returns:
        AstTree: abstract syntax tree object
    """
    return AstTree(ast.parse(filesys.read_file(fname)))
