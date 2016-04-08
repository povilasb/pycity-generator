from hamcrest import assert_that, is_, instance_of
from mock import MagicMock, call, patch, ANY

import filesys as fs


def assert_called_with_files(mock, file_names):
    arg_i = 0
    for all_args in mock.call_args_list:
        args, _ = all_args

        assert_that(args[0], instance_of(fs.File))
        assert_that(args[0].name, is_(file_names[arg_i]))

        arg_i += 1


def assert_called_with_dirs(mock, dir_names):
    arg_i = 0
    for all_args in mock.call_args_list:
        args, _ = all_args

        assert_that(args[0], instance_of(fs.Directory))
        assert_that(args[0].name, is_(dir_names[arg_i]))

        arg_i += 1


@patch('os.listdir')
def test_walk_calls_callback_for_all_python_files(listdir_mock):
    listdir_mock.return_value = ['f1.py', 'f2.py', 'README.rst']
    cb = MagicMock()

    fs.walk('/dummy/path', cb)

    assert_that(cb.call_count, is_(2))

    assert_called_with_files(cb, ['f1.py', 'f2.py'])


@patch('os.listdir')
@patch('os.path.isdir')
def test_walk_calls_callback_for_all_dirs(isdir_mock, listdir_mock):
    def list_dir(path):
        if path == '/dummy/path':
            return ['dir1', 'dir2', 'README.rst']
        return []
    listdir_mock.side_effect = list_dir
    isdir_mock.side_effect = lambda path: not path.endswith('README.rst')
    cb = MagicMock()

    fs.walk('/dummy/path', cb)

    assert_that(cb.call_count, is_(2))
    assert_called_with_dirs(cb, ['dir1', 'dir2'])


@patch('os.listdir')
def test_walk_passes_the_specified_argument_to_callback(listdir_mock):
    listdir_mock.return_value = ['f1.py']
    cb = MagicMock()

    fs.walk('/dummy/path', cb, 'arg')

    cb.assert_called_with(ANY, 'arg')


@patch('os.listdir')
@patch('os.path.isdir')
def test_walk_passes_the_specified_argument_to_callback(
        isdir_mock, listdir_mock):
    listdir_mock.side_effect = [['dir1'], []]
    isdir_mock.side_effect = [True, False]

    cb = MagicMock()

    fs.walk('/dummy/path', cb, 'arg')

    cb.assert_called_with(ANY, 'arg')


@patch('os.listdir')
@patch('os.path.isdir')
def test_walk_passes_callback_result_to_next_walk_calls_for_subdirectories(
        isdir_mock, listdir_mock):
    isdir_mock.side_effect = [True, False]
    listdir_mock.side_effect = [['dir1'], ['f1.py']]
    cb = MagicMock()
    cb.return_value = 'callback result'

    fs.walk('/dummy/path', cb)

    cb.assert_called_with(ANY, 'callback result')
