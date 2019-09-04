from typing import Dict, Any, Union
from firemansam.firecheck import firecheck


def firedict(filename):

    # get fixes string from firecheck
    fixes_out = firecheck(filename)
    # initialise fixes dictionary for filename
    fixes_dict: Dict[str, Union[int, Any]] = {"file": filename}
    # populate scale of fixes for Python 3 compatibility to dictionary
    fixes_scale: int = 0
    for fixes_line in fixes_out.splitlines():
        if fixes_line.startswith('-') and not fixes_line.startswith('---'):
            fixes_scale += 1
    fixes_dict["scale"] = fixes_scale
    print(fixes_dict)
    return fixes_dict
