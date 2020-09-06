import argparse
from py_rename.version import __version__
from py_rename.py_rename import RenameIt

def main():
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
        "-n",
        "--dryrun",
        action="store_true",
        help="dry run: print names of files to be renamed, but don't rename",
    )
    parser.add_argument(
        "-f",
        "--full",
        action="store_true",
        help="Match only full filename against pattern",
    )

    subparsers = parser.add_subparsers(help="sub-command help", dest="command")
    rename_parser = subparsers.add_parser(
        "rename", help="rename files based on regex pattern"
    )
    rename_parser.add_argument("pattern", help="regex pattern to match filenames")
    rename_parser.add_argument(
        "replacement", help="replacement regex pattern for renamed files"
    )

    match_parser = subparsers.add_parser(
        "match", help="rename files based on regex pattern"
    )
    match_parser.add_argument("pattern", help="regex pattern to match filenames")

    prefix_parser = subparsers.add_parser(
        "prefix", help="prefix filenames with prefix string"
    )
    prefix_parser.add_argument(
        "string", help="string to prefix to all filenames in directory"
    )

    postfix_parser = subparsers.add_parser(
        "postfix",
        help="postfix filenames with prefix string",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    postfix_parser.add_argument(
        "string", help="string to postfix to all filenames in directory"
    )
    postfix_parser.add_argument(
        "-e",
        "--include_ext",
        action="store_true",
        default=False,
        help="include file extension when postifixing string",
    )

    lower_parser = subparsers.add_parser("lower", help="convert filenames to lowercase")

    replace_parser = subparsers.add_parser(
        "replace",
        help="replace spaces in filenames to _",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    replace_parser.add_argument(
        "-c", "--fill_char", default="_", help="fill character to replace spaces"
    )

    camelCase_parser = subparsers.add_parser(
        "camelcase", help="convert filenames to camel case"
    )

    args = parser.parse_args()
    rename_it = RenameIt(args.dryrun, args.silent, args.full)

    if args.command == "rename":
        rename_it.bulk_rename(rename_it.match_filename, args.pattern, args.replacement, args.full)
    elif args.command == "match":
        rename_it.bulk_rename(rename_it.match_filename, args.pattern, None, args.full)
    elif args.command == "prefix":
        rename_it.bulk_rename(rename_it.prefix_filename, args.string)
    elif args.command == "postfix":
        rename_it.bulk_rename(rename_it.postfix_filename, args.string, args.include_ext)
    elif args.command == "lower":
        rename_it.bulk_rename(rename_it.lower_filename)
    elif args.command == "replace":
        rename_it.bulk_rename(rename_it.replace_space, args.fill_char)
    elif args.command == "camelcase":
        rename_it.bulk_rename(rename_it.camel_case)
