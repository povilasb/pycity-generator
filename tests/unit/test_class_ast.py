import ast
import exceptions

from hamcrest import assert_that, calling, raises

from python import ClassAst


def test_constructor_raises_exception_if_the_specified_ast_node_to_wrap_is_not_class():
    src = """
def func1():
    pass
"""
    assert_that(
        calling(ClassAst).with_args(ast.parse(src)),
        raises(exceptions.ValueError)
    )
