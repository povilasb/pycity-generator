import ast

from hamcrest import assert_that, is_, has_length

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

def test_argument_count_returns_number_of_arguments_within_function_node():
    src = """
def fun1(arg1, arg2, arg3):
    pass
"""
    fn_node = test_utils.make_function_node(src)

    args_count = python.argument_count(fn_node)

    assert_that(args_count, is_(3))
