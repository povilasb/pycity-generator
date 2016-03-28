from hamcrest import assert_that, is_

from filesys import Dir

def test_subdir_returns_path_relative_to_directory():
    d = Dir('/opt/project')

    subdir = d.subdir('/opt/project/src/utils')

    assert_that(subdir, is_('src/utils'))

def test_subdir_returns_none_if_the_specified_path_is_not_inside_the_directory():
    d = Dir('/opt/project')

    subdir = d.subdir('/opt/other-project/src/utils')

    assert_that(subdir, is_(None))
