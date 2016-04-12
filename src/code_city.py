import python

def analyze_function(func_node):
    """Analyze the function AST node.

    Args:
        func_node (python.FunctionAst)

    Returns:
        dict: metrics about the specified function.
    """
    return {
        'code_length': func_node.loc(),
        'arguments': func_node.argument_count(),
    }


def analyze_class(class_node):
    """Analyze the class AST node.

    Args:
        class_node (ast.ClassDef)

    Returns:
        dict: metrics about the specified class.
    """
    return {
        'code_length': class_node.loc(),
        'methods': class_node.method_count(),
    }


def analyze_file(fname):
    """Analyzes source file and produces data for Code City.

    Args:
        fname (str): full path to source file.

    Returns
        dict: code city data representing the source file.
    """
    module = python.parse_module(fname)
    return {
        'classes': {
            c.name: analyze_class(c) for c in module.classes()},
        'functions': {
            f.name: analyze_function(f) for f in module.functions()
        }
    }
