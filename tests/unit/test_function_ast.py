import ast
import exceptions

from hamcrest import assert_that, calling, raises, is_

from python import FunctionAst

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
    function = FunctionAst(test_utils.make_function_node(src))

    assert_that(function.argument_count(), is_(3))
