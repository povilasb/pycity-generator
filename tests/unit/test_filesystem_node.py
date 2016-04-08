from hamcrest import assert_that, is_

import filesys as fs


def test_full_path_returns_root_path_and_file_name_combined():
    test_file = fs.Node('/root/path', 'file.py')

    assert_that(test_file.full_path, is_('/root/path/file.py'))
