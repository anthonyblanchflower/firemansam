from lib2to3.main import main
from contextlib import redirect_stdout
import io
import glob
import os
import logging


def firecheck(filename):

    # reduce verbosity of logging
    logging.basicConfig(filename=os.devnull)

    # create in-memory text stream
    fixes = io.StringIO()

    # redirect standard output to text stream
    with redirect_stdout(fixes):
        # call 2to3 fixers
        main("lib2to3.fixes", [filename])

    # get fixes string from text stream
    fixes_str = fixes.getvalue()

    return fixes_str


def firedict(filename):

    # get fixes string from firecheck
    fixes_out = firecheck(filename)

    # initialise fixes dictionary for filename
    fixes_dict = {"file": filename}

    # populate scale of fixes for Python 3 compatibility to dictionary
    fixes_scale = 0
    for fixes_line in fixes_out.splitlines():
        if fixes_line.startswith('-') and not fixes_line.startswith('---'):
            fixes_scale += 1
    fixes_dict["scale"] = fixes_scale

    return fixes_dict


def firedir(filedir):

    fixes_list = []

    # populate list of python files in target dir and scale of fixes for Python 3 compatibility
    for filename in glob.iglob('{}/**/*.py'.format(filedir), recursive=True):
        if os.path.isfile(filename):
            fixes_list.append(firedict(filename))

    return fixes_list
