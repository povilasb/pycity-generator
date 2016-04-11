import ast
import exceptions

from hamcrest import assert_that, calling, raises, is_

from python import ClassAst

import test_utils


def test_constructor_raises_exception_if_the_specified_ast_node_to_wrap_is_not_class():
    src = """
def func1():
    pass
"""
    assert_that(
        calling(ClassAst).with_args(ast.parse(src)),
        raises(exceptions.ValueError)
    )


def test_method_count_returns_number_of_methods_within_a_class():
    src = """
class TestClass(object):
    def method1(self):
        pass
    def method2(self):
        pass
"""
    class_node = ClassAst(test_utils.make_class_node(src))

    assert_that(class_node.method_count(), is_(2))
