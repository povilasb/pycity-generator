import os

from hamcrest import assert_that, is_

from filesys import Dir

def this_dir():
    """Returns directory path where this file is located.
    """
    return os.path.dirname(
        os.path.realpath(__file__)
    )

def fixture_dir(fixture_name):
    """
    Returns:
        str: path to python project fixture.
    """
    return '%s/fixtures/%s' % (this_dir(), fixture_name)

def test_py_files_collects_all_python_source_files_from_specified_directory():
    test_dir = Dir(fixture_dir('project1'))

    tree = test_dir.py_files()

    assert_that(tree['files'], is_(['main.py', 'out.py']))

def test_py_files_collects_all_python_files_recursively():
    test_dir = Dir(fixture_dir('project-with-subdir'))

    tree = test_dir.py_files()

    assert_that(tree, is_({
        'files': ['main.py'],
        'dirs': {
            'output': {
                'files': ['__init__.py', 'stdout.py'],
                'dirs': {},
            }
        },
    }))
