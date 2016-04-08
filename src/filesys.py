import os


def read_file(fname):
    with open(fname, 'r') as f:
        return f.read()


class Node(object):
    """Filesystem node: file or directory.
    """
    def __init__(self, root_path, name):
        """
        Args:
            root_path (str): node location in file system.
            name (str): file or directory name.
        """
        self.root_path = root_path
        self.name = name


    @property
    def full_path(self):
        """Returns full file system node path."""
        return os.path.join(self.root_path, self.name)


class File(Node):
    """Represents file in filesystem."""
    pass


class Directory(Node):
    """Represents directory in filesystem."""
    pass


def walk(path, callback, callback_arg=None):
    """Traverse the directory recursively.

    Invokes the specified callback for every file system node.
    Passes the specified argument to the callback.
    The callback might return any value which will be passed to next
    walk() call as a callback argument.

    Args:
        path (str): file system path to traverse.
        callback (callable): function to be called for every traversed node.
            It's signature is callback(fs_node, arg).
        callback_arg (any): callback argument. Default is None.
    """
    fs_nodes = os.listdir(path)
    for f in py_files(fs_nodes):
        callback(File(path, f), callback_arg)

    for d in directories(fs_nodes, path):
        new_callback_arg = callback(Directory(path, d), callback_arg)
        walk(os.path.join(path, d), callback, new_callback_arg)


def py_files(fs_nodes):
    """Extracts python files.

    Args:
        fs_nodes (list): file system nodes.

    Returns:
        list: nodes whose name ends with '*.py'.
    """
    return [f for f in fs_nodes if f.endswith('.py')]


def directories(fs_nodes, root_path):
    """Extracts directories from file system nodes.

    Args:
        fs_nodes (list): file system nodes.
        root_path (str): path where nodes are located. It is used to check
            if the node is a directory.

    Returns:
        list: nodes whose name ends with '*.py'.
    """
    return [f for f in fs_nodes if os.path.isdir(os.path.join(root_path, f))]
