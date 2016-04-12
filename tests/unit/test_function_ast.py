import ast
import exceptions

from hamcrest import assert_that, calling, raises, is_

from python import AstTree, FunctionAst

import test_utils


def test_init_raises_exception_if_ast_node_is_not_function_definition():
    src = """
class Test1(object):
    pass
"""
    assert_that(
        calling(FunctionAst).with_args(ast.parse(src)),
        raises(exceptions.ValueError)
    )


def test_argument_count_returns_function_node_argument_count():
    src = """
def func1(arg1, arg2, arg3):
    pass
"""
    function = AstTree(ast.parse(src)).functions()[0]

    assert_that(function.argument_count(), is_(3))
