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

# The below is how variables should be documented with docstrings

#: This effectively defines the root of the project and so adding ..\, etc is not needed in config files
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

#: Directory that contains configuration files, update as needed.
CONF_DIR = os.path.join(PROJECT_ROOT_DIR, 'conf')

#: Directory were data files/extracts/reports will be stored
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, 'data')

FILENAME_INPUT_CONFIG = os.environ.get('CONFIG_FILE_PATH',
                                       os.path.join(CONF_DIR, 'test.conf'))


from . import helpers


def get_hmm():
	"""This is a place holder for an internal function to the module.  it should be removed/replaced as needed.

	"""
	return 'hmmm...'


def function_example(param1, param2withdefault=False):
	"""This is a that can be called outside this module by way of an import."""
	if helpers.get_answer():
		print(get_hmm())

if __name__ == "__main__":
	function_example()
