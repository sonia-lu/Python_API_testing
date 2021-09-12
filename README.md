# Python_API_testing

Table of content:
1. [Introduction](#introduction)
1. [Installation](#installation)
1. [Instructions](#instructions)
1. [Other](#other)

<a name="introduction"></a>
## Introduction

`This repository was created for recriutment purposes.`

For this automation I used:
- Python
- Pytest
- Selenium

Using this repository you can perform acceptance testing for Allegro endpoints API:
- Get IDs of Allegro categories
- Get a category by ID
- Get parameters supported by a category

Since there is a low number of test cases I decided to use the `linear scripting approach`.
If you are willing to  extend the number of test cases I would recommend switching to 
`keyword driven testing approach` with the usage of behave library.

<a name="installation"></a>
##Installation

Before running automated tests it's necessary to install Python, Python modules. It's one-time installation.

1. Install Python3 and make it available in PATH.
1. Install Python modules:

    ```console
    python -m ensurepip --upgrade
    pip install -r requirements.txt
    ```
1. Generate your token by using  `get_token.py` file. But first insert your `CLIENT_ID` and `CLIENT_SECRET` into
   this file.
   ```console
    python3 get_token.py
   ```
   and wait for config.json  to be created


<a name="instructions"></a>
##Instructions

To run tests you should open `cmd` window or console in your IDE in path Python_API_testing/tests
```bash
# running all test
pytest -v

# running specific test file
pytest test_get_id_category_positive.py -s

# running specific test function
pytest -k test_first_child_categories_id_error
```

