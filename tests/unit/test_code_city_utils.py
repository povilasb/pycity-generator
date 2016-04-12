from hamcrest import assert_that, has_entries

import test_utils

import code_city

def test_analyze_function_returns_function_line_count():
    fn_node = test_utils.make_function_ast("""
def func():
    s = 'test'
    print(s)
""")

    stats = code_city.analyze_function(fn_node)

    assert_that(stats, has_entries(code_length=3))

def test_analyze_function_returns_argument_count():
    fn_node = test_utils.make_function_ast("""
def func(arg1, arg2):
    pass
""")

    stats = code_city.analyze_function(fn_node)

    assert_that(stats, has_entries(arguments=2))


def test_analyze_class_returns_class_line_count():
    class_node = test_utils.make_class_ast("""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
""")

    stats = code_city.analyze_class(class_node)

    assert_that(stats, has_entries(code_length=4))

def test_analyze_class_returns_method_count():
    class_node = test_utils.make_class_ast("""
class Person(object):
    def __init__(self):
        pass

    def serialize(self):
        pass
""")

    stats = code_city.analyze_class(class_node)

    assert_that(stats, has_entries(methods=2))
