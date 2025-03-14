"""This module/package level initialization file.

    The __init__.py file is a Python file that is executed when a package is imported. __init__.py is a special file
    used in Python to define packages and initialize their namespaces. It can contain an initialization code that
    runs when the package is imported. Without this file, Python won't recognize a directory as a package. It serves
    two main purposes:

    It marks the directory as a Python Package so that the interpreter can find the modules inside it. It can contain
    initialization code for the Package, such as importing submodules, defining variables, or executing other code.

"""

# The __all__ variable identifies what packages are to be included if a wildcard import is used in the project.
# Remove the commented lines in this array and include others as needed.
__all__ = [
    # "echo",      # refers to the 'echo.py' file
    # "surround",  # refers to the 'surround.py' file
    # "reverse",   # !!! refers to the 'reverse' function now !!!
]