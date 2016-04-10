import ast

from hamcrest import assert_that, has_length

from python import AstTree


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
