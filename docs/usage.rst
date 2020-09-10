Usage
========

.. role:: bash(code)
   :language: bash

Command line interface
-----------------------

Enter :bash:`py-rename -h` for help

.. code-block:: bash

    $ py-rename -h

    py-rename - Python rename tool for multiple files

    Usage:
    py-rename [OPTIONS] COMMAND [COMMAND-OPTIONS]

    Positional arguments:
        rename              rename files based on regex pattern
        match               rename files based on regex pattern
        prefix              prefix filenames with prefix string
        postfix             postfix filenames with prefix string
        lower               convert filenames to lowercase
        replace             replace spaces in filenames to _
        camelcase           convert filenames to camel case

    Options:
      -h, --help            show this help message and exit
      -V, --version         show program version number and exit
      -s, --silent          do not print output (default: False)
      -n, --dryrun          Dry run: print names of files to be renamed, but do not
                            rename (default: False)
      -f, --full            Match only full filename against pattern (default:
                            False)

Subcommand usage example:

.. code-block:: bash

    $ py-rename rename -h

    Positional arguments:
      pattern      regex pattern to match filenames
      replacement  replacement regex pattern for renamed files

    Options:
      -h, --help   show this help message and exit