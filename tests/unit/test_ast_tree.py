import ast

from hamcrest import assert_that, has_length, is_

from python import AstTree, FunctionAst, ClassAst

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


def test_classes_returns_class_definition_child_nodes():
    src = """
class Test1(object):
    pass
def func1():
    pass
class Test2(object):
    pass
"""
    source_tree = AstTree(ast.parse(src))

    class_nodes = source_tree.classes()

    assert_that(class_nodes, has_length(2))
    assert_that(class_nodes[0], is_(ClassAst))


def test_functions_returns_function_definition_child_nodes():
    src = """
def func1():
    pass
class Test1(object):
    pass
def func2():
    pass
"""
    source_tree = AstTree(ast.parse(src))

    functions = source_tree.functions()

    assert_that(functions, has_length(2))
    assert_that(functions[0], is_(FunctionAst))


def test_loc_returns_lines_of_code():
    src = """
def func1(arg1, arg2, arg3):
    arg1 = arg2
    arg2 = arg3
    pass
"""
    function = AstTree(ast.parse(src)).functions()[0]

    assert_that(function.loc(), is_(4))


def test_name_returns_function_name():
    src = """
def func_name():
    pass
"""
    function = AstTree(ast.parse(src)).functions()[0]

    assert_that(function.name, is_('func_name'))
