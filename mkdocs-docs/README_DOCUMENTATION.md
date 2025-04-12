# Project Documentation

This readme includes details for managing project documentation.  

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
documentation] for additional details.  The markdown files located in mkdocs-docs/docs should be updated as needed 
to keep project documentation updated and accurate.

<!---
Comment: Add any Reference links below.  Anywhere above this block in this Markdown file, include just the 
text within the square brackets.  E.g. [reference]
-->
[Organizing Python Resources]: https://davidhartman.atlassian.net/wiki/spaces/PYTHON/pages/196629
[Hitchhikers]: https://python-docs.readthedocs.io/en/latest/writing/structure.html  "Hitchhikers Guide to Python"
[mkdocs documentation]: https://www.mkdocs.org/
