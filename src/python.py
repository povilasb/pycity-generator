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

def class_nodes(tree):
    return children_of_type(tree, ast.ClassDef)

def function_nodes(tree):
    return children_of_type(tree, ast.FunctionDef)

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

def parse_module(fname):
    return ast.parse(filesys.read_file(fname))

def analyze_file(fname):
    module_tree = parse_module(fname)

    file_stats = {
        'classes': {},
        'functions': {}
    }

    for c in class_nodes(module_tree):
        file_stats['classes'][c.name] = {
            'code_length': code_length(c),
            'methods': method_count(c),
        }

    for f in function_nodes(module_tree):
        file_stats['functions'][f.name] = {
            'code_length': code_length(f)
        }

    return file_stats
