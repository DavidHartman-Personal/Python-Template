# Base README file for Python Project

This is a template/starting README.md file that will become the projects README.md file.  The README.md file that 
contains the details of the PythonTemplate git repo should be reviewed to confirm project setup steps and then 
removed from the project.

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
6. The docs/ and mkdocs-docs/ folders can be removed with the README.md file that is in the root directory being 
   used for any documentation.
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

## Project Organization

This section describes how this project is organized. 

### <folder>/

For each folder provide a description of the folders purpose and depending on the complexity of the project, 
individual files may require some description and/or reference information. 

### <Include explanation, how-to, reference, examples and tutorials as needed>

## Project Documentation

Docstring or other reference information about the project can be included below.  This includes any docstrings 
included in project code.  
To generate markdown text for python docstrings in the project pydoc-markdown can be run to generate project 
documentation.  

`pydoc-markdown -p <package name>`

YAML configuration file used by pydoc-markdown:

```yaml
loaders:
- type: python
  search_path: [../src]
renderer:
  type: mkdocs
  pages:
  - title: API Documentation
    name: index
    contents:
    - school.*
```