import ast

from hamcrest import assert_that, calling, raises, is_

from python import ClassAst, AstTree


def test_constructor_raises_exception_if_the_specified_ast_node_to_wrap_is_not_class():
    src = """
def func1():
    pass
"""
    assert_that(
        calling(ClassAst).with_args(ast.parse(src)),
        raises(ValueError)
    )


def test_method_count_returns_number_of_methods_within_a_class():
    src = """
class TestClass(object):
    def method1(self):
        pass
    def method2(self):
        pass
"""
    class_node = AstTree(ast.parse(src)).classes()[0]

    assert_that(class_node.method_count(), is_(2))
