# Python Automated Tests

## Getting started

Source code: git@gitlab.meetic.ilius.net:a.mihut/python-automated-unit-tests.git

#### Configuration

Environment settings: \core\resources\configuration\environments.yml

Unit tests: \core\resources\configuration\test_cases.yml

Testing sites: \core\resources\sites.yml - overwrite by \tests\TestName\resources\sites.yml

Test users: \core\resources\users.yml overwrite by \tests\TestName\resources\users.yml

Unit test main configuration file: \tests\TestName\resources\configuration\configuration.yml

Variables:
- executable: executable class namespace (used by unittest.TestLoader to load all tests)
- environment: dev, recette, prod (the environment settings are loaded based on this value)
- external_resources: array of custom config files
- driver: name of the selenium web driver (load by \core\utils\DriverFactory.py)

## Installation

The easiest way to install Python packages is via [Pip](http://www.pip-installer.org):

Requirements:

- [Python](https://packaging.python.org/tutorials/installing-packages/) v3.5+
- [Selenium](http://selenium-python.readthedocs.io/installation.html) v3.0+
- [junit_xml](https://pypi.python.org/pypi/junit-xml/1.7) v1.7
````
$ pip install junit_xml
````

- htmlxmltestrunner
````
$ git clone git@bitbucket.org:AlinMihut/htmlxmltestrunner.git
$ cd htmlxmltestrunner
$ python setup.py install
````

Get the latest development version:
````
$ git clone git@gitlab.meetic.ilius.net:a.mihut/python-automated-unit-tests.git
````

## Usage
````
$ python Main.py
````

## Features

- HTML reports: \app\reports\html\\**\\\*.html
- XML reports: \app\reports\xml\\**\\\*.xml

## Contribute

Source Code: https://gitlab.meetic.ilius.net/a.mihut/python-automated-unit-tests

## TODO
* ~~Simplify FormLoginComponent~~
* Refactor /utils/authentication/
* Create FormRegistrationComponent and WebDriverRegistrationComponent - after /utils/authentication refactor
* Refactor RegistrationExecutableTest (use AventadorLanding to register a user)
* Improve htmlxmltestrunner test case stdout and stderr (add better success, error, failure or skipped info) in \Python\Lib\site-packages\html_testRunner-1.0.3-py3.5.egg\HtmlTestRunner\result.py - _HtmlAndXmlTestResult->__report_junit_xml_test_cases
* Create testing framework (TBD)
* POC - callable tests (simplify sites iteration within each test), distinguishing test iterations using subtests
* Implement date roulette test
* Update docs
* Retriable action 

## Support

If you have any questions, please let us know.

Development:
* Levi Molnár <lmolnar@pentalog.fr>
* Stefan Tomoiaga <stomoiaga@pentalog.fr>
* K Erwin <ekaralyos@pentalog.fr>
* Alin Mihut <alinmihutz@gmail.com>
