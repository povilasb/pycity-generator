import os

class Dir:
    def __init__(self, path):
        self.path = path

    def py_files(self):
        files = []
        for root, _, dir_files in os.walk(self.path):
            files += [f for f in dir_files if f.endswith('.py')]

        return files

    def full_path(self, fname):
        return os.path.join(self.path, fname)

def read_file(fname):
    with open(fname, 'r') as f:
        return f.read()
