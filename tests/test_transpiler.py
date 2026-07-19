from redpanda import transpile_source


def test_print():
    assert transpile_source("print('Hello')") == "打印('Hello')"


def test_if():
    source = "if True:\n    pass"
    result = transpile_source(source)

    assert "如果" in result
    assert "真" in result
    assert "跳过" in result


def test_strings_not_translated():
    source = 'print("print if else")'
    result = transpile_source(source)

    assert '打印("print if else")' == result