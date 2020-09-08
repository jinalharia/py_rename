from py_rename.main import parse_args
import pytest


def test_parser_dryrun():
    args = parse_args(["-n"])
    assert args.dryrun == True


def test_parser_command():
    args = parse_args(["lower"])
    assert args.command == "lower"


def test_parser_incorrect_command():
    with pytest.raises(SystemExit):
        parse_args(["rename"])
