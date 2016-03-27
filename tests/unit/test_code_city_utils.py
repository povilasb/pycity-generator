from hamcrest import assert_that, has_entries

import test_utils

import code_city

def test_analyze_function_returns_function_line_count():
    fn_node = test_utils.make_function_node("""
def func():
    s = 'test'
    print(s)
""")

    stats = code_city.analyze_function(fn_node)

    assert_that(stats, has_entries(code_length=3))

def test_analyze_function_returns_argument_count():
    fn_node = test_utils.make_function_node("""
def func(arg1, arg2):
    pass
""")

    stats = code_city.analyze_function(fn_node)

    assert_that(stats, has_entries(arguments=2))
