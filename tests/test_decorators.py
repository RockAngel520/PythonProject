import os

from src.decorators import log


def test_log_func_not_changed():
    @log()
    def my_function(x, y):
        return x + y

    assert my_function(5, 12) == 17


def test_log_ok_in_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(5, 12)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_error_in_console(capsys):
    @log()
    def my_function_with_zero(x, y):
        return x / y

    my_function_with_zero(5, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function_with_zero error: division by zero. Inputs: (5, 0), {}\n"


def test_log_error_2_in_console(capsys):
    @log()
    def my_function_with_zero(x, y):
        return x / y

    my_function_with_zero("a", "b")
    captured = capsys.readouterr()
    assert captured.out == "my_function_with_zero error: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('a', 'b'), {}\n"


def test_log_ok_in_file(tmp_path):
    file_path = tmp_path / "test_ok.txt"

    @log(filename=tmp_path / "test_ok.txt")
    def my_function(x, y):
        return x + y

    my_function(5, 12)

    assert file_path.read_text() == "my_function ok\n"
    assert os.path.exists(file_path)


def test_log_error_in_file(tmp_path):
    file_path = tmp_path / "test_error.txt"

    @log(filename=tmp_path / "test_error.txt")
    def my_function(x, y):
        return x / y

    my_function(5, 0)

    assert file_path.read_text() == "my_function error: division by zero. Inputs: (5, 0), {}\n"
    assert os.path.exists(file_path)
