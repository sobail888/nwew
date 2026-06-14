from greeter import greet


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_with_default():
    assert greet("World") == "Hello, World!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"
