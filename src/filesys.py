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

def read_file(fname):
    with open(fname, 'r') as f:
        return f.read()
