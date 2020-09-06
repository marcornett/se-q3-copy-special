#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "marcornett"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    file_list = os.listdir(dirname)

    special_pattern = re.compile(r'__(\w+)__')

    special_list = []

    for f in file_list:
        if special_pattern.findall(f):
            special_list.append(os.path.abspath(f))
    return special_list


def copy_to(path_list, dest_dir):
    """Copies special files to given directory"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for path in path_list:
        shutil.copy2(path, dest_dir)
    return f'Copied to: {dest_dir}'


def zip_to(path_list, dest_zip):
    """Creates zip folder including files from path list"""
    # try:
    print(f"Command I'm going to do: \nzip -j {dest_zip}")
    for f_path in path_list:
        f = os.path.basename(f_path)
        subprocess.run(
            f'zip -j {dest_zip} {f}',
            shell=True
        )
    # except subprocess.CalledProcessError:
    #     subprocess.check_output(
    #         "identifier",
    #         stderr=subprocess.STDOUT
    #     )
    #     print('???')
    #     print(subprocess.CalledProcessError)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument(
        'from_dir', help="Shows absolute path of directories?", nargs='+')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    if not ns:
        parser.print_usage()
        sys.exit(1)
    directory_list = ns.from_dir
    tozip = ns.tozip
    todir = ns.todir

    # Your code here: Invoke (call) your functions

    for directory in directory_list:
        paths_list = get_special_paths(directory)
        if tozip:
            zip_to(paths_list, tozip)
        elif todir:
            copy_to(paths_list, todir)
        else:
            for path in paths_list:
                print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
