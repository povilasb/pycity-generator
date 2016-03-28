from hamcrest import assert_that, is_

import filesys as fs
from filesys import Dir

def test_subdir_returns_path_relative_to_directory():
    d = Dir('/opt/project')

    subdir = d.subdir('/opt/project/src/utils')

    assert_that(subdir, is_('src/utils'))

def test_subdir_returns_none_if_the_specified_path_is_not_inside_the_directory():
    d = Dir('/opt/project')

    subdir = d.subdir('/opt/other-project/src/utils')

    assert_that(subdir, is_(None))

def test_make_dir_node_returns_dict_with_files_and_dirs_entries():
    node = fs.make_dir_node()

    assert_that(node, is_({'files': [], 'dirs': {}}))

def test_get_subdir_node_returns_dict_to_directory_traversing_directory_childs():
    fs_tree = fs.make_dir_node()

    io_dir = fs.make_dir_node()
    io_dir['files'].append('stdout.py')

    src_dir = fs.make_dir_node()
    src_dir['dirs']['io'] = io_dir

    fs_tree['dirs']['src'] = src_dir

    found_dir = fs.get_subdir_node(fs_tree, 'src/io')

    assert_that(found_dir, is_({'files': ['stdout.py'], 'dirs': {}}))

def test_get_subdir_node_returns_root_node_when_empty_path_string_is_given():
    fs_tree = fs.make_dir_node()

    subdir_node = fs.get_subdir_node(fs_tree, '')

    assert_that(subdir_node, is_(fs_tree))

def test_get_subdir_parent_returns_dict_to_directory_which_is_one_level_up_from_the_specified_subdirectory_path():
    fs_tree = fs.make_dir_node()

    parent_dir, _ = fs.get_subdir_parent(fs_tree, 'subdir')

    assert_that(parent_dir, is_(fs_tree))

def test_get_subdir_parent_returns_current_directory_name():
    fs_tree = fs.make_dir_node()

    _, curr_dir_name = fs.get_subdir_parent(fs_tree, 'subdir')

    assert_that(curr_dir_name, is_('subdir'))
