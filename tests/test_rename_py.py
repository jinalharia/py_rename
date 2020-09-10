import os
from pathlib import Path
from src.py_rename import RenameIt


def test_rename():
    """
    file rename unit test
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12+Red+(000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(
            rename.match_filename, r".+\(00(\d{2})\).+", r"\1-Red.txt", False
        )
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {"00-Red.txt", "01-Red.txt", "02-Red.txt"}

        for idx in range(3):
            os.system(f'rm "0{idx}-Red.txt"')

    finally:
        os.chdir(cwd)


def test_dryrun_match(capsys):
    """
    file match unit test with dry run flag
    :param capsys: read sys out / in / err
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12+Red+(000{idx}).txt"')

        rename = RenameIt(True, False, True)
        rename.bulk_rename(rename.match_filename, r".+\(0000\).+", None, True)

        expected_output = "Performing DryRun: No actions will be taken\n('matched ab12+Red+(0000).txt',)\n('not matched ab12+Red+(0001).txt',)\n('not matched ab12+Red+(0002).txt',)\n('files matched: 1',)\n"
        captured = capsys.readouterr()
        assert captured.out == expected_output

        for idx in range(3):
            os.system(f'rm "ab12+Red+(000{idx}).txt"')

    finally:
        os.chdir(cwd)


def test_prefix():
    """
    filename prefix unit test
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12+Red+(000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.prefix_filename, "testab")
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "testabab12+Red+(0000).txt",
            "testabab12+Red+(0001).txt",
            "testabab12+Red+(0002).txt",
        }

        for idx in range(3):
            os.system(f'rm "testabab12+Red+(000{idx}).txt"')

    finally:
        os.chdir(cwd)


def test_postfix():
    """
    filename postfix unit test excluding extension
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12+Red+(000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.postfix_filename, "testab")
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "ab12+Red+(0000)testab.txt",
            "ab12+Red+(0001)testab.txt",
            "ab12+Red+(0002)testab.txt",
        }

        for idx in range(3):
            os.system(f'rm "ab12+Red+(000{idx})testab.txt"')

    finally:
        os.chdir(cwd)


def test_postfixExt():
    """
    filename postfix unit test including extension
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12+Red+(000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.postfix_filename, "testab", True)
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "ab12+Red+(0000).txttestab",
            "ab12+Red+(0001).txttestab",
            "ab12+Red+(0002).txttestab",
        }

        for idx in range(3):
            os.system(f'rm "ab12+Red+(000{idx}).txttestab"')

    finally:
        os.chdir(cwd)


def test_lower():
    """
    filename lowercase unit test
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ReD+(000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.lower_filename)
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "red+(0000).txt",
            "red+(0001).txt",
            "red+(0002).txt",
        }

        for idx in range(3):
            os.system(f'rm "red+(000{idx}).txt"')

    finally:
        os.chdir(cwd)


def test_replace():
    """
    filename replace space unit test with default
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12 Red (000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.replace_space)
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "ab12_Red_(0000).txt",
            "ab12_Red_(0001).txt",
            "ab12_Red_(0002).txt",
        }

        for idx in range(3):
            os.system(f'rm "ab12_Red_(000{idx}).txt"')

    finally:
        os.chdir(cwd)


def test_replaceChar():
    """
    filename replace space unit test with other character
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12 Red (000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.replace_space, "+")
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "ab12+Red+(0000).txt",
            "ab12+Red+(0001).txt",
            "ab12+Red+(0002).txt",
        }

        for idx in range(3):
            os.system(f'rm "ab12+Red+(000{idx}).txt"')

    finally:
        os.chdir(cwd)


def test_camelcase():
    """
    filename camelcase unit test
    :return: boolean
    """
    cwd = os.getcwd()
    try:
        os.makedirs("tests/res", exist_ok=True)
        os.chdir("tests/res")

        for idx in range(3):
            os.system(f'touch "ab12 Red (000{idx}).txt"')

        rename = RenameIt(False, False, False)
        rename.bulk_rename(rename.camel_case)
        files = set([str(f) for f in Path().iterdir() if f.is_file()])
        assert files == {
            "Ab12Red0000.txt",
            "Ab12Red0001.txt",
            "Ab12Red0002.txt",
        }

        for idx in range(3):
            os.system(f'rm "Ab12Red000{idx}.txt"')

    finally:
        os.chdir(cwd)
