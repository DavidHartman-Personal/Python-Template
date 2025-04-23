# Git repo - Python Template

A Python Template Repository used to do create github repositories.

See my confluence page [Organizing Python Resources] for more details.

## Usage of template

The following steps should be completed once a pyton project has been created using this template based on the type 
of python application being created:

1. One-off script - This would reflect the simplest pyton application that is typically just a single python script.
2. Installable single package - Will have all python files together in a single directory with other files kept at 
   the top directory (e.g. README, .gitignore, etc.)
3. Application with Internal Packages - In larger applications, you may have one or more internal packages that are 
   either tied together with a main runner script or that provide specific functionality to a larger library you are 
   packaging.
4. Option to turn python project/script/module into a operating system command line executable.

To test using this template repository, the following steps can be done.

1. Create new repo using this repo as the template.  This can be done by running the following command: 
   1. `gh repo create <repo new> --template DavidHartman-Personal/Python-Template --private`
2. Test changes to template including updates to the sample code, documentation, etc.
3. Delete the repo with the following once testing is complete.  The delete_repo permission needs to be granted first.
   1. `gh auth refresh -h github.com -s delete_repo`
   2. `gh repo delete <repo to delete>`
4. Cleanup local PyCharm project.  Needs to be run as sudo to handle .git/ directory:
   1. `sudo rm -rf <project directory>`
   2. NOTE: May need to run this twice to handle permissions issue with .git/ directory.

`gh repo create test_repo --template DavidHartman-Personal/Python-Template --private`
`gh repo delete test_repo --yes`
Need to run the following twice due to permissions issue.
`sudo rm -rf /mnt/c/Users/david/Dropbox/Programming/Python/PyCharmProjects/test_repo`

For each of these project scenarios the first steps include:

1. Create new repo using this repo as the template.  This can be done by running the following command: 
   1. `gh repo create <repo new> --template DavidHartman-Personal/Python-Template --private`
2. Clone repo locally using Git->Clone in Pycharm


### One-off script

1. A folder that just contains python code and can be at the project root directory.
2. A single README is generally sufficient to manage documentation.
3. Use docstrings as described below.  The section below includes templates that can be used in the project.
4. The setup.py file should be updated with basic package information.
5. The file sample/core.py can be used as the starting point for the one-off script.  It can be copied to the top 
   level directory along with the __init__.py file and the sample/ folder can be deleted.
6. The docs/ and mkdocs-docs/ folders can be removed with the README_BASE.md being the starting point for 
   documentation.  The README.md (i.e. this file) file can be removed when no longer needed.
7. If using the mkdocs module to generate documentation, the mkdocs-docs/docs/REFERENCE.md file can be reviewed and 
   the mkdocs syntax to include python docstrings can be addeded as needed.  
8. If tests are needed, the test files in the tests/ folder can be copied to the root directory and the tests/ 
   folder can be removed.
9. The requirements.txt file should be updated to identify any required python modules/packages.

export PYTHONPATH="/path/to/other/projects/directory:$PYTHONPATH"

Running the following in the root project directory prints out package docstrings in Markdown format.  This can be 
then added to the readme file.

pydoc-markdown -p <package name (e.g. recursive_iterdir)>

pandoc -s -r html http://www.gnu.org/software/make/ -o example12.text

To convert hello.html from HTML to Markdown:

pandoc -f html -t markdown hello.html

### Installable single package

1. A folder that just contains python code and can be at the project root directory.
2. A single README is generally sufficient to manage documentation.
3. Use docstrings as described below.  The section below includes templates that can be used in the project.
4. The setup.py file should be updated with basic package information.
5. The file sample/core.py can be used as the starting point for the one-off script.  It can be copied to the top 
   level directory along with the __init__.py file and the sample/ folder can be deleted.
6. The docs/ and mkdocs-docs/ folders can be removed with the README_BASE.md being the starting point for 
   documentation.  The README.md file can be removed when no longer needed.
7. If tests are needed, the test files in the tests/ folder can be copied to the root directory and the tests/ 
   folder can be removed.
8. The requirements.txt file should be updated to identify any required python modules/packages.


Test implementation of project setup using this template:

1. Create new repo using this repo as the template.  This can be done by running the following command: 
   1. `gh repo create test_repo --template DavidHartman-Personal/Python-Template --private`
2. Clone repo locally using Git->Clone in Pycharm
3. Move core.py and __init__.py from the sample/ directory to the root directory and delete sample/ folder..
4. Move the test_basic file from the tests/ folder and delete tests/folder.
5. Use docstrings as described below.  The section below includes templates that can be used in the project.
6. Be sure to update this README file to remove any text that is not relevant for the project.

 
 [ ] Add Documentation regarding creating/running tests.


## Project/Template Organization

