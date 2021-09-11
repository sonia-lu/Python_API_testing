# Python_API_testing

Table of content:
1. [Introduction](#introduction)
1. [Installation](#installation)
1. [Instructions](#instructions)
1. [Other](#other)

<a name="introduction"></a>
## Introduction

`This repository was created for recriutment purpose.`

For this automation I used:
- python
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
    pip install selenium
    pip install requests
    pip install pytest
    ```
1. Generate yor token by updating`api_allegrp.php` with your `CLIENT_ID` and `CLIENT_SECRET`
and run this file 
   ```console
    php api_allegrp.php
   ```
   and then copy your token and paste in all files starting  with `test_`

<a name="instructions"></a>
##Instructions

To run tests you should open `cmd` window or console in your IDE in path Python_API_testing/tests
```bash
# running all test
pytest -v

# running specific test file
pytest test_get_id_category_positive.py -v

# running specific test in test file
pytest 
```

<a name="other"></a>
##Other