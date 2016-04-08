import os

from hamcrest import assert_that, is_, instance_of
from mock import MagicMock, call

import filesys as fs


def assert_called_with_fs_nodes(mock, fs_nodes):
    arg_i = 0
    for all_args in mock.call_args_list:
        args, _ = all_args

        assert_that(args[0], instance_of(type(fs_nodes[arg_i])))
        assert_that(args[0].name, is_(fs_nodes[arg_i].name))

        arg_i += 1


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


def test_walk_collects_all_python_files_recursively():
    cb = MagicMock()

    fs.walk(fixture_dir('project-with-subdir'), cb)

    assert_that(cb.call_count, is_(4))
    assert_called_with_fs_nodes(cb, [
        fs.File('', 'main.py'), fs.Directory('', 'output'),
        fs.File('', '__init__.py'), fs.File('', 'stdout.py')
    ])
