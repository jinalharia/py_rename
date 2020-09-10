import os
import re
from pathlib import Path


class RenameIt(object):
    """
    This is a generic Rename class with several methods for various types of renaming.

    Constructor args:

    :param dryrun: just a dry run, no actual renaming performed
    :type dryrun: str, optional
    :param silent: bare minimum will be printed
    :type silent: str, optional
    :param full: apply regex on full filenames only
    :type full: str, optional
    """

    def __init__(self, dryrun, silent, full):
        """
        Constructor for the class.

        :param dryrun: just a dry run, no actual renaming performed
        :param silent: bare minimum will be printed
        :param full: apply regex on full filenames only
        """
        self.silent = silent
        self.dryrun = dryrun
        self.full = full

        if self.dryrun:
            print("Performing DryRun: No actions will be taken")

        self.filenames = sorted([str(f) for f in Path().iterdir() if f.is_file()])

    def _print(self, *msg):
        """
        Print msg if not silent

        :param msg: *str, what to print
        :return: None
        """
        if not self.silent:
            print(msg)

    def _rename(self, old_name, new_name):
        """
        Generic rename method with error handling

        :param old_name: str, filename to change
        :param new_name: str, filename to rename to
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
        """
        Apply renaming function to multiple files

        :param rename_func: specific renaming function to apply
        :param args: args for the specific renaming function
        :return: None
        """
        matched = sum([rename_func(filename, *args) for filename in self.filenames])
        self._print(f"files matched: {matched}")

    def match_filename(self, filename, pattern, replacement, full):
        """
        Match filename function to generate matches

        :param filename: str, filename
        :param pattern: str, matching regex pattern
        :param replacement: str, replacing regex pattern, can be None
        :param full: boolean, apply matching pattern on full filename
        :return: True or False based on filename pattern rename
        """
        if full:
            match = re.fullmatch(pattern, filename)
        else:
            match = re.search(pattern, filename)

        return self.filename_pattern_rename(filename, pattern, replacement, match)

    def filename_pattern_rename(self, filename, pattern, replacement, match):
        """
        Rename or match regex pattern, do the rename and return True or False if matched

        :param filename: str, filename
        :param pattern: str, matching regex pattern
        :param replacement: str, replacing regex pattern, can be None
        :param match: match input based on re library
        :return: True or False depending on if match or no match
        """
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
        """
        Apply prefix to filename

        :param filename: str, filename
        :param prefix_str: str, prefix string to apply
        :return: True
        """
        new_name = prefix_str + filename
        self._rename(filename, new_name)
        return True

    def postfix_filename(self, filename, postfix_str, include_ext=False):
        """
        Apply postfix to filename

        :param filename: str, filename
        :param postfix_str: str, postfix string to apply
        :param include_ext: boolean, apply postfix to filename including file extension or not
        :return: True
        """
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
        """
        Make filename all lowercase

        :param filename: str, filename
        :return: True
        """
        new_name = filename.lower()
        self._rename(filename, new_name)
        return True

    def replace_space(self, filename, fill_char="_"):
        """
        Replace spaces with a fill character

        :param filename: str, filename
        :param fill_char: str, char to replace spaces
        :return: True
        """
        new_name = filename.replace(" ", fill_char)
        self._rename(filename, new_name)
        return True

    def camel_case(self, filename):
        """
        Amend filename to camel case

        :param filename: str, filename
        :return: True
        """
        fname, fext = os.path.splitext(filename)
        old_name = fname.replace("_", " ")
        modified_name = re.findall(r"[\w]+", old_name.lower())
        new_name = "".join([word.title() for word in modified_name])
        new_name = new_name + fext
        self._rename(filename, new_name)
        return True
