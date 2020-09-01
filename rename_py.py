__author__ = "JH"
__date__ = "2020-08-31"
__license__ = "MIT"
__version__ = "0.1.0"

import os
import re
import argparse
from pathlib import Path
import pprint


filenames = sorted([str(f) for f in Path().iterdir()])


class RenameIt(object):
    """Class RenameIt
    
    Constructor args:
     :dryrun: Just dry run, no actions performed
     :silent: Bare minimum will be printed

    """

    def __init__(self, dryrun, silent, full, pattern=None, replacement=None):
        self.silent = silent
        self.dryrun = dryrun
        self.full = full
        self.pattern = pattern
        self.replacement = replacement

        if self.dryrun:
            print("Performing DryRun: No actions will be taken")

        self.filenames = sorted([str(f) for f in Path().iterdir()])
        matched = sum([self.match_filename(filename, pattern, replacement, self.full) for filename in self.filenames])
        self._print(f'files matched: {matched}')

        # if self.pattern is None:


    def _print(self, *msg):
        """Print msg if not silent
        :msg: *str, What to print
        :return: None
        """
        if not self.silent:
            print(msg)

    def _rename(self, old_name, new_name):
        """Generic rename method with error handling
        :old_name: str, Filename to change
        :new_name: str, Filename to rename to
        :return: None
        """
        try:
            if not self.dryrun:
                # os.rename(old_name, new_name)
                self._print(f"real renaming: {old_name} --> {new_name}")
            self._print(f"renaming: {old_name} --> {new_name}")

        except OSError as e:
            self._print(f"Failed to rename {old_name} --> {new_name}: {e}")

    def match_filename(self, filename, pattern, replacement, full):
        if full:
            match = re.fullmatch(pattern, filename)
        else:
            match = re.search(pattern, filename)

        return self.filename_pattern_rename(filename, pattern, replacement, match)

    def filename_pattern_rename(self, filename, pattern, replacement, match):
        if not match:
            self._print(f"not matched {filename}")
            return False

        groups = match.groups()
        group_kwargs = {f"group_{idx + 1}": group for idx, group in enumerate(groups)}

        if replacement is None:
            self._print(f"matched {filename}")
            return True

        new_name = re.sub(pattern, replacement, filename)
        self._rename(filename, new_name)
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python bulk rename tool for multiple files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s version " + __version__
    )
    parser.add_argument(
        "-s", "--silent", help="do not print output", action="store_true"
    )
    parser.add_argument(
        "-d",
        "--dryrun",
        action="store_true",
        help="Dry run: print names of files to be renamed, but don't rename",
    )
    parser.add_argument("-p", "--pattern", help="Regex pattern to match filenames")
    parser.add_argument(
        "-r", "--replacement", help="Replacement regex pattern for renamed files"
    )
    parser.add_argument(
        "-f",
        "--full",
        action="store_true",
        help="Match only full filename against pattern",
    )

    args = parser.parse_args()
    rename_it = RenameIt(
        args.dryrun, args.silent, args.full, args.pattern, args.replacement
    )
    pprint.pprint(vars(args))
    # pprint.pprint(filenames)
