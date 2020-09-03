import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rename_py import RenameIt
from pathlib import Path

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
