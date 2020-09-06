import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pathlib import Path
from py_rename.py_rename import RenameIt

def test_rename():
    cwd = os.getcwd()
    try:
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


def test_prefix():
    cwd = os.getcwd()
    try:
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
    cwd = os.getcwd()
    try:
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
    cwd = os.getcwd()
    try:
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
    cwd = os.getcwd()
    try:
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
    cwd = os.getcwd()
    try:
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
    cwd = os.getcwd()
    try:
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
    cwd = os.getcwd()
    try:
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
