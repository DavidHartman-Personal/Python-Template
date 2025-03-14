"""Short description of the main script/module

This is considered the main or core script for a project/task.  It is likely where the __main__ function
would be defined.

Any imports/dependencies/requirements should be noted here (e.g. argparse, etc)

"""

# import any functions inside or outside of this module.  If no helpers are needed it can be removed from here
# as well as remove the file from the sample module.

__version__ = '2021.01'
__author__ = 'David Hartman'

import sys
import os
import datetime
from . import helpers

# The below is how variables should be documented with docstrings

# <Data Type>: Variables should have a comment as in this case. <Data Type>: can be used to note the variables data type
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def get_hmm() -> str:
    """This is a placeholder for an internal function to the module.  it should be removed/replaced as needed.

    Longer description of function

    Returns:
        str: Description of any returned value(s)
    """
    return 'hmmm...'


def function_example(param1, param2withdefault=False) -> None:
    """This is a placeholder for an internal function to the module.  it should be removed/replaced as needed.

    Longer description of function

    Returns:
        <Data Type>: Description of any returned value(s)

    """
    if helpers.get_answer():
        print(get_hmm())


if __name__ == "__main__":
    function_example(param1="")
