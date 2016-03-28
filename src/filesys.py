import os

class Dir:
    def __init__(self, path):
        self.path = path

    def py_files(self):
        """Collects python files from directory.

        Returns:
            dict: directory tree with python files collected only.
        """
        tree = {
            'files': [],
            'dirs': [],
        }

        for root, _, dir_files in os.walk(self.path):
            tree['files'] = [f for f in dir_files if f.endswith('.py')]

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
