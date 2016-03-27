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

    files = test_dir.py_files()

    assert_that(files, is_(['main.py', 'out.py']))
