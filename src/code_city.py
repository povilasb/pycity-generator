import python

def analyze_file(fname):
    """Analyzes source file and produces data for Code City.

    Args:
        fname (str): full path to source file.

    Returns
        dict: code city data representing the source file.
    """
    module_tree = python.parse_module(fname)

    file_stats = {
        'classes': {},
        'functions': {}
    }

    for c in python.class_nodes(module_tree):
        file_stats['classes'][c.name] = {
            'code_length': python.code_length(c),
            'methods': python.method_count(c),
        }

    for f in python.function_nodes(module_tree):
        file_stats['functions'][f.name] = {
            'code_length': python.code_length(f)
        }

    return file_stats
