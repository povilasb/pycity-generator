import os

class Dir:
    def __init__(self, path):
        self.path = path

    def py_files(self):
        """Collects python files from directory.

        Returns:
            dict: directory tree with python files collected only.
        """
        tree = make_dir_node()

        for root, dirs, dir_files in os.walk(self.path):
            cur_dir_node = make_dir_node()
            cur_dir_node['files'] = [f for f in dir_files if f.endswith('.py')]

            parent_dir_node, cur_dir = get_subdir_parent(tree, self.subdir(root))
            if cur_dir:
                parent_dir_node['dirs'][cur_dir] = cur_dir_node
            else:
                tree['files'] = cur_dir_node['files']

        return tree

    def full_path(self, fname):
        return os.path.join(self.path, fname)

    def subdir(self, dir_path):
        """Extracts relative subdirectory path.

        Args:
            dir_path (str): subdirectory absolute path.

        Returns:
            str: path to the specified directory relative from this
                directory.
            None: if the specified directory is not inside this directory.
        """
        if dir_path.startswith(self.path):
            return dir_path[(len(self.path) + 1):]

def read_file(fname):
    with open(fname, 'r') as f:
        return f.read()

def make_dir_node():
    """Constructs directory node representing object.
    """
    return {
        'files': [],
        'dirs': {},
    }

def get_subdir_node(dir_tree, subdir_path):
    """
    Args:
        dir_tree (dict): root directory to search node for.
        subdir_path (str): path to subdirectory node to find.

    Returns:
        dict: directory tree node to the specified subdirectory.
    """
    node = dir_tree

    if subdir_path:
        dirs = subdir_path.split('/')
        for d in dirs:
            node = node['dirs'][d]

    return node

def get_subdir_parent(dir_tree, subdir_path):
    """
    Args:
        dir_tree (dict): root directory to search node for.
        subdir_path (str): path to subdirectory node whose parent we are
            looking for.

    Returns:
        dict: directory tree node to the specified subdirectory parent node.
    """
    parent_path, curr_dir = os.path.split(subdir_path)
    return get_subdir_node(dir_tree, parent_path), curr_dir


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
