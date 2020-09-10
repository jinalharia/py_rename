from src.main import parse_args
import pytest


def test_parser_dryrun():
    """
    parser unit test with dry run flag
    :return: boolean
    """
    args = parse_args(["-n"])
    assert args.dryrun == True


def test_parser_command():
    """
    parser unit test with lower flag
    :return: boolean
    """
    args = parse_args(["lower"])
    assert args.command == "lower"


def test_parser_incorrect_command():
    """
    parser unit test with command with incorrect arguments
    :return: boolean
    """
    with pytest.raises(SystemExit):
        parse_args(["rename"])
