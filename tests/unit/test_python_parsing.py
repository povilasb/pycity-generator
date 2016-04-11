import ast

from hamcrest import assert_that, has_length, instance_of
from mock import patch

import test_utils
import python

def test_argument_nodes_returns_a_list_of_function_arguments():
    src = """
def fun1(arg1, arg2, arg3):
    pass
"""
    fn_node = test_utils.make_function_node(src)

    args = python.argument_nodes(fn_node)

    assert_that(args, has_length(3))


@patch('filesys.read_file')
def test_parse_module_returns_ast_tree(read_file_mock):
    read_file_mock.return_value = """
def fun1(arg1, arg2, arg3):
    pass
"""

    module = python.parse_module('dummy_module')

    assert_that(module, instance_of(python.AstTree))
