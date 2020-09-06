import os
import re
# import argparse
from pathlib import Path
# import pprint
# from .version import __version__

class RenameIt(object):
    """Class RenameIt
    
    Constructor args:
     :dryrun: Just dry run, no actions performed
     :silent: Bare minimum will be printed
     :full: Apply regex on full filenames only

    """

    def __init__(self, dryrun, silent, full):
        self.silent = silent
        self.dryrun = dryrun
        self.full = full

        if self.dryrun:
            print("Performing DryRun: No actions will be taken")

        self.filenames = sorted([str(f) for f in Path().iterdir() if f.is_file()])
        # matched = sum(
        #     [
        #         self.match_filename(filename, pattern, replacement, self.full)
        #         for filename in self.filenames
        #     ]
        # )
        # self._print(f"files matched: {matched}")

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
                os.rename(old_name, new_name)
                # self._print(f"real renaming: {old_name} --> {new_name}")
            self._print(f"renaming: {old_name} --> {new_name}")

        except OSError as e:
            self._print(f"Failed to rename {old_name} --> {new_name}: {e}")

    def bulk_rename(self, rename_func, *args):
        matched = sum(
            [
                rename_func(filename, *args)
                for filename in self.filenames
            ]
        )
        self._print(f"files matched: {matched}")

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

    def prefix_filename(self, filename, prefix_str):
        new_name = prefix_str + filename
        self._rename(filename, new_name)
        return True

    def postfix_filename(self, filename, postfix_str, include_ext=False):
        if include_ext:
            new_name = filename + postfix_str
            self._rename(filename, new_name)
            return True
        else:
            fname, fext = os.path.splitext(filename)
            new_name = fname + postfix_str + fext
            self._rename(filename, new_name)
            return True

    def lower_filename(self, filename):
        new_name = filename.lower()
        self._rename(filename, new_name)
        return True

    def replace_space(self, filename, fill_char="_"):
        new_name = filename.replace(" ", fill_char)
        self._rename(filename, new_name)
        return True

    def camel_case(self, filename):
        fname, fext = os.path.splitext(filename)
        old_name = fname.replace("_", " ")
        modified_name = re.findall(r"[\w]+", old_name.lower())
        new_name = "".join([word.title() for word in modified_name])
        new_name = new_name + fext
        self._rename(filename, new_name)
        return True

