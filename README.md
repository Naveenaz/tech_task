
## Pre requisites: ##

Download and install Python 3.x.

Either install via Homebrew : https://docs.python-guide.org/starting/install3/osx/

Or download via https://www.python.org/downloads/

Once installed check the version number : python3 --version It should return 3.x


## Steps to do set up ##


Install all dependencies. Navigate to the project root folder and do the following:

pip3 install -r requirements.txt --user

Install ChromeDriver from brew (make sure chromedriver supports your version of chrome)

brew install chromedriver

or

https://chromedriver.chromium.org/downloads

## Running UI tests: ##

To run individual test:
```python
python3 -m pytest -s ui_tests.py::InputFormsCheck::test_click_submit_without_value
```

To run suites:

```python
python3 -m pytest -s test_example_form.py
```

Please see sample output in ui_tests/output/output.txt.

## Running API tests: ##

To run individual test:

```python
python3 -m pytest -s api_tests.py::APITester::test_api_response_contact_info
```

To run suites:

```python
python3 -m pytest -s api_tests.py
```

Please see sample output in api_tests/output/output.txt.


#### Note: I have setup workflows. They need URL/software working on the host before testing. Also, might need to adjust the path of test file. ####
