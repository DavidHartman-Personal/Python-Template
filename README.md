# Git repo - Python Template

A Python Template Repository used to do create github repositories.

See my confluence page [Organizing Python Resources] for more details.

## Usage of template

The following steps should be completed once a pyton project has been created using this template.

1. Create new repo using this repo as the template.  This can be done by running the following command: 
   1. `gh repo create <repo new> --template DavidHartman-Personal/Python-Template --private`
2. Clone repo locally using Git->Clone in Pycharm
3. Update the sample/ project directory as needed, renaming and/or remove files as needed.
4. Update the docs/ folder as needed to assist with creating project documentation.
5. Use docstrings as described below.  The section below includes templates that can be used in the project.
6. Be sure to update this README file to remove any text that is not relevant for the project.

- [ ] Add Documentation regarding creating/running tests.

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

`gh repo delete test_repo --yes`
Need to run the following twice due to permissions issue.
`sudo rm -rf /mnt/c/Users/david/Dropbox/Programming/Python/PyCharmProjects/test_repo`

## Project/Template Organization

This section describes how this template is organized.  The code organization and examples included follow the guidance from [Hitchhiker's Guide to Python][Hitchhikers].

### docs/

The docs folder contains templates and other files used to create project documentation. The documentation
generation processes utilize sphinx and supporting processes to create/update documentation and deploy documentation
via mkdocs server. See the section below on creating/updating documentation.

### mkdocs-docs/

The docs folder contains templates and other files used to create and deploy project documentation. The 
documentation is deployed using mkdocs.  
In order to deploy/use mkdocs, confirm that the following python packages are installed and available.

`python -m pip list | grep mkdoc`

The following modules should be included:
* mkdocs
* mkdocs-autorefs
* mkdocs-get-deps
* mkdocs-material
* mkdocs-material-extensions
* mkdocstrings
* mkdocstrings-python

The docs/ folder includes standard markdown files that should be created/deployed.  In order to confirm that mkdocs 
is set up and configured correctly, run the mkdocs server and navigate to the URL the documentation is being served 
on (default site is https://127.0.0.1:8000).

`mkdocs serve`

The main landing page provides details on how to further configure and deploy project documentation. See the [mkdocs 
documentation] for additional details.

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
def function_example(param1, param2withdefault=False):
    """Gets and prints the spreadsheet's header columns
    
    Longer function header comment describing details/purpose of the function
    
    Parameters:
      param1 (<data type>) : Describe param1
      param2withdefault (<data type>) : A flag used to print the columns to the console
                                        (default is False)
    Returns
      name (<data type>): Describe return results
    
    Raises
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
