from lib2to3.main import main
from contextlib import redirect_stdout
import io
import os
import logging


def firecheck(filename):

    # reduce verbosity of logging
    logging.basicConfig(filename=os.devnull)
    try:
        # create in-memory text stream
        fixes = io.StringIO()
        # redirect standard output to text stream
        with redirect_stdout(fixes):
            # call 2to3 fixers
            main("lib2to3.fixes", [filename])
        # get fixes string from text stream
        fixes_str = fixes.getvalue()
    except IOError as err:
        print("I/O error({0}): {1}".format(err.errno, err.strerror))
    else:
        return fixes_str
