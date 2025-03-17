import pytest
import subprocess
import sys
import os
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "srcs/day00"))


def test_python_day00_ex00():
    result = subprocess.run(["python3", "../srcs/day00/ex00/Hello.py"],
            capture_output=True,
            text=True
            )
    output = result.stdout

    assert "['Hello', 'World!']" in output
    assert "('Hello', 'Germany!')" in output
    assert "{'Hello', 'Heilbronn!'}" or "{'Heilbronn!', 'Hello'}" in output
    assert "{'Hello': '42Heilbronn!'}" in output


def test_python_day00_ex01():
    result = subprocess.run(["../srcs/day00/ex01/format_ft_time.py",
    "1666355857.3622"],
            capture_output=True,
            text=True
            )
    output = result.stdout
    assert "Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation"
    assert "Oct 21 2022" in output


from ex02.find_ft_type import all_thing_is_obj
from ex03.NULL_not_found import NULL_not_found
from ex04.whatis import main as whatis
from utils import run_flake8


def test_python_day00_ex02(capsys):
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    assert 42 == all_thing_is_obj(ft_list)
    captured = capsys.readouterr()
    assert 'list' in captured.out

    assert 42 == all_thing_is_obj(ft_tuple)
    captured = capsys.readouterr()
    assert 'tuple' in captured.out

    assert 42 == all_thing_is_obj(ft_set)
    captured = capsys.readouterr()
    assert 'set' in captured.out

    assert 42 == all_thing_is_obj(ft_dict)
    captured = capsys.readouterr()
    assert 'dict' in captured.out

    assert 42 == all_thing_is_obj("Brian")
    captured = capsys.readouterr()
    assert 'str' in captured.out

    assert 42 == all_thing_is_obj("Toto")
    captured = capsys.readouterr()
    assert 'str' in captured.out

    assert 42 == all_thing_is_obj(10)
    captured = capsys.readouterr()
    assert 'int' in captured.out


def test_python_day00_ex03(capsys):
    assert 0 == NULL_not_found(None)
    captured = capsys.readouterr()
    assert "None <class 'NoneType'>" in captured.out

    assert 0 == NULL_not_found(float("NaN"))
    captured = capsys.readouterr()
    assert "nan <class 'float'>" in captured.out

    assert 0 == NULL_not_found(0)
    captured = capsys.readouterr()
    assert "0 <class 'int'>" in captured.out
    
    assert 0 == NULL_not_found('')
    captured = capsys.readouterr()
    assert " <class 'str'>" in captured.out
    
    assert 0 == NULL_not_found(False)
    captured = capsys.readouterr()
    assert "False <class 'bool'>" in captured.out
    
    assert 1 == NULL_not_found("Brian")
    captured = capsys.readouterr()
    assert "Type not Found" in captured.out


def test_python_day00_ex04(capsys):

    test = subprocess.run(["../srcs/day00/ex04/whatis.py", "4"],
                          capture_output=True,
                          text=True
                          )
    result = test.stdout
    assert "I'm Even." in result 

    test = subprocess.run(["../srcs/day00/ex04/whatis.py", "5"],
                          capture_output=True,
                          text=True
                          )
    result = test.stdout
    assert "I'm Odd." in result

    
    test = subprocess.run(["../srcs/day00/ex04/whatis.py"],
                          capture_output=True,
                          text=True
                          )
    result = test.stdout
    assert "AssertionError" in result

    test = subprocess.run(["../srcs/day00/ex04/whatis.py", "wrwrwe"],
                          capture_output=True,
                          text=True
                          )
    result = test.stdout
    assert "ValueError" in result


def test_python_day00_ex05():
    result = run_flake8("../srcs/day00/ex05/building.py")
    assert "" == result