This section describes how this template is organized.  The code organization and examples included follow the guidance from [Hitchhiker's Guide to Python][Hitchhikers].

### mkdocs-docs/

This folder contains files needed to create and maintain project documentation. 

See the [README_DOCUMENTATION.md](mkdocs-docs/README_DOCUMENTATION.md) file for additional information. 

### sample/

The sample folder contains a simple example set of code that show how the main project code base would appear. This
folder should be renamed to align with the project being implemented. The comments in the various files provide
detailed steps that should be completed to set up a new project using this template. The main code for the project
would follow the format of the code in the core.py file. This file should be renamed to align with the code/logic
that make sense for the project.

The code organization and examples included follow the guidance from [Hitchhiker's Guide to Python][Hitchhikers].

### tests/

The sample folder contains a simple example set of code that show how the main project code base would appear. This
folder should be renamed to align with the project being implemented. The comments in the various files provide
detailed steps that should be completed to set up a new project using this template. The main code for the project
would follow the format of the code in the core.py file. This file should be renamed to align with the code/logic
that make sense for the project.

### setup.py

The setup.py file in Python serves as the control center for building, distributing, and installing Python packages. It primarily uses the setuptools library to define package metadata and handle packaging tasks. It has two main functions:
* Package Configuration:
  * It contains the setup() function, which specifies details about the package, such as:
    * Name
    * Version
    * Author information
    * Dependencies
    * Entry points
    * Data files 
* Command-Line Interface:
  * It acts as a command-line interface for various packaging-related tasks. By running python setup.py <command>, developers can perform actions like:
    * Building the package (python setup.py build)
    * Installing the package (python setup.py install)
    * Creating distributions (python setup.py sdist or python setup.py bdist_wheel)
    * Running tests (python setup.py test)
  
While setup.py was traditionally central to Python packaging, modern projects increasingly use pyproject.toml for 
metadata and build configuration. However, setup.py remains relevant, especially for older projects or when building 
source distributions.  If the project is not intended to be packaged and distributed this file can be removed or 
ignored.

## Generating/Updating Documentation - Sphinx

1. Install the sphinx plugin/module.
2. Run the sphinx-quickstart to create the initial structures
3. Update core.py to modify the path to include the project directory and add the sphinx.ext.autodoc to the extensions
   array.
4. Make updates to the index.rst file to include the Python resources to generate documentation for.

## docstring Comments

The below are templates for the various types of docstrings that should be used for any code within a project.

#### Function Header Comment Block

```python
def function_example(param1, param2withdefault=False) -> None:
    """Gets and prints the spreadsheet's header columns
    
    Longer function header comment describing details/purpose of the function
    
    Parameters:
      param1 (<data type>) : Describe param1
      param2withdefault (<data type>) : A flag used to print the columns to the console
                                        (default is False)
    Returns:
      name (<data type>): Describe return results
    
    Raises:
      IOError: An error occurred accessing the smalltable.
    """
```

#### Class Comment Block

```python
class example:
    """One line description of class
    
      Longer, multi-line description.  The init function is where descriptions of the class attributes will be defined.
   
      Attributes:
        class_attribute (<data type>) : Description of class attribute.
        class_attribute_with_default (<data type>) : Class attribute with default value. (default=2)
   
      Methods:
        class_method (param1=<default>) : Example class method
      """

    def __init__(
            self,
            class_attribute: <

        data
    type >,
    class_attribute_with_default: < data
    type > = 2
    ) -> None
    """init function for class
    
    Describe any logic performed, especially any aside from a simple assignment of the input value.
    
    Attributes:
      class_attribute (<data type>) : Description of class attribute.
      class_attribute_with_default (<data type>) : Class attribute with default value. (default=2)
    
    """
    self.class_attribute = class_attribute
    self.class_attribute_with_default = class_attribute_with_default

```

#### Variables

A single line description for a variable should be formatted as below:

```python
#: <provide variable description>
variable_one = "hello"
```

#### Module docstring/comments

```python
"""A one line summary of the module or program, terminated by a period.

    Leave one blank line.  The rest of this docstring should contain an
    overall description of the module or program.  Optionally, it may also
    contain a brief description of exported classes and functions and/or usage
    examples.
    
    Methods/Functions:
        - `add(a, b)` - Returns the sum of two numbers.
        - `subtract(a, b)` - Returns the difference of two numbers.
        - `multiply(a, b)` - Returns the product of two numbers.
        - `divide(a, b)` - Returns the quotient of two numbers.
    
    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0
 
    Usage example:
   
      foo = ClassFoo()
      bar = foo.FunctionBar()
    
    References:
        Note any references including links
"""
```

<!---
Comment: Add any Reference links below.  Anywhere above this block in this Markdown file, include just the 
text within the square brackets.  E.g. [reference]
-->
[Organizing Python Resources]: https://davidhartman.atlassian.net/wiki/spaces/PYTHON/pages/196629
[Hitchhikers]: https://python-docs.readthedocs.io/en/latest/writing/structure.html  "Hitchhikers Guide to Python"
[mkdocs documentation]: https://www.mkdocs.org/
