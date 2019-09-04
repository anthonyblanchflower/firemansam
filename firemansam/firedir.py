import glob
import os
from typing import Dict, List, Any, Union

from firemansam.firedict import firedict


def firedir(filedir):

    fixes_list: List[Dict[str, Union[int, Any]]] = []
    try:
        # populate list of python files in target dir and scale of fixes for Python 3 compatibility
        for filename in glob.iglob('{}/**/*.py'.format(filedir), recursive=True):
            if os.path.isfile(filename):
                fixes_list.append(firedict(filename))
    except OSError as err:
        print("OS error: {0}".format(err))
    else:
        return fixes_list
