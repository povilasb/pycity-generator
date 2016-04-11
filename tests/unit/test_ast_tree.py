import ast

from hamcrest import assert_that, has_length, is_

from python import AstTree

import test_utils


def test_class_nodes_returns_class_definition_child_nodes():
    src = """
class Test1(object):
    pass
def func1():
    pass
class Test2(object):
    pass
"""
    source_tree = AstTree(ast.parse(src))

    class_nodes = source_tree.class_nodes()

    assert_that(class_nodes, has_length(2))


def test_function_nodes_returns_function_definition_child_nodes():
    src = """
def func1():
    pass
class Test1(object):
    pass
def func2():
    pass
"""
    source_tree = AstTree(ast.parse(src))

    function_nodes = source_tree.function_nodes()

    assert_that(function_nodes, has_length(2))


def test_loc_returns_lines_of_code():
    src = """
def func1(arg1, arg2, arg3):
    arg1 = arg2
    arg2 = arg3
    pass
"""
    function = AstTree(test_utils.make_function_node(src))

    assert_that(function.loc(), is_(4))
