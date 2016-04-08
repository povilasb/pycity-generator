import python

def analyze_function(func_node):
    """Analyze the function AST node.

    Args:
        func_node (ast.FunctionDef)

    Returns:
        dict: metrics about the specified function.
    """
    return {
        'code_length': python.code_length(func_node),
        'arguments': python.argument_count(func_node),
    }


def analyze_class(class_node):
    """Analyze the class AST node.

    Args:
        class_node (ast.ClassDef)

    Returns:
        dict: metrics about the specified class.
    """
    return {
        'code_length': python.code_length(class_node),
        'methods': python.method_count(class_node),
    }


def analyze_file(fname):
    """Analyzes source file and produces data for Code City.

    Args:
        fname (str): full path to source file.

    Returns
        dict: code city data representing the source file.
    """
    module_tree = python.parse_module(fname)
    return {
        'classes': {
            c.name: analyze_class(c) for c in python.class_nodes(module_tree)},
        'functions': {
            f.name: analyze_function(f) for f in python.function_nodes(module_tree)
        }
    }
